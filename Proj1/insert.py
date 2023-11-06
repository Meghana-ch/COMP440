from tkinter import *
import pymysql
from PIL import ImageTk
from tkinter import messagebox

# Functionality
def back():
    insert_data.destroy()
    import home

def user_enter(event):
    if UsernameEntry.get() == 'Username':
        UsernameEntry.delete(0, END)

def title_enter(event):
    if TitleEntry.get() == 'Title':
        TitleEntry.delete(0, END)

def desc_enter(event):
    if DescEntry.get() == 'Description':
        DescEntry.delete(0, END)

def category():
    if variable.get() != 'Default':
        variable.set('Default')

def price_enter(event):
    if PriceEntry.get() == 'Price':
        PriceEntry.delete(0, END)

def clear():
    TitleEntry.delete(0, END)
    DescEntry.delete(0, END)
    variable.set('Default')
    PriceEntry.delete(0, END)

def check_error():
    if TitleEntry.get() == '' or DescEntry.get() == '' or variable.get() == '' or PriceEntry.get() == '':
        messagebox.showerror('ERROR', 'All fields are Required')
    # elif passwordEntry.get() != ConfirmPasswordEntry.get():
    #     messagebox.showerror('ERROR', 'Password Mismatch')
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
        query = 'SELECT COUNT(*) FROM product WHERE Username=%s AND Entry_Date=CURDATE()'
        mycursor.execute(query, UsernameEntry.get())
        user_count = mycursor.fetchone()
        if user_count[0] > 2:
            messagebox.showerror('ERROR', 'Already entered 3 times. Try after a day.')
        else:
            query = 'insert into proj1_db.product(Title, Description, Category, Price, Username, Entry_Date) values(%s, %s, %s, %s, %s, curdate())'
            mycursor.execute(query,
                             (TitleEntry.get(), DescEntry.get(), variable.get(), PriceEntry.get(), UsernameEntry.get()))
            con.commit()
            messagebox.showinfo('SUCCESS!', 'Data Logged!' + UsernameEntry.get())
            con.close()
            clear()


# GUI
insert_data = Tk()
insert_data.geometry('990x660+20+20')  # place the window in the comp screen
insert_data.resizable(False, False)  # disable the full screen option for window
insert_data.title('Insert Page')  # Title of the window

# Background image setting
bgImage = ImageTk.PhotoImage(file='img/db_bg.png')
bgLabel = Label(insert_data, image=bgImage)
bgLabel.place(x=0, y=0)

# Create a white rectangle
formbg = ImageTk.PhotoImage(file='img/rectangle.png')
formLabel = Label(insert_data, image=formbg)
formLabel.place(x=120, y=55)

# Create a heading
heading = Label(insert_data, text='Insert details\nof your Product', font=('Microsoft Yahei UI Light', 40, 'bold'),
                bg='cyan4', fg='white')
heading.place(x=630, y=270)

# Entry for Title
TitleHeading = Label(insert_data, text='Enter Title of Product:', font=('Microsoft Yahei UI Light', 17),
                     bg='white', fg='cyan4')
TitleHeading.place(x=140, y=80)
TitleEntry = Entry(insert_data, width=20, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='Cyan', bg='white',
                   highlightthickness=0)
TitleEntry.place(x=142, y=110)
TitleEntry.insert(0, 'Title')
TitleEntry.bind('<FocusIn>', title_enter)
frame1 = Frame(insert_data, width=200, height=3, bg='cyan4')
frame1.place(x=142, y=130)

# Entry for Description
DescHeading = Label(insert_data, text='Enter Description of Product:', font=('Microsoft Yahei UI Light', 17),
                    bg='white', fg='cyan4')
DescHeading.place(x=140, y=180)
DescEntry = Entry(insert_data, width=35, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='Cyan', bg='white',
                  highlightthickness=0)
DescEntry.place(x=142, y=210)
DescEntry.insert(0, 'Description')
DescEntry.bind('<FocusIn>', desc_enter)
frame2 = Frame(insert_data, width=400, height=3, bg='cyan4')
frame2.place(x=142, y=230)

# Entry for Category
CatHeading = Label(insert_data, text='Select Category of Product:', font=('Microsoft Yahei UI Light', 17),
                   bg='white', fg='cyan4')
CatHeading.place(x=140, y=280)
variable = StringVar(insert_data)
variable.set("Default")  # default value
CatEntry = OptionMenu(insert_data, variable, "Default", "Mobile", "Laptop", "Desktop", "Ipad")
CatEntry.config(bg='powder blue', fg='cyan4', width=15)
CatEntry.pack()
CatEntry.place(x=142, y=310)
button = Button(insert_data, text="OK", command=category, background='powder blue', foreground='cyan4',
                highlightthickness=0,
                highlightcolor='cyan4', highlightbackground='cyan4', border=0)
button.pack()
button.place(x=340, y=310)

# Entry for Price
PriceHeading = Label(insert_data, text='Enter Price of Product:', font=('Microsoft Yahei UI Light', 17), bg='white',
                     fg='cyan4')
PriceHeading.place(x=140, y=370)
PriceEntry = Entry(insert_data, width=35, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='Cyan', bg='white',
                   highlightthickness=0)
PriceEntry.place(x=142, y=400)
PriceEntry.insert(0, 'Price')
PriceEntry.bind('<FocusIn>', price_enter)
frame3 = Frame(insert_data, width=120, height=3, bg='cyan4')
frame3.place(x=142, y=420)

# Entry for Username
UsernameHeading = Label(insert_data, text='Enter your username:', font=('Microsoft Yahei UI Light', 17), bg='white',
                        fg='cyan4')
UsernameHeading.place(x=140, y=470)
UsernameEntry = Entry(insert_data, width=35, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='Cyan', bg='white',
                      highlightthickness=0)
UsernameEntry.place(x=142, y=500)
UsernameEntry.insert(0, 'Username')
UsernameEntry.bind('<FocusIn>', user_enter)
frame4 = Frame(insert_data, width=200, height=3, bg='cyan4')
frame4.place(x=142, y=520)

# Insert button
InsertButton = Button(insert_data, text='INSERT', font=('Open Sans', 17, 'bold'), bg='cyan3', activebackground='cyan',
                      foreground='cyan4', activeforeground='cyan4', highlightthickness=2,
                      highlightcolor='cyan4', highlightbackground='cyan4', border=2, width=17, height=1,
                      command=connect_db)
InsertButton.place(x=230, y=555)

# Back Button
back_button = Button(insert_data, text='Back to Main Menu', font=('Open Sans', 10, 'bold'), bg='cyan3',
                     activebackground='cyan', foreground='cyan4', activeforeground='cyan4', highlightthickness=2,
                     highlightcolor='cyan4', highlightbackground='cyan4', border=2, width=12, height=1,
                     command=back)
back_button.place(x=10, y=10)

insert_data.mainloop()
