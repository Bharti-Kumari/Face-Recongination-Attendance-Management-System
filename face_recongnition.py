from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import threading

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x760+0+0")
        self.root.title("Face Recognition System")

        self.face_recognition_running = False
        self.face_recognition_thread = None

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 28, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1360, height=40)

        # 1st image
        img_top = Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\FD1.jpg")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=42, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\FD1.jpg")
        img_bottom = img_bottom.resize((700, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=653, y=42, width=700, height=700)

        # button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.start_face_recognition, font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=180, y=600, width=350, height=40)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def mark_attendance(self, i, r, n, d):
        try:
            with open("Attendance.csv", "r+", newline="\n") as f:
                myDataList = f.readlines()
                name_list = [line.split(",")[0] for line in myDataList]
                
                if i not in name_list:
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtString = now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                    print(f"Attendance marked for {i}, {r}, {n}, {d}")
                else:
                    print(f"Attendance already marked for {i}, {r}, {n}, {d}")
        except Exception as e:
            print(f"Error writing to attendance file: {e}")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            if img is None:
                messagebox.showerror("Error", "Image is empty in draw_boundary")
                return []

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            highest_confidence = 0
            best_match = None

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                if confidence > highest_confidence:
                    highest_confidence = confidence
                    best_match = (id, confidence, x, y, w, h)

            if best_match and highest_confidence > 77:
                id, confidence, x, y, w, h = best_match
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Kittu@123", database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select name from student where id=%s", (str(id),))
                    n = my_cursor.fetchone()
                    n = "+".join(n) if n else "Unknown"

                    my_cursor.execute("select roll from student where id=%s", (str(id),))
                    r = my_cursor.fetchone()
                    r = "+".join(r) if r else "Unknown"

                    my_cursor.execute("select dep from student where id=%s", (str(id),))
                    d = my_cursor.fetchone()
                    d = "+".join(d) if d else "Unknown"

                    my_cursor.execute("select id from student where id=%s", (str(id),))
                    i = my_cursor.fetchone()
                    i = "+".join(i) if i else "Unknown"

                    if n != "Unknown" and r != "Unknown" and d != "Unknown" and i != "Unknown":
                        cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(i, r, n, d)
                    else:
                        print(f"Data for ID {id} is incomplete or not found")
                        cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

                except Exception as e:
                    print(f"Database query failed: {e}")
                    cv2.putText(img, "Error", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                finally:
                    conn.close()
            else:
                cv2.putText(img, "Unknown Face", (20, 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            return features

        def recognize(img, clf, faceCascade):
            if img is None:
                messagebox.showerror("Error", "Image is empty in recognize")
                return img
            draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while self.face_recognition_running:
            ret, img = video_cap.read()
            if not ret or img is None:
                messagebox.showerror("Error", "Failed to capture image from camera")
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def start_face_recognition(self):
        self.face_recognition_running = True
        self.face_recognition_thread = threading.Thread(target=self.face_recog)
        self.face_recognition_thread.start()

    def stop_face_recognition(self):
        self.face_recognition_running = False
        if self.face_recognition_thread and self.face_recognition_thread.is_alive():
            self.face_recognition_thread.join()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.stop_face_recognition()
            self.root.destroy()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
