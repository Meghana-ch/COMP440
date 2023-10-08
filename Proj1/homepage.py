from tkinter import *
from PIL import ImageTk

# GUI
home = Tk()
home.geometry('1081x772+20+20')  # place the window in the comp screen
home.resizable(False, False)  # disable the full screen option for window
home.title('Home Page')  # Title of the window

# Background image setting
bgImage = ImageTk.PhotoImage(file='Attendance2.jpg')
bgLabel = Label(home, image=bgImage)
bgLabel.place(x=0, y=0)

# Placing a header
heading = Label(home, text='ATTENDANCE TRACKER', font=('Microsoft Yahei UI Light', 30, 'bold'), bg='white', fg='navy')
heading.place(x=720, y=80)

home.mainloop()
