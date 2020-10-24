#Importing all Libraries

import random
import string
import os.path
import tkinter as tk
from tkinter import messagebox


# get random string password with letters, digits, and symbols
def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    
    return password


# Function for getting data from user input
def get_data():
    user = entry_user.get()
    site = entry_web.get()
    pwd = entry_pass.get()
    return(user,site,pwd)

# This funtion will check the existence of file and if not available, it will create a new one
def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()

# This function will append new password in the txt file
def appendNew():
    checkExistence()
    file = open("info.txt", 'a')

    user,site,pwd = get_data()
    if (user != '' and site != '' and pwd != ''):
        print()
        print()

        userName = user
        passWord = pwd
        website = site

        print()
        print()

        usrnm = "UserName: " + userName + "\n"
        web = "Website: " + website + "\n"
        pwd = "Password: " + passWord + "\n"

        file.write("---------------------------------\n")
        file.write(usrnm)
        file.write(pwd)
        file.write(web)
        file.write("---------------------------------\n")
        file.write("\n")
        file.close
        messagebox.showinfo("Information","Password Saved")
    elif (user == '' or site == '' or pwd == ''):
        messagebox.showwarning("Warning","Please fill all the fields")
        



# This function will print the generated password in the tab next to "Generate Button"

root = tk.Tk()


user = tk.StringVar()  
site = tk.StringVar()
password = tk.StringVar()

def call():
    text = get_random_password_string(10)
    password.set(text)
    

root.title("Password Generator")
root.configure(background=('Gray10'))
root.geometry('400x400')

#Label and prompt for getting username
label_user=tk.Label(root,text='Username:',bg='RoyalBlue3',fg='snow')
label_user.place(x=80, y=200)
entry_user=tk.Entry(textvariable = user, bg='snow', fg='Gray10')
entry_user.place(x = 150, y = 200)

#Label and prompt for getting website name
label_web=tk.Label(root,text='Website:',bg='RoyalBlue3',fg='snow')
label_web.place(x=80, y=250)
entry_web=tk.Entry(textvariable = site, bg='snow', fg='Gray10')
entry_web.place(x = 150, y = 250)

#Button for calling Password Generate Function
button_gen = tk.Button(root, text='Generate', bg='Dark Green',fg = 'snow', activebackground='OrangeRed2',command=call)
button_gen.place(x=80, y=300)
entry_pass=tk.Entry(text= password, bg='snow', fg='Gray10')
entry_pass.place(x = 150, y = 300)

#Button for saving the passowrds into file
button_save = tk.Button(root, text='Save', bg='Dark Green', fg = 'snow',activebackground='OrangeRed2', command=appendNew)
button_save.place(x=150, y=350)


root.mainloop()
