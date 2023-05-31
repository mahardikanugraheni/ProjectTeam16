import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk

window = tk.Tk()
window.title("BMI Calculator")
window.geometry('600x400')
window.configure(bg='#8FBC8F')

img = tk.PhotoImage(file='logologin.png')
img2= Image.open('logologin.png')
resize = img2.resize((200,200),Image.LANCZOS)
converted = ImageTk.PhotoImage(resize)
a= tk.Label(window,image=converted,border=0,bg='#E9967A')
a.pack()


def halaman_SignUp():
    halaman_SignUp = tk.Toplevel(window)
    halaman_SignUp.title("Menu Sign Up")
    halaman_SignUp.geometry('600x400')
    label1 = tk.Label(halaman_SignUp, text="Ini adalah Menu Sign Up", bg ='white',fg='black')
    label1.pack(expand=True,padx=50,pady=30)
    user = Entry(halaman_SignUp,width=25,fg='black',border=0,bg='white',font=('Arial',12))
    user.pack(padx=20,pady=30)
    user.insert(0,'Username')
    Frame(halaman_SignUp,width=295,height=2,bg='white').place(x=25,y=107)
    heading.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    window.close



def halaman_SignIn():
    halaman_SignIn = tk.Toplevel(window)
    halaman_SignIn.title("Menu Sign In")
    halaman_SignIn.geometry('600x400')
    label = tk.Label(halaman_SignIn,text="Ini adalah Menu Sign In", bg='white',fg='black')
    label.pack(expand=True,padx=50,pady=30)
    heading.pack_forget()
    button1.pack_forget()
    button2.pack_forget()


heading = Label(window, text='Selamat Datang di BMI & BMR Calculator', fg="white", bg="#8FBC8F",font=('Arial',18,'bold'))
heading.pack(expand=True,padx=50,pady=30)
button1 = tk.Button(window,text="Sign Up", bg='white',fg='black',command=halaman_SignUp)
button1.pack(expand=True,ipadx=30,ipady=10,pady=30,side='right' )
button2 = tk.Button(window,text="Log In", bg='white',fg='black',command=halaman_SignIn)
button2.pack(expand=True,ipadx=30,ipady=10,pady=30,side='left')

window.mainloop()
