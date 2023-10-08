from tkinter import *
from PIL import ImageTk
import tkinter as tk
import pymysql
from tkinter import messagebox

# Functionality
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)
        passwordEntry.config(show='*')

def hide():
    closeeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=show)

def show():
    closeeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=hide)

def signup_page():
    login.destroy()
    import signup

def clear():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('ERROR', 'All fields are Required.')
    else:
        try:
            con = pymysql.connect(host='localhost', port=3306,  user='root', password='Honey@2323', database='proj1_db')
            mycursor = con.cursor()
        except:
            messagebox.showerror('ERROR', 'Database Connectivity Issue, please try again!')
            return

        query = 'use proj1_db'
        mycursor.execute(query)
        query = 'select * from user where Username=%s and Password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row is None:
            messagebox.showerror('ERROR', 'Invalid Username or Password')
        else:
            messagebox.showinfo('WELCOME', 'Login is Successful!')
            clear()
            con.close()
            login.destroy()
            import homepage

# GUI
login = Tk()
login.geometry('990x660+20+20')  # place the window in the comp screen
login.resizable(False, False)  # disable the full screen option for window
login.title('Login Page')  # Title of the window

# Background image setting
bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(login, image=bgImage)
bgLabel.grid(row=0, column=0)

# Placing a header
heading = Label(login, text='USER LOGIN', font=('Microsoft Yahei UI Light', 30, 'bold'), bg='white', fg='navy')
heading.place(x=610, y=120)

# username Entry Fields
usernameEntry = Entry(login, width=20, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='firebrick2', bg='white',
                      highlightthickness=0)
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)
frame1 = Frame(login, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=220)

# password Entry Fields
passwordEntry = Entry(login, width=20, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='firebrick2', bg='white',
                      highlightthickness=0)
passwordEntry.place(x=580, y=250)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)
frame2 = Frame(login, width=250, height=2, bg='firebrick1')
frame2.place(x=580, y=270)
# eye button
closeeye = PhotoImage(file='closeye.png')
eyeButton = Button(login, image=closeeye, bd=0, highlightthickness=0, activebackground='white', cursor='hand2',
                   command=hide)
eyeButton.place(x=800, y=243)

forgetButton = tk.Button(login, text='Forgot Password?', font=('Open Sans', 13), background='white',
                         foreground='firebrick2',
                         highlightthickness=0, highlightcolor='plum', highlightbackground='white', border=0)
forgetButton.place(x=700, y=275)

loginButton = tk.Button(login, text='LOGIN', font=('Open Sans', 17, 'bold'), background='grey', foreground='firebrick2',
                        activeforeground='firebrick3',
                        highlightthickness=2, highlightcolor='firebrick1', highlightbackground='plum', border=2,
                        width=17, height=2, command=login_user)
loginButton.place(x=585, y=325)

orLabel = Label(login, text='------------------ OR ------------------', font=('Open Sans', 15), fg='firebrick1',
                bg='white')
orLabel.place(x=563, y=380)

fblogo = PhotoImage(file='facebook.png')
fbLabel = Label(login, image=fblogo, bg='white')
fbLabel.place(x=620, y=420)

googlelogo = PhotoImage(file='google.png')
googleLabel = Label(login, image=googlelogo, bg='white')
googleLabel.place(x=690, y=420)

twitterlogo = PhotoImage(file='twitter.png')
twitterLabel = Label(login, image=twitterlogo, bg='white')
twitterLabel.place(x=760, y=420)

signupLabel = Label(login, text='Dont have an account?', font=('Open Sans', 13, 'bold'), fg='firebrick1', bg='white')
signupLabel.place(x=555, y=500)

new_accButton = tk.Button(login, text='Create New One', font=('Open Sans', 13, 'bold'), background='white',
                          foreground='blue', highlightthickness=0, highlightcolor='plum', highlightbackground='white',
                          border=0, command=signup_page)
new_accButton.place(x=705, y=500)

login.mainloop()
