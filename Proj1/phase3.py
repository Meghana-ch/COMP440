from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import ttk

# Create a MySQL connection
con = pymysql.connect(host='localhost', port=3306, user='root', password='Honey@2323', database='proj1_db')
mycursor = con.cursor()

# Main Table Formation
def table_form(items, columns):
    # Calculate the number of rows and columns
    num_rows = len(items) + 1  # +1 for the header row
    num_columns = len(items[0]) if items else 1  # Assuming there is at least one column

    # Calculate the width and height of the result window based on the number of rows and columns
    window_width = num_columns * 100  # Adjust the factor based on your column width
    window_height = num_rows * 25  # Adjust the factor based on your row height

    # Create a new window to display the results
    result_window = Toplevel()
    result_window.geometry(f'{window_width}x{window_height}')
    result_window.title('Expensive Items in Each Category')

    style = ttk.Style()
    style.configure("Treeview",
                    background="powder blue",
                    fieldbackground="powder blue",
                    borderwidth=2,
                    relief="solid"
                    )
    style.configure("Treeview.Heading",
                    foreground="black",
                    font=('Helvetica', 14, 'bold', 'underline')
                    )
    style.configure("Treeview.Cell",
                    foreground="black"
                    )
    tree = ttk.Treeview(result_window, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='center')

    # Insert the retrieved items into the table
    for item in items:
        tree.insert("", "end", values=item, tags=('black_text',))
    tree.tag_configure('black_text', foreground='black')
    tree.pack()


def table_form_single(items, columns):
    # Calculate the number of rows and columns
    num_rows = len(items) + 1  # +1 for the header row
    num_columns = len(items[0]) if items else 1  # Assuming there is at least one column

    # Calculate the width and height of the result window based on the number of rows and columns
    window_width = num_columns * 100  # Adjust the factor based on your column width
    window_height = num_rows * 25  # Adjust the factor based on your row height

    # Create a new window to display the results
    result_window = Toplevel()
    result_window.geometry(f'{window_width}x{window_height}')
    result_window.title('Expensive Items in Each Category')

    style = ttk.Style()
    style.configure("Treeview",
                    background="powder blue",
                    fieldbackground="powder blue",
                    borderwidth=2,
                    relief="solid"
                    )
    style.configure("Treeview.Heading",
                    foreground="black",
                    font=('Helvetica', 14, 'bold', 'underline')
                    )
    style.configure("Treeview.Cell",
                    foreground="black"
                    )
    tree = ttk.Treeview(result_window, columns=columns, show='headings')

    tree.heading(columns, text=columns)
    tree.column(columns, width=100, anchor='center')

    # Insert the retrieved items into the table
    for item in items:
        tree.insert("", "end", values=item, tags=('black_text',))
    tree.tag_configure('black_text', foreground='black')
    tree.pack()

# GUI
p3 = Tk()
p3.geometry('990x660+20+20')  # place the window in the comp screen
p3.resizable(False, False)  # disable the full screen option for window
p3.title('Phase 3 Page')  # Title of the window

# Background image setting
bgImage = ImageTk.PhotoImage(file='img/db_bg.png')
bgLabel = Label(p3, image=bgImage)
bgLabel.place(x=0, y=0)
frame0 = Frame(p3, width=3, height=660, bg='cyan4')
frame0.place(x=495, y=0)

frameA = Frame(p3, width=990, height=3, bg='cyan4')
frameA.place(x=0, y=132)

frameB = Frame(p3, width=990, height=3, bg='cyan4')
frameB.place(x=0, y=264)

frameC = Frame(p3, width=990, height=3, bg='cyan4')
frameC.place(x=0, y=396)

frameD = Frame(p3, width=990, height=3, bg='cyan4')
frameD.place(x=0, y=528)

# -------------------------------------------TASK 1------------------------------------------------------
def task1():
    query = 'SELECT Product_ID, Title, MAX(Price), Category FROM product GROUP BY Category'
    mycursor.execute(query)
    items = mycursor.fetchall()
    columns = ('ID', 'Title', 'Price', 'Category')
    table_form(items, columns)

# Task 1 Heading
XHeading = Label(p3, text='TASK 1', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=220, y=15)
# Expensive in each category
ExpButton = Button(p3, text='Expensive Item in each Category', font=('Open Sans', 15, 'bold'), bg='cyan3',
                   activebackground='cyan',
                   foreground='cyan4', activeforeground='cyan4', highlightthickness=2, highlightcolor='cyan4',
                   highlightbackground='cyan4', border=2, width=20, height=1, command=task1)
ExpButton.place(x=110, y=70)

# ---------------------------------------------TASK 2-----------------------------------------------------
def X_enter(event):
    if XEntry.get() == 'X Category':
        XEntry.delete(0, END)

# Task 2 Heading
XHeading = Label(p3, text='TASK 2', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=720, y=15)

# Entry for X
XHeading = Label(p3, text='Enter Category X:', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=510, y=60)
XEntry = Entry(p3, width=15, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='Cyan', bg='white',
               highlightthickness=0)
XEntry.place(x=510, y=90)
XEntry.insert(0, 'X Category')
XEntry.bind('<FocusIn>', X_enter)
frame1 = Frame(p3, width=168, height=3, bg='cyan4')
frame1.place(x=510, y=110)

def Y_enter(event):
    if YEntry.get() == 'Y Category':
        YEntry.delete(0, END)

# Entry for Y
YHeading = Label(p3, text='Enter Category Y:', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
YHeading.place(x=680, y=60)
YEntry = Entry(p3, width=15, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='Cyan', bg='white',
               highlightthickness=0)
YEntry.place(x=680, y=90)
YEntry.insert(0, 'Y Category')
YEntry.bind('<FocusIn>', Y_enter)
frame2 = Frame(p3, width=168, height=3, bg='cyan4')
frame2.place(x=680, y=110)

def task2():
    query = ('SELECT Username, Title, Category, Price FROM product WHERE category IN (%s, %s) GROUP BY Username, '
             'DATE(Entry_Date) HAVING COUNT(DISTINCT Category) = 2 AND COUNT(*) >= 2;')
    mycursor.execute(query, (XEntry.get(), YEntry.get()))
    items = mycursor.fetchall()
    columns = ('Username', 'Title', 'Category', 'Price')
    table_form(items, columns)

# Search Button
Search1Button = Button(p3, text='Search User', font=('Open Sans', 15, 'bold'), bg='cyan3', activebackground='cyan',
                       foreground='cyan4', activeforeground='cyan4', highlightthickness=2, highlightcolor='cyan4',
                       highlightbackground='cyan4', border=2, width=6, height=1, command=task2)
Search1Button.place(x=870, y=70)

# -------------------------------------------------TASK 3---------------------------------------------------
def User_enter(event):
    if UserEntry.get() == 'Username':
        UserEntry.delete(0, END)

# Task 3 Heading
XHeading = Label(p3, text='TASK 3', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=220, y=147)

# Entry for Username
UserHeading = Label(p3, text='Enter the Username:', font=('Microsoft Yahei UI Light', 15),
                    bg='white', fg='cyan4')
UserHeading.place(x=50, y=190)
UserEntry = Entry(p3, width=15, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='Cyan', bg='white',
                  highlightthickness=0)
UserEntry.place(x=50, y=220)
UserEntry.insert(0, 'Username')
UserEntry.bind('<FocusIn>', User_enter)
frame3 = Frame(p3, width=168, height=3, bg='cyan4')
frame3.place(x=50, y=240)

def task3():
    global tree
    query = '''
            SELECT DISTINCT product.Title
            FROM product
            JOIN Review ON product.Title = Review.Product_Name
            WHERE product.Username = %s
            AND Review.Rating IN ('Excellent', 'Good');
    '''
    mycursor.execute(query, (UserEntry.get()))
    items = mycursor.fetchall()
    columns = 'Title'
    table_form_single(items, columns)

# Search Button
Search2Button = Button(p3, text='Search Reviews', font=('Open Sans', 15, 'bold'), bg='cyan3', activebackground='cyan',
                       foreground='cyan4', activeforeground='cyan4', highlightthickness=2, highlightcolor='cyan4',
                       highlightbackground='cyan4', border=2, width=9, height=1, command=task3)
Search2Button.place(x=260, y=200)

# -------------------------------------------------------TASK4-----------------------------------------------------------
def Date_enter(event):
    if DateEntry.get() == 'Date(YYYY-MM-DD)':
        DateEntry.delete(0, END)

# Task 4 Heading
XHeading = Label(p3, text='TASK 4', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=720, y=147)

# Entry for Date
DateHeading = Label(p3, text='Enter the Date:', font=('Microsoft Yahei UI Light', 15),
                    bg='white', fg='cyan4')
DateHeading.place(x=580, y=190)
DateEntry = Entry(p3, width=15, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='Cyan', bg='white',
                  highlightthickness=0)
DateEntry.place(x=580, y=220)
DateEntry.insert(0, 'Date(YYYY-MM-DD)')
DateEntry.bind('<FocusIn>', Date_enter)
frame4 = Frame(p3, width=168, height=3, bg='cyan4')
frame4.place(x=580, y=240)

def task4():
    global tree
    query = 'SELECT Username, COUNT(*) AS posted_items FROM product WHERE Entry_Date = %s GROUP BY Username' \
            ' HAVING COUNT(*) = (SELECT MAX(Entry_Date) FROM(SELECT COUNT(*) AS Entry_Date FROM product' \
            ' WHERE Entry_Date = %s GROUP BY Username) AS counts)'

    mycursor.execute(query, (DateEntry.get(), DateEntry.get()))
    items = mycursor.fetchall()
    columns = ('Username', 'Title', 'Category', 'Rating')
    table_form(items, columns)


Search3Button = Button(p3, text='Search User', font=('Open Sans', 15, 'bold'), bg='cyan3', activebackground='cyan',
                       foreground='cyan4', activeforeground='cyan4', highlightthickness=2, highlightcolor='cyan4',
                       highlightbackground='cyan4', border=2, width=9, height=1, command=task4)
Search3Button.place(x=780, y=200)

# --------------------------------------------- Task 5 -----------------------------------------------------
# Task 5 Heading
XHeading = Label(p3, text='TASK 5', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=220, y=279)
# Entry for UserX
UserXHeading = Label(p3, text='Select User X', font=('Microsoft Yahei UI Light', 12), bg='white', fg='cyan4')
UserXHeading.place(x=110, y=310)
variable1 = StringVar(p3)
variable1.set("Default")  # default value
# Query to retrieve usernames from the Review table
query = 'SELECT DISTINCT User FROM Review'
mycursor.execute(query)
Usernames = mycursor.fetchall()
# Extract usernames from the result
usernames_list = [row[0] for row in Usernames]
UserXEntry = OptionMenu(p3, variable1, *usernames_list)
UserXEntry.config(bg='cyan4', fg='white', width=10)
UserXEntry.place(x=110, y=335)

# Entry for UserY
UserYHeading = Label(p3, text='Select User Y', font=('Microsoft Yahei UI Light', 12), bg='white', fg='cyan4')
UserYHeading.place(x=260, y=310)
variable2 = StringVar(p3)
variable2.set("Default")  # default value
# Query to retrieve usernames from the Review table
query = 'SELECT DISTINCT User FROM Review'
mycursor.execute(query)
Usernames = mycursor.fetchall()
# Extract usernames from the result
usernames_list = [row[0] for row in Usernames]
UserYEntry = OptionMenu(p3, variable2, *usernames_list)
UserYEntry.config(bg='cyan4', fg='white', width=10)
UserYEntry.place(x=260, y=335)

def task5():
    global tree
    query = '''
            SELECT DISTINCT u.Username
            FROM user u
            JOIN product p ON u.Username = p.Username
            JOIN Review r1 ON p.Title = r1.Product_Name
            JOIN Review r2 ON p.Title = r2.Product_Name
            WHERE r1.User = %s
               AND r1.Rating IN ('good', 'excellent')
               AND r2.User = %s
               AND r2.Rating IN ('good', 'excellent');
            '''
    mycursor.execute(query, (variable1.get(), variable2.get()))
    items = mycursor.fetchall()
    columns = 'Username'
    table_form_single(items, columns)


Search10Button = Button(p3, text='Search Favorite User', font=('Open Sans', 15, 'bold'), bg='cyan3',
                        activebackground='cyan', foreground='cyan4', activeforeground='cyan4', highlightthickness=2,
                        highlightcolor='cyan4', highlightbackground='cyan4', border=2, width=15, height=1, command=task5)
Search10Button.place(x=150, y=360)

# --------------------------------------------Task 6-------------------------------------------------------
def task6():
    global tree
    query = '''
        SELECT DISTINCT u.Username
        FROM product u
        LEFT JOIN product i ON u.Username = i.Username
        LEFT JOIN Review r ON i.Title = r.Product_Name
        WHERE i.Title IS NULL
           OR (r.Rating IS NULL)
           OR (r.Rating != 'Excellent')
           OR (
                 r.Rating = 'Excellent'
                 AND (
                        SELECT COUNT(*)
                        FROM Review
                        WHERE Product_Name = i.Title AND Rating = 'Excellent'
                     ) < 3
              )
    '''
    mycursor.execute(query)
    items = mycursor.fetchall()
    columns = 'Username'
    table_form_single(items, columns)

# Task 6 Heading
XHeading = Label(p3, text='TASK 6', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=720, y=279)
Search5Button = Button(p3, text='Search Excellent Products', font=('Open Sans', 15, 'bold'), bg='cyan3',
                       activebackground='cyan',
                       foreground='cyan4', activeforeground='cyan4', highlightthickness=2, highlightcolor='cyan4',
                       highlightbackground='cyan4', border=2, width=15, height=1, command=task6)
Search5Button.place(x=650, y=330)

# --------------------------------------------Task 7-------------------------------------------------------
def task7():
    global tree
    query = '''
        SELECT DISTINCT User
        FROM Review
        WHERE User NOT IN (
            SELECT User
            FROM Review
            WHERE Rating = 'Poor'
        )
    '''
    mycursor.execute(query)
    items = mycursor.fetchall()
    columns = 'Username'
    table_form_single(items, columns)

# Task 7 Heading
XHeading = Label(p3, text='TASK 7', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=220, y=411)

Search6Button = Button(p3, text='Search No Poor Reviews', font=('Open Sans', 15, 'bold'), bg='cyan3',
                       activebackground='cyan',
                       foreground='cyan4', activeforeground='cyan4', highlightthickness=2, highlightcolor='cyan4',
                       highlightbackground='cyan4', border=2, width=15, height=1, command=task7)
Search6Button.place(x=145, y=460)

# --------------------------------------------Task 8-------------------------------------------------------
def task8():
    global tree
    query = '''
        SELECT DISTINCT User
        FROM Review
        WHERE User NOT IN (
            SELECT User
            FROM Review
            WHERE Rating != 'Poor'
        )
    '''
    mycursor.execute(query)
    items = mycursor.fetchall()
    columns = 'Username'
    table_form_single(items, columns)

# Task 8 Heading
XHeading = Label(p3, text='TASK 8', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=720, y=411)

Search7Button = Button(p3, text='Search Poor Reviews', font=('Open Sans', 15, 'bold'), bg='cyan3',
                       activebackground='cyan', foreground='cyan4', activeforeground='cyan4', highlightthickness=2,
                       highlightcolor='cyan4', highlightbackground='cyan4', border=2, width=15, height=1, command=task8)
Search7Button.place(x=645, y=460)

# --------------------------------------------Task 9-------------------------------------------------------
def task9():
    global tree
    query = '''
        SELECT DISTINCT p.Username
        FROM product p
        LEFT JOIN Review r ON p.Title = r.Product_Name
        WHERE p.Username != ''  -- Exclude items without a username
          AND (
                r.Rating IS NULL  -- Exclude items without reviews
                OR r.Rating != 'poor'  -- Exclude items with 'poor' reviews
              )
          AND NOT EXISTS (
                SELECT 1
                FROM product p2
                LEFT JOIN Review r2 ON p2.Title = r2.Product_Name
                WHERE p2.Username = p.Username
                  AND (
                        r2.Rating IS NULL  -- Exclude items without reviews
                        OR r2.Rating = 'poor'  -- Include items with 'poor' reviews
                      )
              )
    '''
    mycursor.execute(query)
    items = mycursor.fetchall()
    columns = ('Username', 'Title')
    table_form(items, columns)

# Task 9 Heading
XHeading = Label(p3, text='TASK 9', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=220, y=543)

Search8Button = Button(p3, text='Search No Poor Reviews Product', font=('Open Sans', 15, 'bold'), bg='cyan3',
                       activebackground='cyan',
                       foreground='cyan4', activeforeground='cyan4', highlightthickness=2, highlightcolor='cyan4',
                       highlightbackground='cyan4', border=2, width=20, height=1, command=task9)
Search8Button.place(x=120, y=590)

# --------------------------------------------Task 10-------------------------------------------------------
def task10():
    global tree
    query = '''
        SELECT U1.USERNAME AS USER_A, U2.USERNAME AS USER_B
        FROM USER U1, USER U2
        WHERE U1.USERNAME < U2.USERNAME
        AND NOT EXISTS (
            SELECT 1
            FROM PRODUCT P1
            LEFT JOIN REVIEW R1 ON P1.Product_ID = R1.Product_ID AND R1.User = U2.Username
            WHERE P1.Username = U1.Username AND (R1.Rating IS NULL OR R1.Rating != 'Excellent')
        )
        AND NOT EXISTS (
            SELECT 1
            FROM PRODUCT P2
            LEFT JOIN REVIEW R2 ON P2.Product_ID = R2.Product_ID AND R2.User = U1.USERNAME
            WHERE P2.USERNAME = U2.USERNAME AND (R2.Rating IS NULL OR R2.Rating != 'Excellent'))
        '''
    mycursor.execute(query)
    items = mycursor.fetchall()
    columns = ('Username1', 'Username2')
    table_form(items, columns)

# Task 10 Heading
XHeading = Label(p3, text='TASK 10', font=('Microsoft Yahei UI Light', 15),
                 bg='white', fg='cyan4')
XHeading.place(x=720, y=543)

Search9Button = Button(p3, text='Search Friends on Reviews', font=('Open Sans', 15, 'bold'), bg='cyan3',
                       activebackground='cyan',
                       foreground='cyan4', activeforeground='cyan4', highlightthickness=2, highlightcolor='cyan4',
                       highlightbackground='cyan4', border=2, width=20, height=1, command=task10)
Search9Button.place(x=625, y=590)

p3.mainloop()
