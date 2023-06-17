import tkinter as tk
from PIL import Image,ImageTk
import fixbisa as fb

window = tk.Tk()
window.title("BMI Calculator")
window.state('zoomed')

bg = tk.PhotoImage(file='firstpage.png')
bg1=Image.open('firstpage.png')
resize = bg1.resize((1300,650),Image.LANCZOS)
firstpage= ImageTk.PhotoImage(resize)

bg = tk.PhotoImage(file='bglogin.png')
bg2=Image.open('bglogin.png')
resize = bg2.resize((1300,650),Image.LANCZOS)
bgloginpage= ImageTk.PhotoImage(resize)

bg = tk.PhotoImage(file='bgsignup.png')
bg3=Image.open('bgsignup.png')
resize = bg3.resize((1300,650),Image.LANCZOS)
bgsignuppage= ImageTk.PhotoImage(resize)

bg = tk.PhotoImage(file='awalkalku.png')
bg4=Image.open('awalkalku.png')
resize = bg4.resize((1300,650),Image.LANCZOS)
awalkalkupage= ImageTk.PhotoImage(resize)

bg = tk.PhotoImage(file='kalkulator.png')
bg5=Image.open('kalkulator.png')
resize = bg5.resize((1300,650),Image.LANCZOS)
bmibmr= ImageTk.PhotoImage(resize)

fb.awal(window,
        firstpage,
        bgloginpage,
        bgsignuppage,
        awalkalkupage,
        bmibmr)
window.mainloop()