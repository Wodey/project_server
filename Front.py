import tkinter as tk
from tkinter import *
import sqlite3


con = sqlite3.connect("testdatabase.db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users
                   (name TEXT, score INT)''')

con.commit()


class MainApplication:

    win = tk.Tk()

    def __init__(self):
        def FrontPage():
            def AdminPagePassword():
                def AdminPage():

                    self.ReturnButton.destroy()

                    self.content.destroy()

                    self.Admin.destroy()

                    self.content = Frame(self.wrapper, bg='white')

                    self.ExerciseText = Text(self.content, width = 60, height = 10, borderwidth = 2, relief="solid", font = ('Arial',20))

                    self.content.pack(expand=1, ipady=100)
                    self.ExerciseText.grid(column = 0, row = 1)


                self.content.destroy()

                self.Admin.destroy()

                def Return():
                    self.wrapper.destroy()
                    self.JustADecoration.destroy()
                    FrontPage()

                self.content = Frame(self.wrapper, bg='white')

                self.ReturnButton = Button(self.wrapper, bg='#fff', text='<< Return', font=('Times New Roman', 24), borderwidth=0, command = Return)

                self.PasswordLabel = Label(self.content, bg='white', text='Are you sure you are an admin?',
                                        font=('Times New Roman', 36))

                self.password = Entry(self.content, borderwidth=2, relief="solid", width='40', justify='center',
                                   font=('Arial', 23), bg='white', fg='#000')

                self.submit = Button(self.content, borderwidth=2, relief="solid", width=20, height=1,
                                     font=('Times New Roman', 16), text='Submit', bg='white', command=AdminPage)

                self.ReturnButton.pack(anchor = NW, padx = 80, pady = 60)
                self.content.pack(expand=1, ipady=100)
                self.PasswordLabel.grid(column=0, row=1, columnspan=2, pady=100)
                self.password.grid(column=0, row=2, padx=5)
                self.submit.grid(column=1, row=2, padx=5)


            def ExercisePge():
                def LeaderTAble():

                    self.content.destroy()

                    self.Admin.destroy()


                    self.content = Frame(self.wrapper, width = 500, height = 600, bg='white', borderwidth = 2, relief="solid")

                    self.content.pack(expand = 1)



                self.content.destroy()

                self.Admin.destroy()


                self.content = Frame(self.wrapper, bg = '#fff')
                self.content.grid_columnconfigure(0, weight=1)
                self.content.grid_columnconfigure(1, weight=1)
                self.content.grid_rowconfigure(2, weight = 1)


                for val in cur.execute("SELECT * FROM users"):
                    name = val[0]

                univweidth = 300

                self.BigLabel = Label(self.content, text='Contest', font=('Times New Roman', 36), bg = '#fff')

                self.xrslabel = Label(self.content, text = 'Exercise', font = ('Times New Roman', 24), bg = '#fff')

                self.Exercise = Label(self.content, width = univweidth, text = name + '(Its just to test)\nmmm\nmmmmm\nnnnnnnn\nnnnnnn\nnnnn', font = ('Times New Roman', 20), bg = 'white', borderwidth = 2, relief="solid")

                self.anslabel = Label(self.content, text = 'Put your answer', font=('Times New Roman', 24), bg = '#fff')

                self.answerinp = Text(self.content, width = univweidth, height = 5, borderwidth = 2, relief="solid", font = ('Arial',20))

                self.NextButton = Button(self.content, borderwidth = 2, relief="solid", height = 2, font = ('Times New Roman', 16), text = 'Next', bg = 'white', command = LeaderTAble)

                self.HintButton = Button(self.content, borderwidth=2, relief="solid", height=2, font = ('Times New Roman', 16), text='Take a hint', bg='white')

                self.content.pack(expand = 1, fill = BOTH, padx = 60, pady = (0, 60))
                self.BigLabel.grid(column=0, row=0, columnspan = 2, pady = 40, sticky="WE")
                self.xrslabel.grid(column=0, row=1, sticky="NSEW", padx = 20, pady = 20)
                self.anslabel.grid(column=1, row=1, sticky="NSEW", padx = 20, pady = 20)
                self.Exercise.grid(column = 0, row = 2, padx = 20, pady = 40, sticky="NSEW")
                self.answerinp.grid(column = 1, row = 2, padx = 20, pady = 40, sticky="NSEW")
                self.NextButton.grid(column = 1, row = 3, padx = 20, pady = 20, sticky = 'WE')
                self.HintButton.grid(column = 0, row = 3, padx = 20, pady = 20, sticky = 'WE')


            def removeplaceholder(event):
                self.login.delete(0, 'end')
                self.login.configure(fg = 'black')


            def submit():
                value = self.login.get()
                cur.execute("INSERT INTO users VALUES (?, ?)", (value, 0))
                if value and value != 'You...':
                    ExercisePge()


            self.root = MainApplication.win
            self.root.iconbitmap('icon.ico')
            self.root.title('TheApp')
            self.root.geometry(f"1080x720+300+200")

            self.JustADecoration = Frame(self.root, width = 2000, height = 2, bg = 'black')

            self.wrapper = Frame(self.root, bg = 'white')

            self.content = Frame(self.wrapper, bg = 'white', )

            self.FrontLabel = Label(self.content, bg = 'white', text = 'This is the story about', font = ('Times New Roman', 36))

            self.login = Entry(self.content, borderwidth = 2, relief="solid", width='40', justify = 'center',  font = ('Arial',23), bg = 'white', fg = '#ddd')
            self.login.insert(0, 'You...')
            self.login.bind("<FocusIn>", removeplaceholder)

            self.submit = Button(self.content, borderwidth = 2, relief="solid", width = 20, height = 1, font = ('Times New Roman', 16), text = 'Submit', bg = 'white', command=submit)

            self.Admin = Button(self.wrapper, bg = '#fff', text = 'I am an admin', font = ('Times New Roman', 18, 'underline'),  borderwidth = 0, command = AdminPagePassword)

            self.JustADecoration.pack()
            self.wrapper.pack(expand = 1, fill = BOTH)
            self.content.pack(expand=1, ipady=100)
            self.FrontLabel.grid(column = 0, row = 0, columnspan = 2, pady = 100)
            self.login.grid(column = 0, row = 1, padx = 5)
            self.submit.grid(column = 1, row = 1, padx = 5)
            self.Admin.pack(anchor = N, pady = 40)

        FrontPage()

    def start(self):
        MainApplication.win.mainloop()


app = MainApplication()
app.start()