from tkinter import *
import pymysql
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk

# Create a MySQL connection
con = pymysql.connect(host='localhost', port=3306, user='root', password='Honey@2323', database='proj1_db')
mycursor = con.cursor()

def back():
    gen.destroy()
    import home

# Function to create tables and populate them with sample data
def initialize_database():
    # Create the 'items' table
    query = 'DROP TABLE IF EXISTS product'
    mycursor.execute(query)

    query = 'CREATE TABLE product' \
            '( Product_ID INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(100), Description varchar(2500),' \
            'Category VARCHAR(100), Price int, Username varchar(100), Entry_Date date)'
    mycursor.execute(query)

    # Insert sample data into the 'items' table
    query = "INSERT INTO product (Title, Description, Category, Price, Username, Entry_Date)" \
            "VALUES ('Smartphone', 'This is the new iPhone X', 'Mobile', 1000, '', CURDATE())," \
            "('Laptop', 'Powerful laptop for work and gaming', 'Laptop', 1500, '', CURDATE())," \
            "('Headphones', 'High-quality noise-canceling headphones', 'Electronic', 200, '', CURDATE())," \
            "('Book', 'Bestseller novel', 'Book', 20, '', CURDATE())," \
            "('Camera', 'Professional DSLR camera', 'Electronic', 800, '', CURDATE())"
    mycursor.execute(query)

    # Create the 'reviews' table
    query = 'DROP TABLE IF EXISTS Review'
    mycursor.execute(query)

    query = 'CREATE TABLE Review (' \
            'Review_ID INT AUTO_INCREMENT PRIMARY KEY,' \
            'Product_Name varchar(100),' \
            'Category varchar(200),' \
            'Price INT,' \
            'Rating varchar(100),' \
            'Review varchar(1000),' \
            'User varchar(100),' \
            'Entry_Date date)'
    mycursor.execute(query)

    query = "INSERT INTO Review (Product_Name, Category, Price, Rating, Review, User, Entry_Date)" \
            "VALUES ('Smartphone', 'Mobile', 1000, 'Good', 'Its in a good condition', '', CURDATE())," \
            "('MacPro', 'Laptop', 1500, 'Excellent', 'Great working condition', '', CURDATE())," \
            "('Bosh Headphones', 'Electronic', 200, 'Fair', 'Its working well', '', CURDATE())," \
            "('Five tales', 'Book', 20, 'Excellent', 'Its a new  book', '', CURDATE())," \
            "('Go Pro', 'Electronic', 800, 'Excellent', 'Its an awesome camera', '', CURDATE())"
    mycursor.execute(query)
    # Commit changes to the database
    con.commit()
    display_product_table()
    display_review_table()
    con.close()


def display_product_table():
    ProductHeading = Label(gen, text='Product Table', font=('Microsoft Yahei UI Light', 15), bg='white',
                           fg='cyan4')
    ProductHeading.place(x=440, y=75)
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
    style.theme_use('clam')
    # Create a Treeview widget to display the 'product' table
    product_cols = ("Product ID", "Title", "Description", "Category", "Price", "User", "Entry Date")
    product_tree = ttk.Treeview(gen, columns=product_cols, show='headings')
    for col in product_cols:
        product_tree.heading(col, text=col)
        product_tree.column(col, stretch=YES, width=120, anchor='center')
    product_tree.place(x=70, y=100)
    product_tree.tag_configure('black_text', foreground='black')
    # Retrieve data from the 'product' table and insert it into the Treeview
    query = 'SELECT * FROM product'
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        product_tree.insert("", "end", values=row)


def display_review_table():
    ProductHeading = Label(gen, text='Review Table', font=('Microsoft Yahei UI Light', 15), bg='white',
                           fg='cyan4')
    ProductHeading.place(x=440, y=375)
    # Create a Treeview widget to display the 'product' table
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
    style.theme_use('clam')
    review_cols = ("Review ID", "Product Name", "Category", "Price", "Rating", "Review", "User", "Entry Date")
    review_tree = ttk.Treeview(gen, columns=review_cols, show="headings")
    for col in review_cols:
        review_tree.heading(col, text=col)
        review_tree.column(col, width=120, anchor='center')
    review_tree.place(x=13, y=400)
    review_tree.tag_configure('black_text', foreground='black')
    # Retrieve data from the 'product' table and insert it into the Treeview
    query = 'SELECT * FROM Review'
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        review_tree.insert("", "end", values=row)
    # Back Button
    back_button = Button(gen, text='Back to Main Menu', font=('Open Sans', 10, 'bold'), bg='cyan3',
                         activebackground='cyan',
                         foreground='cyan4', activeforeground='cyan4', highlightthickness=2,
                         highlightcolor='cyan4', highlightbackground='cyan4', border=2, width=12, height=1,
                         command=back)
    back_button.place(x=10, y=10)

gen = Tk()
gen.geometry('990x660+20+20')  # place the window in the comp screen
gen.resizable(False, False)  # disable the full screen option for window
gen.title("Initialize Database")

# Background image setting
bgImage = ImageTk.PhotoImage(file='img/db_bg.png')
bgLabel = Label(gen, image=bgImage)
bgLabel.place(x=0, y=0)

initialize_button = Button(gen, text='Initialize Database', font=('Open Sans', 20, 'bold'), bg='cyan3',
                           activebackground='cyan', foreground='cyan4', activeforeground='cyan4', highlightthickness=2,
                           highlightcolor='cyan4', highlightbackground='cyan4', border=2, width=13, height=1,
                           command=initialize_database)
initialize_button.place(x=385, y=20)

gen.mainloop()
