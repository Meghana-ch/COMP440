from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import tkinter as tk
import pymysql


def login_page():
    signup.destroy()
    import signin


def clear():
    emailEntry.delete(0, END)
    firstEntry.delete(0, END)
    lastEntry.delete(0, END)
    passwordEntry.delete(0, END)
    ConfirmPasswordEntry.delete(0, END)
    userEntry.delete(0, END)


def check_error():
    if firstEntry.get() == '' or lastEntry.get() == '' or emailEntry.get() == '' or userEntry.get() == '' or passwordEntry.get() == '' or ConfirmPasswordEntry.get() == '':
        messagebox.showerror('ERROR', 'All fields are Required')
    elif passwordEntry.get() != ConfirmPasswordEntry.get():
        messagebox.showerror('ERROR', 'Password Mismatch')
    else:
        return True


def connect_db():
    check_error()
    if check_error():
        try:
            con = pymysql.connect(host='localhost', port=3306, user='root', password='Honey@2323', database='proj1_db')
            mycursor = con.cursor()
        except:
            messagebox.showerror('ERROR', 'Database Connectivity Issue, please try again!')
            return

        query = 'use proj1_db'
        mycursor.execute(query)
        query = 'select * from user where Username=%s'
        mycursor.execute(query, (userEntry.get()))
        username = mycursor.fetchone()
        query = 'select * from user where Email=%s'
        mycursor.execute(query, (emailEntry.get()))
        email = mycursor.fetchone()
        if email is not None:
            messagebox.showerror('ERROR', 'Duplicate Entry. Email is already registered')
        elif username is not None:
            messagebox.showerror('ERROR', 'Username already exists.')
        else:
            query = 'insert into proj1_db.user(Username, Password, `First Name`, `Last Name`, Email) values(%s, %s, %s, %s, %s)'
            mycursor.execute(query, (
            userEntry.get(), passwordEntry.get(), firstEntry.get(), lastEntry.get(), emailEntry.get()))
            con.commit()
            messagebox.showinfo('SUCCESS!', 'Registration successful!\nPlease Login')
            con.close()
            clear()
            signup.destroy()
            import signin


# Window Setup
signup = Tk()
signup.title('Signup Page')
signup.resizable(False, False)

# Background setup
background = ImageTk.PhotoImage(file='img/bg.jpg')
bgLabel = Label(signup, image=background)
bgLabel.grid()

# Heading
frame = Frame(signup, bg='white')
frame.place(x=554, y=100)
heading = Label(signup, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 25, 'bold'), bg='white', fg='navy')
heading.place(x=565, y=62)

# First Name
firstLabel = Label(frame, text='First Name', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white', fg='firebrick2')
firstLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(5, 0))
firstEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13, 'bold'), bg='light pink', fg='white')
firstEntry.grid(row=2, column=0, sticky='w', padx=25)

# Last Name
lastLabel = Label(frame, text='Last Name', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white', fg='firebrick2')
lastLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(5, 0))
lastEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13, 'bold'), bg='light pink', fg='white')
lastEntry.grid(row=4, column=0, sticky='w', padx=25)

# Email entry
emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white', fg='firebrick2')
emailLabel.grid(row=5, column=0, sticky='w', padx=25)
emailEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13, 'bold'), bg='light pink', fg='white')
emailEntry.grid(row=6, column=0, sticky='w', padx=25)

# Username Entry
userLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white', fg='firebrick2')
userLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(5, 0))
userEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13, 'bold'), bg='light pink', fg='white')
userEntry.grid(row=8, column=0, sticky='w', padx=25)

# Password Entry
passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white',
                      fg='firebrick2')
passwordLabel.grid(row=9, column=0, sticky='w', padx=25, pady=(5, 0))
passwordEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13, 'bold'), bg='light pink', fg='white')
passwordEntry.grid(row=10, column=0, sticky='w', padx=25)

# Confirm Password Entry
ConfirmPasswordLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white',
                             fg='firebrick2')
ConfirmPasswordLabel.grid(row=11, column=0, sticky='w', padx=25, pady=(5, 0))
ConfirmPasswordEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13, 'bold'), bg='light pink',
                             fg='white')
ConfirmPasswordEntry.grid(row=12, column=0, sticky='w', padx=25)

# signup button
signupButton = tk.Button(frame, text='SIGNUP', font=('Open Sans', 17, 'bold'), bg='hot pink',
                         activebackground='hot pink', foreground='firebrick2',
                         activeforeground='firebrick3', highlightthickness=2, highlightcolor='firebrick2',
                         highlightbackground='firebrick2',
                         border=2, width=17, height=1, command=connect_db)
signupButton.grid(row=14, column=0, pady=13)

# Login option
loginLabel = Label(frame, text='Already have an account?', font=('Open Sans', 12, 'bold'), fg='firebrick1', bg='white')
loginLabel.grid(row=15, column=0)
loginButton = Button(frame, text='Login Here', font=('Open Sans', 12, 'bold underline'), background='white',
                     fg='blue', highlightthickness=0, highlightcolor='plum', highlightbackground='white',
                     bd=0, command=login_page)
loginButton.grid(row=16, column=0)

signup.mainloop()
