import csv
from tkinter import *  # Importing Tkinter module for GUI

window = Tk()  # Creating a window
window.title("PyPassCred: Password Generator and Manager")  # Adding title for the window
window.geometry("1240x1000")  # Setting geometry of the window

head = Label(window, text="PyPassCred", font=("MONTSERRAT", 30))  # Creating a the heading
# for the window
head.place(x=500, y=10)  # Placing the heading in the window

# vertical = Scale(window, from_=0, to=200)
# vertical.place(x=1200, y=0)


def create_passfile():  # Creating a file to store passwords, username and site url
   with open("password.csv", 'w') as passfile:
       csvwriter = csv.writer(passfile)
       csvwriter.writerow(["WEBSITE", "USERNAME", "PASSWORD"])


def enable():                                       # Enabling all the frames and Create Button
   for i in frame_random.winfo_children():
       i.configure(state='normal')
   for i in frame_custom.winfo_children():
       i.configure(state='normal')
   for i in view_frame.winfo_children():
       i.configure(state='normal')
   for i in update_frame.winfo_children():
       i.configure(state='normal')
   create.configure(state='normal')


login_label = Label(window, text="")

master_password = Entry(window, width=50)               # Entry field for Master Password
master_password.place(x=600, y=95)
master_label = Label(window, text="Master Password:")
master_label.place(x=500, y=95)


def login():                                            # Function for login button
   global create
   global login_label
   masterpass = master_password.get()

   if masterpass == "ishanrocks":

       enable()

       login_label.config(text="**Success**", fg="blue")
       login_label.place(x=690, y=110)

       master_password.delete(0, END)
   else:
       login_label.config(text="**Wrong Password**", fg="red")
       login_label.place(x=690, y=110)


login_button = Button(window, text="Login", padx=5, pady=3, command=login)
login_button.place(x=920, y=92)

create_label = Label(window, text="Click here to create a file to save password", font=("Calibri", 11))  # Creating a
# label to identify create button
create_label.place(x=35, y=85)  # Placing a label
create = Button(window, text="Create", padx=5, pady=5, command=create_passfile)  # Creating a create button
create.place(x=310, y=95)  # Placing the button
caution = Label(window, text="(Caution: On clicking this button it will create a new file\n and all your existing "
                            "password will be deleted)", font=("Calibri", 8), fg="red")  # Creating a caution label
# to warn users
caution.place(x=40, y=105)       # Placing caution


def insert_pass(listpass):           # Function to add passwords, site url and username to the file
   with open("password.csv", 'a', newline='') as filepass:
       csvwriter = csv.writer(filepass)
       csvwriter.writerow(listpass)
       listpass.clear()


# Random Password Frame

frame_random = LabelFrame(window, text="Random Password Generator", padx=120, pady=57)  # A frame for generating
# random password
frame_random.place(x=40, y=150)  # Placing the frame

url1 = Entry(frame_random, width=50)  # Creating an Entry widget for url
url1_label = Label(frame_random, text="URL:")  # Entry label for url
url1_label.grid(row=0, column=1)  # Placing the label
url1.grid(row=0, column=2, columnspan=2)  # Placing the entry widget

username1 = Entry(frame_random, width=50)  # Creating an Entry widget for username
username1_label = Label(frame_random, text="Username:")  # Entry label for username
username1_label.grid(row=1, column=1)  # Placing the label
username1.grid(row=1, column=2, columnspan=2)  # Placing the Entry widget

length_label = Label(frame_random, text="Length of the \npassword: ")  # Dropdown box label
length_label.grid(row=2, column=1)  # Placing the label


def callback(selection):  # Func to get the value from the dropdown box
   global choice
   choice = selection


clicked = IntVar()
drop = OptionMenu(frame_random, clicked, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, command=callback)
# Creating a dropdown box
drop.grid(row=2, column=2)  # Placing the dropdown box


def generate_button():  # Func to generate random strong password
   global choice, list1

   from random import randint

   website = url1.get()
   usern = username1.get()
   passwd = ''

   for i in range(choice):
       i = chr(randint(33, 126))
       passwd = str(passwd) + i
       list1 = [website, usern, passwd]

   insert_pass(list1)  # Inserting the password to the file

   password_label = Label(frame_random, text="Generated password for %s is: " % website)
   label = Label(frame_random, text=passwd)

   password_label.grid(row=3, column=2)
   label.grid(row=4, column=2)

   url1.delete(0, END)  # Removing the entries from url entry

   username1.delete(0, END)  # Removing the entries from username entry


generate = Button(frame_random, text="Generate", command=generate_button)  # Creating a generate button
generate.grid(row=2, column=3)  # Placing the button

# Custom Password Frame

frame_custom = LabelFrame(window, text="Custom Password", padx=130, pady=77)  # A frame for entering custom password
frame_custom.place(x=40, y=430)


def save():  # Func to arrange the passwords in list and save the list in the file
   global url
   global username
   global password_custom

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

   passlist = [url_string, username_string, password_custom_string]  # A list containing username site url and
   # password is created

   insert_pass(passlist)


def new():  # Func to remove entries from the entry widgets
   url.delete(0, END)
   username.delete(0, END)
   password_custom.delete(0, END)


url = Entry(frame_custom, width=50)     # Creating an Entry widget for url
url_label = Label(frame_custom, text="URL:")
url_label.grid(row=0, column=1)
url.grid(row=0, column=2, columnspan=2)

username = Entry(frame_custom, width=50)    # Creating an Entry widget for username
username_label = Label(frame_custom, text="Username:")
username_label.grid(row=1, column=1)
username.grid(row=1, column=2, columnspan=2)

password_custom = Entry(frame_custom, width=50)     # Creating an Entry widget for password
password_custom_label = Label(frame_custom, text="Password:")
password_custom_label.grid(row=2, column=1)
password_custom.grid(row=2, column=2, columnspan=2)

save_button = Button(frame_custom, text="Save", padx=5, pady=5, command=save)       # Creating a save button
save_button.grid(row=3, column=2)

new_button = Button(frame_custom, text="New entry", padx=5, pady=5, command=new)     # Creating a New Entry button
new_button.grid(row=3, column=3)

# View Password
view_frame = LabelFrame(window, text="View Password", padx=140, pady=65)
view_frame.place(x=695, y=150)

url_retrieve = Entry(view_frame, width=35)  # Creating an Entry widget for url
url_retrieve_label = Label(view_frame, text="URL:")
url_retrieve_label.grid(row=0, column=1)
url_retrieve.grid(row=0, column=2, columnspan=2)

username_retrieve = Entry(view_frame, width=35)  # Creating an Entry widget for username
username_retrieve_label = Label(view_frame, text="Username:")
username_retrieve_label.grid(row=1, column=1)
username_retrieve.grid(row=1, column=2, columnspan=2)

view_button = Button(view_frame, text="View Password")
view_button.grid(row=2, column=2)

# Update Password frame
update_frame = LabelFrame(window, text="Update Password", padx=130, pady=77)  # A frame for entering custom password
update_frame.place(x=695, y=430)

update_url = Entry(update_frame, width=35)  # Creating an Entry widget for url
update_url_label = Label(update_frame, text="URL:")
update_url_label.grid(row=0, column=1)
update_url.grid(row=0, column=2, columnspan=2)

username_update = Entry(update_frame, width=35)  # Creating an Entry widget for username
username_update_label = Label(update_frame, text="Username:")
username_update_label.grid(row=1, column=1)
username_update.grid(row=1, column=2, columnspan=2)

old_password = Entry(update_frame, width=35)  # Creating an Entry widget for old password
old_password_label = Label(update_frame, text="Old Password:")
old_password_label.grid(row=2, column=1)
old_password.grid(row=2, column=2, columnspan=2)

new_password = Entry(update_frame, width=35)  # Creating an Entry widget for new password
new_password_label = Label(update_frame, text="New Password:")
new_password_label.grid(row=3, column=1)
new_password.grid(row=3, column=2, columnspan=2)

update_button = Button(update_frame, text="Update Password")
update_button.grid(row=4, column=2)

for child in frame_custom.winfo_children():         # Disabling Custom Password Frame
   child.configure(state='disable')
for child in frame_random.winfo_children():         # Disabling Random Password Frame
   child.configure(state='disable')
for child in view_frame.winfo_children():           # Disabling View Password Frame
   child.configure(state='disable')
for child in update_frame.winfo_children():           # Disabling View Password Frame
   child.configure(state='disable')
create.configure(state="disable")                   # Disabling Create button

window.mainloop()
