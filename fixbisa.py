import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk
import csv


window = Tk()
window.title("BMI Calculator")
window.state('zoomed')

bg = tk.PhotoImage(file='firstpage.png')
bg1=Image.open('firstpage.png')
resize = bg1.resize((1300,650),Image.LANCZOS)
converted1= ImageTk.PhotoImage(resize)

bg = tk.PhotoImage(file='bglogin.png')
bg2=Image.open('bglogin.png')
resize = bg2.resize((1300,650),Image.LANCZOS)
converted2= ImageTk.PhotoImage(resize)

bg = tk.PhotoImage(file='bgsignup.png')
bg3=Image.open('bgsignup.png')
resize = bg3.resize((1300,650),Image.LANCZOS)
converted3= ImageTk.PhotoImage(resize)

bg = tk.PhotoImage(file='awalkalku.png')
bg4=Image.open('awalkalku.png')
resize = bg4.resize((1300,650),Image.LANCZOS)
converted4= ImageTk.PhotoImage(resize)

bg = tk.PhotoImage(file='kalkulator.png')
bg5=Image.open('kalkulator.png')
resize = bg5.resize((1300,650),Image.LANCZOS)
converted5= ImageTk.PhotoImage(resize)
page_check=0

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
    frame1.pack(ipadx=1300,ipady=650)
    a= tk.Label(frame1,image=converted1,border=0)
    a.pack(fill=tk.BOTH,expand=tk.YES)
    button1 = tk.Button(a,text="Sign Up", bg='#fabb17',fg='white',border=0,font=('Arial',18),command=halaman_Signup)
    button1.place(x=495,y=450,relwidth=0.1)
    button2 = tk.Button(a,text="Log In", bg='#fabb17',fg='white',border=0,font=('Arial',18),command=halaman_SignIn)
    button2.place(x=650,y=450,relwidth=0.1)

def signin():
    username=username_entry.get()
    password=password_entry.get()
    
    with open('database.csv','r')as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            if row[1]==username and row[2]==password:
                messagebox.showinfo('sign in','Log In Berhasil')
                next_button = tk.Button(bglogin,text='Next', command=halaman_awal,bg='#fabb17',fg='white',border=0,font=('Arial',14))
                next_button.place(x=885,y=430,relwidth=0.1)
                return
        messagebox.showerror('invalid','Username atau Password Salah')


def halaman_SignIn():
    global frame2, page_check, username_entry, password_entry,bglogin
    frame1.pack_forget()
    page_check=2
    frame2=tk.LabelFrame(window)
    frame2.pack(ipadx=1300,ipady=650)
    bglogin= tk.Label(frame2,image=converted2,border=0)
    bglogin.pack(fill=tk.BOTH,expand=tk.YES)
    username_label = Label(bglogin,text="Username", fg="#94221e", bg="#f3e1d1",font=('The Seasons Light',18,'bold'))
    username_label.place(x=885,y=220)
    username_entry = tk.Entry(bglogin)
    username_entry.place(x=850,y=250,relwidth=0.15)
    password_label = Label(bglogin,text="Password", fg="#94221e", bg="#f3e1d1",font=('The Seasons Light',18,'bold'))
    password_label.place(x=885,y=290)
    password_entry = tk.Entry(frame2)
    password_entry.place(x=850,y=320,relwidth=0.15)
    login_button = tk.Button(bglogin,text="Login",command=signin,bg='#fabb17',fg='white',border=0,font=('Arial',14))
    login_button.place(x=885,y=370,relwidth=0.1)
    

def halaman_Signup():
    global frame3, page_check
    frame1.pack_forget()
    page_check=3
    frame3=tk.LabelFrame(window)
    frame3.pack(ipadx=1300,ipady=650)
    bgsignup= tk.Label(frame3,image=converted3,border=0)
    bgsignup.pack(fill=tk.BOTH,expand=tk.YES)
    def signup():
        name=name_entry.get()
        username=user1_entry.get()
        password=password1_entry.get()
        if name_entry.get()=='' or user1_entry.get()=='' or password1_entry.get()=='':
            messagebox.showerror('invalid','Mohon Isi Semua!')
        else:
            with open('database.csv','a',newline='')as file:
                csv_writer=csv.writer(file)
                csv_writer.writerow([name,username,password])
                messagebox.showinfo('Sign Up','Sign Up Berhasil')
    name_label = Label(bgsignup,text="Nama", fg="#94221e", bg="#f3e1d1",font=('Arial',18,'bold'))
    name_label.place(x=910,y=220)
    name_entry = tk.Entry(bgsignup)
    name_entry.place(x=850,y=250,relwidth=0.15)
    user1_label = Label(bgsignup,text="Username", fg="#94221e", bg="#f3e1d1",font=('Arial',18,'bold'))
    user1_label.place(x=885,y=290)
    user1_entry = tk.Entry(bgsignup)
    user1_entry.place(x=850,y=320,relwidth=0.15)
    password1_label = Label(bgsignup,text="Password", fg="#94221e", bg="#f3e1d1",font=('Arial',18,'bold'))
    password1_label.place(x=885,y=350)
    password1_entry = tk.Entry(bgsignup)
    password1_entry.place(x=850,y=380,relwidth=0.15)
    signup_button = tk.Button(bgsignup,text="SignUp",command=signup,bg='#fabb17',fg='white',border=0,font=('Arial',14))
    signup_button.place(x=883,y=440,relwidth=0.1)
    back_button = tk.Button(bgsignup,text="Back",command=awal,bg='#fabb17',fg='white',border=0,font=('Arial',14))
    back_button.place(x=883,y=500,relwidth=0.1)

def halaman_awal():
    global frame4,page_check
    frame2.pack_forget()
    page_check=4
    frame4=tk.LabelFrame(window)
    frame4.pack(ipadx=1300,ipady=650)
    frame4.configure(bg='#8FBC8F')
    bghal_awal= tk.Label(frame4,image=converted4,border=0)
    bghal_awal.pack(fill=tk.BOTH,expand=tk.YES)
    button1 = tk.Button(bghal_awal,text='BMI Calculator',command=open_bmi,bg='#fabb17',fg='white',border=0,font=('Helvetica',14))
    button1.place(x=450,y=350)
    button2 = tk.Button(bghal_awal,text='BMR Calculator',command=open_bmr,bg='#fabb17',fg='white',border=0,font=('Arial',14))
    button2.place(x=680,y=350)

def bmi_index(bmi):
    if bmi < 18.5:
        with open("olahraga_bmi.csv",'r') as file:
            csv_reader = csv.reader(file)
            data=list(csv_reader)

            selected_data = [ ]
            for row in data:
                selected_data.append((row[0],row[1],row[2]))
            message = ''
            for row in selected_data:
                message += ':'.join(row) + "\n"
            messagebox.showinfo(f'BMI = {bmi} is Underweight',message)
            
    elif (bmi>18.5) and (bmi<24.9):
        with open("olahraga_bmi.csv",'r') as file:
            csv_reader = csv.reader(file)
            data=list(csv_reader)

            selected_data = [ ]
            for row in data:
                selected_data.append((row[3],row[4],row[5]))
            message = ''
            for row in selected_data:
                message += ':'.join(row) + "\n"
            messagebox.showinfo(f'BMI = {bmi} is Normal',message)
        
    elif (bmi>24.9) and (bmi <29.9):
        with open("olahraga_bmi.csv",'r') as file:
            csv_reader = csv.reader(file)
            data=list(csv_reader)

            selected_data = [ ]
            for row in data:
                selected_data.append((row[6],row[7],row[8]))
            message = ''
            for row in selected_data:
                message += ':'.join(row) + "\n"
            messagebox.showinfo(f'BMI = {bmi} is Overweight',message)
  
    else:
        with open("olahraga_bmi.csv",'r') as file:
            csv_reader = csv.reader(file)
            data=list(csv_reader)

            selected_data = [ ]
            for row in data:
                selected_data.append((row[9],row[10],row[11]))
            message = ''
            for row in selected_data:
                message += ':'.join(row) + "\n"
            messagebox.showinfo(f'BMI = {bmi} is Obesity',message)
 
   
def reset_entry1():
    age_ent.delete(0,'end')
    height.delete(0,'end')
    weight.delete(0,'end')
    var = IntVar()

def calculate_bmi():
    kg = int(weight.get())
    m = int(height.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def open_bmi():
    global frame5, page_check,age_ent,height,weight,hasil_bmi
    frame4.pack_forget()
    page_check=5
    var=IntVar()
    frame5=tk.Label(window)
    frame5.pack(expand=True,ipadx=1920,ipady=1080)
    bgkalku= tk.Label(frame5,image=converted5,border=0)
    bgkalku.pack(fill=tk.BOTH,expand=tk.YES)
    age_lb=Label(bgkalku,text='Umur',font=('Arial',16),fg="#94221e",bg="#f3e1d1")
    age_lb.place(x=495,y=120)
    age_ent=Entry(bgkalku)
    age_ent.place(x=695,y=125)
    gen_lb=Label(bgkalku,text='Pilih Jenis Kelamin',fg="#94221e",bg="#f3e1d1",font=('Arial',14))
    gen_lb.place(x=495,y=180)
    male_rb=Radiobutton(bgkalku,text='Pria',variable=var,value=1,fg="#94221e",bg="#f3e1d1",font=('Arial',14))
    male_rb.place(x=665,y=182)
    female_rb=Radiobutton(bgkalku,text='Wanita',variable=var,value=2,fg="#94221e",bg="#f3e1d1",font=('Arial',14))
    female_rb.place(x=753,y=182)
    height_lb=Label(bgkalku,text='Tinggi Badan (cm)',bg="#f3e1d1",fg="#94221e",font=('Arial',16))
    height_lb.place(x=495,y=237)
    weight_lb=Label(bgkalku,text='Berat Badan (kg)',bg="#f3e1d1",fg="#94221e",font=('Arial',16))
    weight_lb.place(x=495,y=292)
    height=Entry(bgkalku)
    height.place(x=695,y=245)
    weight=Entry(bgkalku)
    weight.place(x=695,y=300)
    cal_btn=Button(bgkalku,text='Calculate',command=calculate_bmi,bg="#fabb17",border=1,fg='white',font=('Arial',14))
    cal_btn.place(x=499,y=380,relwidth=0.07)
    reset_btn=Button(bgkalku,text='Reset',command=reset_entry1,bg="#fabb17",border=1,fg='white',font=('Arial',14))
    reset_btn.place(x=600,y=380,relwidth=0.07)
    back_btn=Button(bgkalku,text='Back',bg="#fabb17",border=1,fg='white',font=('Arial',14),command=halaman_awal)
    back_btn.place(x=699,y=380,relwidth=0.07)

     
def hitung_bmr():
    berat_badan = float(input_berat.get())
    tinggi_badan = float(input_tinggi.get())
    umur = int(input_umur.get())
    gender = input_gender.get()

    if gender == "Pria":
        bmr = 66 + (13.75 * berat_badan) + (5 * tinggi_badan) - (6.75 * umur)
        with open("makanan_bmr.csv",'r') as file:
            csv_reader = csv.reader(file)
            data=list(csv_reader)

            selected_data = []
            for row in data:
                selected_data.append((row[0],row[1]))
            message = ''
            for row in selected_data:
                message += ':'.join(row) + "\n"
            messagebox.showinfo(f'BMR kamu adalah {bmr:.2f}',message)
    else:
        bmr = 655 + (9.56 * berat_badan) + (1.85 * tinggi_badan) - (4.68 * umur)
        with open("makanan_bmr.csv",'r') as file:
            csv_reader = csv.reader(file)
            data=list(csv_reader)

            selected_data = []
            for row in data:
                selected_data.append((row[2],row[3]))
            message = ''
            for row in selected_data:
                message += ':'.join(row) + "\n"
            messagebox.showinfo(f'BMR kamu adalah {bmr:.2f}',message)

def reset_entry():
    input_berat.delete(0,'end')
    input_tinggi.delete(0,'end')
    input_umur.delete(0,'end')
    input_gender.delete(0,'end')
    var = IntVar()

def open_bmr():
    global frame6,page_check,input_berat,input_tinggi, input_umur,input_gender,hasil_bmr
    frame4.pack_forget()
    page_check=6
    frame6=tk.Label(window)
    frame6.pack(expand=True,ipadx=600,ipady=400)
    bgkalku2= tk.Label(frame6,image=converted5,border=0)
    bgkalku2.pack(fill=tk.BOTH,expand=tk.YES)
    label_berat=Label(bgkalku2,text='Berat Badan (kg)',bg='#f3e1d1',fg='#94221e',font=('Arial',18))
    label_berat.place(x=495,y=120)
    input_berat=Entry(bgkalku2)
    input_berat.place(x=710,y=125)
    label_tinggi = Label(bgkalku2, text="Tinggi Badan (cm)",bg='#f3e1d1',fg='#94221e',font=('Arial',18))
    label_tinggi.place(x=495,y=180)
    input_tinggi = Entry(bgkalku2)
    input_tinggi.place(x=710,y=184)
    label_umur = Label(bgkalku2, text="Umur",bg='#f3e1d1',fg='#94221e',font=('Arial',18))
    label_umur.place(x=495,y=237)
    input_umur = Entry(bgkalku2)
    input_umur.place(x=710,y=245)
    label_gender = Label(bgkalku2, text="Jenis Kelamin",bg='#f3e1d1',fg='#94221e',font=('Arial',18))
    label_gender.place(x=495,y=292)
    input_gender = Entry(bgkalku2)
    input_gender.place(x=710,y=300)
    tombol_hitung = Button(bgkalku2, text="Hitung BMR", command=hitung_bmr,fg='white',bg='#fabb17',font=('Arial',14))
    tombol_hitung.place(x=690,y=380)    
    reset_btn=Button(bgkalku2,text='Reset',command=reset_entry,bg="#fabb17",border=1,fg='white',font=('Arial',14))
    reset_btn.place(x=495,y=380)

    
awal()
window.mainloop()
