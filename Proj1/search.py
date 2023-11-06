from tkinter import *
import pymysql
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox


def back():
    app_search.destroy()
    import home

def clear():
    rating_var.set('Default')
    review_text_entry.delete(0, END)
    UsernameEntry.delete(0, END)
    IDEntry.delete(0, END)

def rating_enter(event):
    if rating_var.get() != 'Default':
        variable.set('Default')

def ID_Entry(event):
    if IDEntry.get() == 'ID number':
        IDEntry.delete(0, END)

def User_Entry(event):
    if UsernameEntry.get() == 'Username':
        UsernameEntry.delete(0, END)

def review_enter(event):
    if review_text_entry.get() == 'Review':
        review_text_entry.delete(0, END)

def on_select_item(event):
    global selected_item
    selected_item = tree.item(tree.selection())['values']

def check_error():
    if review_text_entry.get() == '' or rating_var.get() == 'Default' or UsernameEntry.get() == '' or IDEntry.get() == '':
        messagebox.showerror('ERROR', 'All fields are Required')
    else:
        return True

def write_review():
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
        query = 'SELECT COUNT(*) FROM review WHERE User=%s AND Entry_Date=CURDATE()'
        mycursor.execute(query, UsernameEntry.get())
        count = mycursor.fetchone()
        if count[0] > 2:
            messagebox.showerror('ERROR', 'ERROR!\nYour limit for reviewing has reached. Please try tomorrow!')
        else:
            query = 'SELECT Title FROM product WHERE Product_ID=%s'
            mycursor.execute(query, IDEntry.get())
            Product_name = mycursor.fetchone()
            query = 'SELECT Category FROM product WHERE Product_ID=%s'
            mycursor.execute(query, IDEntry.get())
            Category = mycursor.fetchone()
            query = 'SELECT Price FROM product WHERE Product_ID=%s'
            mycursor.execute(query, IDEntry.get())
            Price = mycursor.fetchone()
            query = 'insert into proj1_db.review(Product_Name, Category, Price, Rating, Review, User, Entry_Date) values(%s, %s, %s, %s, %s, %s, curdate())'
            mycursor.execute(query,
                             (Product_name, Category, Price, rating_var.get(), review_text_entry.get(),
                              UsernameEntry.get()))
            con.commit()
            messagebox.showinfo('SUCCESS!', 'Review Logged!')
            con.close()
            clear()


def search_items():
    global rating_var
    global review_text_entry
    global tree
    global IDEntry
    global UsernameEntry
    # Retrieve the category from the user input
    category = variable.get()

    # Perform a SQL query to retrieve items with the given category
    con = pymysql.connect(host='localhost', port=3306, user='root', password='Honey@2323', database='proj1_db')
    cursor = con.cursor()
    query = 'SELECT * FROM product WHERE Category = %s'
    cursor.execute(query, category)
    items = cursor.fetchall()

    style = ttk.Style()
    style.configure("Treeview",
                    background="powder blue",  # Set the background color
                    fieldbackground="powder blue",
                    borderwidth=2,  # Set the border width
                    relief="solid"  # Set the border style to solid
                    )
    style.configure("Treeview.Heading",  # Set text color for headings
                    foreground="black",  # Set the text color to black
                    font=('Helvetica', 14, 'bold', 'underline')
                    )
    style.configure("Treeview.Cell",
                    foreground="black"  # Set the text color for cell content to black
                    )
    columns = ('ID', 'Title', 'Description', 'Category', 'Price')
    tree = ttk.Treeview(app_search, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='center')

    # Insert the retrieved items into the table
    for item in items:
        tree.insert("", "end", values=item, tags=('black_text',))

    tree.tag_configure('black_text', foreground='black')

    tree.place(x=235, y=90)
    # Display the search results in a new window or a table
    tree.bind('<<TreeviewSelect>>', on_select_item)  # Bind the selection event

    # Entry for ID
    IDHeading = Label(app_search, text='Enter the ID of product:', font=('Microsoft Yahei UI Light', 15), bg='white',
                      fg='cyan4')
    IDHeading.place(x=145, y=330)
    IDEntry = Entry(app_search, width=35, font=('Microsoft Yahei UI Light', 20), bd=1, fg='white',
                    bg='cyan4', highlightthickness=1)
    IDEntry.place(x=325, y=330)
    IDEntry.insert(0, 'ID number')
    IDEntry.bind('<FocusIn>', ID_Entry)

    # Entry for Username
    UsernameHeading = Label(app_search, text='Enter your username:', font=('Microsoft Yahei UI Light', 17), bg='white',
                            fg='cyan4')
    UsernameHeading.place(x=145, y=380)
    UsernameEntry = Entry(app_search, width=35, font=('Microsoft Yahei UI Light', 20), bd=1, fg='white',
                          bg='cyan4', highlightthickness=1)
    UsernameEntry.place(x=325, y=380)
    UsernameEntry.insert(0, 'Username')
    UsernameEntry.bind('<FocusIn>', User_Entry)

    # rating
    rating_var = StringVar()
    rating_label = Label(app_search, text="Rating:", font=('Microsoft Yahei UI Light', 17), bg="white",
                         fg="cyan4")
    rating_label.place(x=250, y=430)
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="cyan4", background="white")
    rating_entry = ttk.Combobox(app_search, textvariable=rating_var, values=["excellent", "good", "fair", "poor"],
                                background="cyan4", font=('Microsoft Yahei UI Light', 19))

    rating_entry.place(x=325, y=430)
    rating_entry.insert(0, 'Default')
    rating_entry.bind('<FocusIn>', rating_enter)
    review_text_label = Label(app_search, text="Review:", font=('Microsoft Yahei UI Light', 17), bg="white",
                              fg="cyan4")
    review_text_label.place(x=245, y=480)
    review_text_entry = Entry(app_search, width=35, font=('Microsoft Yahei UI Light', 19), bd=1, fg='white',
                              bg='cyan4', highlightthickness=1)
    review_text_entry.place(x=325, y=480)
    review_text_entry.insert(0, 'Review')
    review_text_entry.bind('<FocusIn>', review_enter)

    write_review_button = Button(app_search, text='Write Review', font=('Open Sans', 17, 'bold'), bg='cyan3',
                                 activebackground='cyan', foreground='cyan4', activeforeground='cyan4',
                                 highlightthickness=2, highlightcolor='cyan4', highlightbackground='cyan4', border=2,
                                 width=10, height=1, command=write_review)
    write_review_button.place(x=400, y=530)


app_search = Tk()
app_search.geometry('990x660+20+20')  # place the window in the comp screen
app_search.resizable(False, False)  # disable the full screen option for window
app_search.title('Search Page')  # Title of the window

# Background image setting
bgImage = ImageTk.PhotoImage(file='img/db_bg.png')
bgLabel = Label(app_search, image=bgImage)
bgLabel.place(x=0, y=0)

# Entry for Category
CatHeading = Label(app_search, text='Select Category', font=('Microsoft Yahei UI Light', 17),
                   bg='white', fg='cyan4')
CatHeading.place(x=425, y=12)
variable = StringVar(app_search)
variable.set("Default")  # default value
CatEntry = OptionMenu(app_search, variable, "Mobile", "Laptop", "Desktop", "Ipad")
CatEntry.config(bg='cyan4', fg='white', width=15)
CatEntry.place(x=400, y=40)
button = Button(app_search, text="OK", command=search_items, background='powder blue', foreground='cyan4',
                highlightthickness=0, highlightcolor='cyan4', highlightbackground='cyan4', border=0)
button.place(x=460, y=65)

# Back Button
back_button = Button(app_search, text='Back to Main Menu', font=('Open Sans', 10, 'bold'), bg='cyan3',
                     activebackground='cyan',
                     foreground='cyan4', activeforeground='cyan4', highlightthickness=2,
                     highlightcolor='cyan4', highlightbackground='cyan4', border=2, width=12, height=1,
                     command=back)
back_button.place(x=10, y=10)

app_search.mainloop()
