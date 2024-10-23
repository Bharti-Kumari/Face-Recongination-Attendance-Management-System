from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class HelpDesk:
    def __init__(self, root):
        self.root = root
        self.root.title("Help Desk")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>', self.enter_func)

        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)
        main_frame.pack()
        img_chat = Image.open(r"C:\Users\Bharti Soni\Desktop\Attendance management system\college_images\chatbot.jpg")
        img_chat = img_chat.resize((200, 70))
        self.photoimg = ImageTk.PhotoImage(img_chat)
        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, compound=LEFT, image=self.photoimg, text='CHAT ME', font=('arial', 30, 'bold'), fg='Navy', bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('arial', 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        label1 = Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'), fg='Navy', bg='white')
        label1.grid(row=0, column=0, padx=5, sticky=W)
        
        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=('times new roman', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)
        self.send = Button(btn_frame, text="Send >>", command=self.send, font=('times new roman', 15, 'bold'), width=8, bg='Navy', fg='white')
        self.send.grid(row=0, column=2, padx=5, sticky=W)
        self.clear = Button(btn_frame, text="Clear Data", command=self.clear, font=('times new roman', 15, 'bold'), width=8, bg='#6fb0fc', fg='white')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label2 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='Navy', bg='white')
        self.label2.grid(row=1, column=1, padx=5, sticky=W)

    ################################# Function Declaration ###############################

    def enter_func(self, event):
        self.send.invoke()

    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')

    def send(self):
        user_input = self.entry.get().strip().lower()
        send = '\t\t\t' + 'You: ' + self.entry.get()
        self.text.insert(END, '\n' + send)
        self.text.yview(END)

        if user_input == '':
            self.msg = 'Please enter some input'
            self.label2.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label2.config(text=self.msg, fg='red')
            self.respond(user_input)

    def respond(self, user_input):
        responses = {
            'hello': 'Hi!',
            'hi': 'Hello!',
            'how are you?': 'I\'m fine, thank you! How can I assist you?',
            'who created you': 'I was created by Bharti Kumari.',
            'what is face recognition?': 'Face recognition is a technology that identifies or verifies a person from a digital image or a video frame.',
            'why is my face not being recognized?': 'Ensure that your face is clearly visible and that there is sufficient lighting. Also, make sure your face data is registered in the system.',
            'how to register my face?': 'To register your face, go to the registration section of the application, and follow the instructions to capture your face data.',
            'what to do if the system marks the wrong person?': 'This could be due to a close resemblance to another person in the database. Try re-registering with a clearer image.',
            'how to reset the system?': 'You can reset the system by restarting the application. If the issue persists, contact technical support.',
            'how to update my face data?': 'You can update your face data by going to the update section in the application and following the instructions.',
            'can the system recognize multiple faces at once?': 'Yes, the system is designed to recognize multiple faces, but it marks attendance for one person at a time to avoid confusion.',
            'how to improve face recognition accuracy?': 'Ensure good lighting, avoid obstructions, and keep your face data updated with multiple images.',
            'what if my face changes over time?': 'It\'s recommended to update your face data regularly, especially if there are significant changes in your appearance.',
            'can the system work in low light?': 'Low light can affect accuracy. It\'s best to use the system in well-lit environments.',
            'what camera resolution is needed for best results?': 'A camera with at least 720p resolution is recommended for better face recognition accuracy.',
            'how does the system handle face masks?': 'Face masks can reduce accuracy. For better results, use the system without a mask or register your face with a mask if required.',
            'can the system detect emotions?': 'The system is primarily designed for identification and not emotion detection.',
            'is the system secure?': 'Yes, the system uses secure methods to store and process face data.',
            'can I delete my face data?': 'Yes, you can delete your face data through the user settings in the application.',
            'how often should I update my face data?': 'It\'s recommended to update your face data every 6-12 months or whenever there\'s a significant change in your appearance.',
            'what happens if my face is not recognized?': 'If your face is not recognized, try again in better lighting or ensure your face is properly aligned with the camera.',
            'can multiple people register the same face?': 'No, each face is unique to the user. If there are similarities, it could lead to misidentification.',
            'what if the system crashes during face recognition?': 'Restart the application and try again. Ensure your system meets the necessary hardware requirements.',
            'can the system work outdoors?': 'The system can work outdoors but may struggle with extreme lighting conditions. It\'s best used in controlled environments.',
            'what if the system is slow?': 'Slow performance may be due to insufficient system resources. Check your system requirements and close unnecessary applications.',
            'can I use this system on multiple devices?': 'Yes, the system can be used on multiple devices, but each device should have the necessary software installed.',
            'how do I troubleshoot connection issues?': 'Ensure your device is connected to the network and check your internet connection. Restart the application if necessary.',
            'what are the best practices for face recognition?': 'Use a consistent background, avoid strong backlighting, and keep the camera at eye level.',
            'how is my data protected?': 'Your data is encrypted and stored securely, with access limited to authorized personnel.',
            'can the system recognize faces in a group photo?': 'Yes, but it’s best to focus on one person at a time for accurate recognition and attendance marking.',
            'how do I update the system?': 'Check for updates in the application settings or visit the official website for the latest version.',
            'how do I contact support?': 'You can contact support through the application’s help section or via the official website.',
            'what do I do if the application freezes?': 'Force close the application and restart it. If the issue persists, check for updates or reinstall the application.',
            'can I use the system without an internet connection?': 'Basic functions may work offline, but some features, like data synchronization, require an internet connection.',
            'how do I export attendance records?': 'You can export attendance records through the application’s settings or data management section.',
            'what file format is used for attendance records?': 'Attendance records are typically saved in CSV format, which can be opened with spreadsheet software.',
            'can I customize the system’s interface?': 'Some elements may be customizable through the application’s settings, depending on the version you’re using.',
            'how do I integrate the system with other software?': 'Check the documentation or contact support for integration options with other software.',
            'can the system be used in multiple languages?': 'Yes, language options may be available in the settings. Contact support if your language is not listed.',
            'what if the system detects a face incorrectly?': 'Re-register your face with better images, and ensure no one else has similar features in the database.',
            'can the system recognize faces in a video?': 'Yes, the system can recognize faces in real-time video streams as well as in recorded videos.',
            'what happens if the camera is blocked?': 'If the camera is blocked, the system won’t be able to capture your face. Ensure the camera lens is clean and unobstructed.',
            'how do I switch between cameras?': 'If you have multiple cameras, you can select the desired camera in the application’s settings.',
            'what are the recommended system requirements?': 'A computer with at least 4GB RAM, a dual-core processor, and a camera with 720p resolution or higher is recommended.',
            'how do I enable/disable face recognition?': 'You can enable or disable face recognition in the application’s settings under the security or privacy section.',
            'what should I do if the system cannot detect my face at all?': 'Ensure the camera is working properly, the environment is well-lit, and your face is within the camera’s field of view.',
            'can I use this system for security purposes?': 'Yes, the system can be used for security, but it’s primarily designed for attendance management.',
            'how do I change the camera resolution?': 'Camera resolution settings can usually be adjusted in the camera software or within the application’s settings if supported.',
            'is there a user manual available?': 'Yes, a user manual can typically be found within the application or on the official website.',
        }

        bot_response = responses.get(user_input, 'I did not get that. Could you please rephrase?')
        self.text.insert(END, '\n\n' + 'Bot: ' + bot_response)

if __name__ == "__main__":
    root = Tk()
    obj = HelpDesk(root)
    root.mainloop()
