import tkinter as tk
import pandas as pd
from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk
import csv

window = Tk()
window.title("BMI Calculator")
window.geometry('600x400')
window.configure(bg='#8FBC8F')

img = tk.PhotoImage(file='logologin.png')
img2= Image.open('logologin.png')
resize = img2.resize((200,200),Image.LANCZOS)
converted = ImageTk.PhotoImage(resize)
page_check=0

# #path database csv
# database = 'database.csv'

# # Baca database 
# data = pd.read_csv(database)

# # Masukin ke variabel
# username = data['Username']
# password = data['Password']

def awal():
    global frame1,page_check
    if page_check == 0:
        pass
    elif page_check == 2:
        frame2.pack_forget()
    elif page_check == 3:
        frame3.pack_forget()
    page_check=1
    frame1=tk.Frame(window,bg='#8FBC8F')
    frame1.pack(ipadx=600,ipady=400)
    a= tk.Label(frame1,image=converted,border=0,bg='#E9967A')
    a.pack()
    heading = Label(frame1, text='Selamat Datang di BMI & BMR Calculator', fg="white", bg="#8FBC8F",font=('Arial',18,'bold'))
    heading.pack(expand=True,padx=50,pady=30)
    button1 = tk.Button(frame1,text="Sign Up", bg='white',fg='black',command=halaman_Signup)
    button1.pack(expand=True,ipadx=30,ipady=10,pady=30,side='right' )
    button2 = tk.Button(frame1,text="Log In", bg='white',fg='black',command=halaman_SignIn)
    button2.pack(expand=True,ipadx=30,ipady=10,pady=30,side='left')

def signin():
    username=username_entry.get()
    password=password_entry.get()
    
    with open('database.csv','r')as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            if row[1]==username and row[2]==password:
                messagebox.showinfo('sign in','sukses')
                return
        messagebox.showerror('invalid','gagal')

def halaman_SignIn():
    global frame2, page_check, username_entry, password_entry
    frame1.pack_forget()
    page_check=2
    frame2=tk.LabelFrame(window)
    frame2.pack(ipadx=600,ipady=400)
    frame2.configure(bg="#8FBC8F")
    login_label = Label(frame2,text="Menu Login", fg="white", bg="#8FBC8F",font=('Arial',18,'bold'))
    login_label.pack(expand=True,padx=50,pady=10)
    username_label = Label(frame2,text="Username", fg="white", bg="#8FBC8F",font=('Arial',18,'bold'))
    username_label.pack(expand=True,padx=50,pady=20)
    username_entry = tk.Entry(frame2)
    username_entry.pack(padx=10)
    password_label = Label(frame2,text="Password", fg="white", bg="#8FBC8F",font=('Arial',18,'bold'))
    password_label.pack(expand=True,padx=50,pady=20)
    password_entry = tk.Entry(frame2)
    password_entry.pack(padx=50,pady=20)
    login_button = tk.Button(frame2,text="Login",command=signin)
    login_button.pack(expand=True, ipadx=40,padx=50,pady=20,side="left")
    next_button = tk.Button(frame2,text='Next', command=awal)
    next_button.pack(expand=True, ipadx=40,padx=50,pady=20,side="right")


def halaman_Signup():
    global frame3, page_check
    frame1.pack_forget()
    page_check=3
    frame3=tk.LabelFrame(window)
    frame3.pack(ipadx=600,ipady=400)
    frame3.configure(bg="#8FBC8F")
    def signup():
        name=name_entry.get()
        username=user1_entry.get()
        password=password1_entry.get()
        with open('database.csv','a')as file:
            csv_writer=csv.writer(file)
            csv_writer.writerow([name,username,password])
            messagebox.showinfo('Sign Up','sukses')

    signup_label = Label(frame3,text="Menu SignUp", fg="white", bg="#8FBC8F",font=('Arial',18,'bold'))
    signup_label.pack(expand=True,padx=50,pady=5)
    name_label = Label(frame3,text="Nama", fg="white", bg="#8FBC8F",font=('Arial',18,'bold'))
    name_label.pack(expand=True,padx=50,pady=10)
    name_entry = tk.Entry(frame3)
    name_entry.pack(padx=10)
    user1_label = Label(frame3,text="Username", fg="white", bg="#8FBC8F",font=('Arial',18,'bold'))
    user1_label.pack(expand=True,padx=50,pady=15)
    user1_entry = tk.Entry(frame3)
    user1_entry.pack(padx=10)
    password1_label = Label(frame3,text="Password", fg="white", bg="#8FBC8F",font=('Arial',18,'bold'))
    password1_label.pack(expand=True,padx=50,pady=20)
    password1_entry = tk.Entry(frame3)
    password1_entry.pack(padx=50,pady=20)
    signup_button = tk.Button(frame3,text="SignUp",command=signup)
    signup_button.pack(expand=True,padx=50,pady=20,side="left")
    back_button = tk.Button(frame3,text="Back",command=awal)
    back_button.pack(expand=True,ipadx=30,padx=50,pady=20,side="right")


awal()
window.mainloop()
