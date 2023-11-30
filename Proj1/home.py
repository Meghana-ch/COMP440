from tkinter import *
from PIL import ImageTk


# Functionality
def phase3_page():
    home.destroy()
    import phase3

def insert_page():
    home.destroy()
    import insert

def search_page():
    home.destroy()
    import search


def gen_page():
    home.destroy()
    import Gen


# GUI
home = Tk()
home.geometry('990x660+20+20')  # place the window in the comp screen
home.resizable(False, False)  # disable the full screen option for window
home.title('Home Page')  # Title of the window

# Background image setting
bgImage = ImageTk.PhotoImage(file='img/db_bg.png')
bgLabel = Label(home, image=bgImage)
bgLabel.place(x=0, y=0)

# Create a heading
heading = Label(home, text='PICK AN OPTION', font=('Microsoft Yahei UI Light', 30, 'bold'), bg='aquamarine2', fg='navy')
heading.place(x=365, y=130)

# Insert button
InsertButton = Button(home, text='Insert Data', font=('Open Sans', 20, 'bold'), bg='cyan3', activebackground='cyan',
                      foreground='cyan4', activeforeground='cyan4', highlightthickness=2,
                      highlightcolor='cyan4', highlightbackground='cyan4', border=2, width=17, height=1,
                      command=insert_page)
InsertButton.place(x=350, y=250)

# Search Button
SearchButton = Button(home, text='Search Data', font=('Open Sans', 20, 'bold'), bg='cyan3', activebackground='cyan',
                      foreground='cyan4', activeforeground='cyan4', highlightthickness=2,
                      highlightcolor='cyan4', highlightbackground='cyan4', border=2, width=17, height=1,
                      command=search_page)
SearchButton.place(x=350, y=350)

# Generate Button
GenButton = Button(home, text='Initialize Database', font=('Open Sans', 20, 'bold'), bg='cyan3',
                   activebackground='cyan',
                   foreground='cyan4', activeforeground='cyan4', highlightthickness=2, highlightcolor='cyan4',
                   highlightbackground='cyan4', border=2, width=17, height=1, command=gen_page)
GenButton.place(x=350, y=450)

# Phase3
# Generate Button
Phase3Button = Button(home, text='Phase 3 Options', font=('Open Sans', 20, 'bold'), bg='cyan3', activebackground='cyan',
                      foreground='cyan4', activeforeground='cyan4', highlightthickness=2, highlightcolor='cyan4',
                      highlightbackground='cyan4', border=2, width=17, height=1, command=phase3_page)
Phase3Button.place(x=350, y=550)
home.mainloop()
