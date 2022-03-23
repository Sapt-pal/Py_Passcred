# Importing necessary module
from tkinter import *
from tkinter import messagebox

import mysql.connector as sql_conn

window_main = Tk()
window_main.title("PyPassCred: Password Generator and Manager")
window_main.geometry("650x400")

canvas_main = Canvas(window_main, width=500, height=300)
canvas_main.pack()

head = Label(canvas_main, text="PyPassCred", font=("Garamond", 30))
head.grid(row=0, column=0)

sub_head = Label(canvas_main, text='''Python and MySQL Automated Password Management''',
                 font=("Garamond", 18))
sub_head.grid(row=1, column=0)

masterpass_label = Label(canvas_main, text="Master Password", font=("Cambria", 20))
masterpass_label.grid(row=2, column=0, padx=50, pady=(90, 10))

masterpass = Entry(canvas_main, width=50)
masterpass.grid(row=3, column=0)


def login():
    masterpw = masterpass.get()

    if masterpw == "pypasscred":
        window_main.destroy()
        welcome()

    else:
        messagebox.showerror(title='Incorrect Password', message="Wrong Password. Try Again")
        masterpass.delete(0, END)


login_bt = Button(canvas_main, text="LOGIN", command=login,
                  font=("Cambria", 10), borderwidth=3)
login_bt.grid(row=4, column=0, padx=25, pady=25)


def welcome():
    global window_welc

    window_welc = Tk()
    window_welc.title("PyPassCred: Password Generator and Manager")
    window_welc.geometry("650x400")

    canvas_welc = Canvas(window_welc, width=650, height=400)
    canvas_welc.pack()

    welcome = Label(canvas_welc, text="Welcome to the Main Menu", font=("Garamond", 30))
    welcome.grid(row=0, column=0, columnspan=2)

    def create_db():  # Creating a database to store passwords, username and site url

        conn_obj = sql_conn.connect(host="localhost", user="root", passwd="@IshanDas10")
        sql_cursor = conn_obj.cursor()

        if conn_obj.is_connected():
            sql_cursor.execute("CREATE DATABASE IF NOT EXISTS Py_PassCred")
            sql_cursor.execute("USE Py_PassCred")
            table = """CREATE TABLE IF NOT EXISTS passwords_data (
            SNo INTEGER AUTO_INCREMENT PRIMARY KEY, 
            site_URL VARCHAR(50),
            username VARCHAR(20), 
            password VARCHAR(20), 
            password_nature VARCHAR(20) ) """
            sql_cursor.execute(table)

    create = Button(canvas_welc, text="Create a database and table\n (if already does not exist)",
                    padx=80, pady=5, borderwidth=5, command=create_db, font=("Cambria", 15))
    create.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    random_bt = Button(canvas_welc, text="Random Password", padx=30, pady=20, borderwidth=5,
                       command=lambda: [window_welc.destroy(), random()], font=("Cambria", 15))
    random_bt.grid(row=2, column=0, sticky='e', padx=10, pady=5)

    custom_bt = Button(canvas_welc, text="Custom Password", padx=40, pady=20, borderwidth=5,
                       command=lambda: [window_welc.destroy(), custom()], font=("Cambria", 15))
    custom_bt.grid(row=2, column=1, sticky='e', padx=10, pady=5)

    view_bt = Button(canvas_welc, text="View Password", padx=40, pady=20, borderwidth=5,
                     command=lambda: [window_welc.destroy(), view()], font=("Cambria", 15))
    view_bt.grid(row=3, column=0, sticky='e', padx=10, pady=5)

    update_bt = Button(canvas_welc, text="Update Password", padx=41, pady=20, borderwidth=5,
                       command=lambda: [window_welc.destroy(), update()], font=("Cambria", 15))
    update_bt.grid(row=3, column=1, sticky='e', padx=10, pady=5)

    exit_bt = Button(canvas_welc, text="Exit", padx=20, pady=10, borderwidth=5,
                     command=window_welc.destroy, font=("Cambria", 15))
    exit_bt.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    window_welc.mainloop()


def data_entry(site_URL, username, password, password_nature):
    conn_obj = sql_conn.connect(host="localhost", user="root", passwd="@IshanDas10", db="py_passcred")
    sql_cursor = conn_obj.cursor()

    query = f"INSERT INTO passwords_data (site_url, username, password, password_nature)  VALUES (%s, %s, %s, %s)"

    val = (site_URL, username, password, password_nature)

    try:
        sql_cursor.execute(query, val)
        conn_obj.commit()
        sql_cursor.close()
    except Exception as e:
        conn_obj.rollback()
        conn_obj.close()


def random():
    global window_rand

    window_rand = Tk()
    window_rand.title("PyPassCred: Password Generator and Manager")
    window_rand.geometry("650x400")

    canvas_rand = Canvas(window_rand, width=650, height=400)
    canvas_rand.pack()

    rand_label = Label(canvas_rand, text="Random Password Generator", padx=120, pady=30, font=("Garamond", 30))
    rand_label.grid(row=0, column=0, columnspan=3)  # Placing the frame

    url1 = Entry(canvas_rand, width=50)  # Creating an Entry widget for url
    url1_label = Label(canvas_rand, text="URL:", font=("Cambria", 15))  # Entry label for url
    url1_label.grid(row=1, column=0, sticky='e', padx=(5, 10), pady=(5, 5))  # Placing the label
    url1.grid(row=1, column=1, columnspan=2, sticky='w', padx=(10, 5), pady=(5, 5))  # Placing the entry widget

    username1 = Entry(canvas_rand, width=50)  # Creating an Entry widget for username
    username1_label = Label(canvas_rand, text="Username:", font=("Cambria", 15))  # Entry label for username
    username1_label.grid(row=2, column=0, sticky='e', padx=(5, 10), pady=(5, 5))  # Placing the label
    username1.grid(row=2, column=1, columnspan=2, padx=(10, 5), pady=(5, 5), sticky='w')  # Placing the Entry widget

    length_label = Label(canvas_rand, text="Length of the \npassword: ", font=("Cambria", 15))  # Dropdown box label
    length_label.grid(row=3, column=0, sticky='e', padx=(5, 10), pady=(5, 5))  # Placing the label

    # Function to get the value from the dropdown box
    def callback(selection):
        global choice
        choice = selection

    # Creating a dropdown box and placing it
    num_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    clicked = IntVar()
    drop = OptionMenu(canvas_rand, clicked, *num_list, command=callback)
    drop.grid(row=3, column=1, sticky="w", padx=(30, 15), pady=(5, 5))

    # Function to generate random strong password
    def generate_button():
        global choice

        from random import randint

        website = url1.get()
        usern = username1.get()
        passwd = ''

        for i in range(choice):
            i = chr(randint(33, 126))
            passwd = str(passwd) + i

        data_entry(website, usern, passwd, 'Random')

        messagebox.showinfo("Password Stored!", f"Password for {website} is :\n {passwd}")

        url1.delete(0, END)  # Removing the entries from url entry

        username1.delete(0, END)  # Removing the entries from username entry

    generate = Button(canvas_rand, text="Generate", font=("Cambria", 10),
                      command=generate_button, pady=20, borderwidth=4)
    generate.grid(row=4, column=1, pady=(15, 10), sticky="ew")  # Placing the button

    back_rand = Button(canvas_rand, text="Back to the Main Menu", font=("Cambria", 10),
                       command=lambda: [window_rand.destroy(), welcome()],
                       pady=20, borderwidth=4)
    back_rand.grid(row=5, column=1, pady=(15, 10), sticky="ew")

    window_rand.mainloop()


def custom():
    global window_cust

    global url
    global username
    global password_custom

    window_cust = Tk()
    window_cust.title("PyPassCred: Password Generator and Manager")
    window_cust.geometry("650x400")

    canvas_cust = Canvas(window_cust, width=650, height=400)
    canvas_cust.pack()

    cust_label = Label(canvas_cust, text="Custom Password", padx=120, pady=30, font=("Garamond", 30))
    cust_label.grid(row=0, column=0, columnspan=3, sticky='e')

    # Function to insert the custom data into database
    def save():

        file_url = url.get()
        url_string = ''
        for i in [file_url]:
            url_string += i

        file_username = username.get()
        username_string = ''
        for i in [file_username]:
            username_string += i

        file_password_custom = password_custom.get()
        password_custom_string = ''
        for i in [file_password_custom]:
            password_custom_string += i

        data_entry(url_string, username_string, password_custom_string, "Custom")

        messagebox.showinfo("Password Stored!", f"Password for {url_string} is :\n\n {password_custom_string}")

    # Function to remove entries from the entry widgets
    def new():
        url.delete(0, END)
        username.delete(0, END)
        password_custom.delete(0, END)

    # Creating an Entry widget for url
    url = Entry(canvas_cust, width=50)
    url_label = Label(canvas_cust, text="URL:", font=("Cambria", 15))
    url_label.grid(row=1, column=0, sticky='e', padx=(5, 10), pady=(5, 5))
    url.grid(row=1, column=1, columnspan=2, sticky='w', padx=(10, 5), pady=(5, 5))

    # Creating an Entry widget for username
    username = Entry(canvas_cust, width=50)
    username_label = Label(canvas_cust, text="Username:", font=("Cambria", 15))
    username_label.grid(row=2, column=0, sticky='e', padx=(5, 10), pady=(5, 5))
    username.grid(row=2, column=1, columnspan=2, padx=(10, 5), pady=(5, 5), sticky='w')

    # Creating an Entry widget for password
    password_custom = Entry(canvas_cust, width=50)
    password_custom_label = Label(canvas_cust, text="Password:", font=("Cambria", 15))
    password_custom_label.grid(row=3, column=0, sticky='e', padx=(5, 10), pady=(5, 5))
    password_custom.grid(row=3, column=1, columnspan=2, padx=(10, 5), pady=(5, 5), sticky='w')

    # Creating a save button
    save_button = Button(canvas_cust, text="Save", padx=5, pady=5, font=("Cambria", 10),
                         command=save, borderwidth=4)
    save_button.grid(row=4, column=1, pady=(10, 10), padx=(15, 10))

    # Creating a New Entry button
    new_button = Button(canvas_cust, text="New entry", padx=5, pady=5, font=("Cambria", 10),
                        command=new, borderwidth=4)
    new_button.grid(row=4, column=2, pady=(10, 10), padx=(15, 10))

    back_cust = Button(canvas_cust, text="Back to the Main Menu", font=("Cambria", 10),
                       command=lambda: [window_cust.destroy(), welcome()],
                       pady=20, borderwidth=4)
    back_cust.grid(row=5, column=1, pady=(15, 10), sticky="ew")

    window_cust.mainloop()


def view():
    global window_view

    window_view = Tk()
    window_view.title("PyPassCred: Password Generator and Manager")
    window_view.geometry("650x400")

    canvas_view = Canvas(window_view, width=650, height=400)
    canvas_view.pack()

    def view_pw():
        global pw
        conn_obj = sql_conn.connect(host="localhost", user="root", passwd="@IshanDas10", db="py_passcred")
        sql_cursor = conn_obj.cursor()

        view_url = url_retrieve.get()
        view_usern = username_retrieve.get()

        query = f"""SELECT password FROM passwords_data where site_URL = '{view_url}' and username = '{view_usern}'"""

        try:
            sql_cursor.execute(query)
            p = sql_cursor.fetchone()
            pw = p[0]
            conn_obj.commit()
            sql_cursor.close()
        except Exception as e:
            conn_obj.rollback()
            conn_obj.close()

        url_retrieve.delete(0, END)
        username_retrieve.delete(0, END)

        messagebox.showinfo("Password Viewer", f"Password for {view_url} is :\n\n {pw}")

    view_label = Label(canvas_view, text="View Password", padx=120, pady=30, font=("Garamond", 30))
    view_label.grid(row=0, column=0, columnspan=3, sticky='e')

    # Creating an Entry widget for url
    url_retrieve = Entry(canvas_view, width=35)
    url_retrieve_label = Label(canvas_view, text="URL:", font=("Cambria", 15))
    url_retrieve_label.grid(row=1, column=0, sticky='e', padx=(5, 10), pady=(5, 5))
    url_retrieve.grid(row=1, column=1, columnspan=2, sticky='w', padx=(10, 5), pady=(5, 5))

    # Creating an Entry widget for username
    username_retrieve = Entry(canvas_view, width=35)
    username_retrieve_label = Label(canvas_view, text="Username:", font=("Cambria", 15))
    username_retrieve_label.grid(row=2, column=0, sticky='e', padx=(5, 10), pady=(5, 5))
    username_retrieve.grid(row=2, column=1, columnspan=2, padx=(10, 5), pady=(5, 5), sticky='w')

    # Creating a Button to view the password
    view_button = Button(canvas_view, text="View Password", borderwidth=4, padx=15, pady=8, command=view_pw)
    view_button.grid(row=3, column=1, pady=(10, 10), padx=(15, 10))

    back_view = Button(canvas_view, text="Back to the Main Menu", font=("Cambria", 10),
                       command=lambda: [window_view.destroy(), welcome()],
                       pady=20, borderwidth=4)
    back_view.grid(row=5, column=1, pady=(15, 10), sticky="ew")

    window_view.mainloop()


def update():
    global window_up

    window_up = Tk()
    window_up.title("PyPassCred: Password Generator and Manager")
    window_up.geometry("650x400")

    canvas_up = Canvas(window_up, width=650, height=400)
    canvas_up.pack()

    def update_pswd():
        import mysql.connector as sql_conn

        conn_obj = sql_conn.connect(host="localhost", user="root", passwd="@IshanDas10", db="py_passcred")
        sql_cursor = conn_obj.cursor()

        url_upfunc = update_url.get()
        usern_upfunc = username_update.get()
        old_pw = old_password.get()
        new_pw = new_password.get()

        exc = f"""UPDATE passwords_data set password = '{new_pw}'
        where site_URL = '{url_upfunc}'
        and username = '{usern_upfunc}'
        and password = '{old_pw}'"""
        try:
            sql_cursor.execute(exc)
            conn_obj.commit()
            sql_cursor.close()
        except Exception as e:
            conn_obj.rollback()
            conn_obj.close()

        messagebox.showinfo("Password Changed!", f"Password for {url_upfunc} is changed to:\n\n {new_pw}")

        update_url.delete(0, END)
        username_update.delete(0, END)
        old_password.delete(0, END)
        new_password.delete(0, END)

    update_label = Label(canvas_up, text="Update Password", padx=120, pady=30, font=("Garamond", 30))
    update_label.grid(row=0, column=0, columnspan=3, sticky='e')

    update_url = Entry(canvas_up, width=50)
    update_url_label = Label(canvas_up, text="URL:", font=("Cambria", 15))
    update_url_label.grid(row=1, column=0, sticky='e', padx=(5, 10), pady=(5, 5))
    update_url.grid(row=1, column=1, columnspan=2, sticky='w', padx=(10, 5), pady=(5, 5))

    username_update = Entry(canvas_up, width=50)
    username_update_label = Label(canvas_up, text="Username:", font=("Cambria", 15))
    username_update_label.grid(row=2, column=0, sticky='e', padx=(5, 10), pady=(5, 5))
    username_update.grid(row=2, column=1, columnspan=2, padx=(10, 5), pady=(5, 5), sticky='w')

    old_password = Entry(canvas_up, width=50)
    old_password_label = Label(canvas_up, text="Old Password:", font=("Cambria", 15))
    old_password_label.grid(row=3, column=0, sticky='e', padx=(5, 10), pady=(5, 5))
    old_password.grid(row=3, column=1, columnspan=2, padx=(10, 5), pady=(5, 5), sticky='w')

    new_password = Entry(canvas_up, width=50)
    new_password_label = Label(canvas_up, text="Password:", font=("Cambria", 15))
    new_password_label.grid(row=4, column=0, sticky='e', padx=(5, 10), pady=(5, 5))
    new_password.grid(row=4, column=1, columnspan=2, padx=(10, 5), pady=(5, 5), sticky='w')

    update_button = Button(canvas_up, text="Update Password", borderwidth=4, padx=15, pady=8, command=update_pswd)
    update_button.grid(row=5, column=1, pady=(6, 10), padx=(15, 10))

    back_up = Button(canvas_up, text="Back to the Main Menu", font=("Cambria", 10),
                     command=lambda: [window_up.destroy(), welcome()],
                     pady=20, borderwidth=4)
    back_up.grid(row=6, column=1, pady=(15, 10), sticky="ew")

    window_up.mainloop()


window_main.mainloop()
