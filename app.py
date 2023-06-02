from tkinter import *
from tkinter import messagebox

def reset_entry():
    age.delete(0,'end')
    height.delete(0,'end')
    weight.delete(0,'end')

def calculate_bmi():
    kg = int(weight.get())
    m = int(height.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI_Calculator', f'BMI = {bmi} is Underweight')
    elif (bmi>18.5) and (bmi<24.9):
        messagebox.showinfo('BMI_Calculator', f'BMI = {bmi} is Normal')
    elif (bmi>24.9) and (bmi <29.9):
        messagebox.showinfo('BMI_Calculator', f'BMI ={bmi} is Overweight, harus olahraga dan diet')
    else:
        messagebox.showinfo('BMI_Calculator', f'BMI = {bmi} is Obesity')

ws = Tk()
ws.title('BMI_Calculator')
ws.geometry('400x300')
ws.config(bg='#6495ED')

var = IntVar()

frame = Frame(
    ws,
    padx=10,
    pady=10
)
frame.pack(expand=True)
    
age_lb = Label(
    frame,
    text="Enter Age (2-120)"
)
age_lb.grid(row=1,column=1)

age = Entry(
    frame,
)
age.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender'
)
gen_lb.grid(row=2,column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb =Radiobutton(
    frame2,
    text = 'Male',
    variable = var,
    value = 1
)
male_rb.pack(side=LEFT)

female_rb =Radiobutton(
    frame2,
    text = 'Female',
    variable = var,
    value = 2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Enter Height (cm)"
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)",
)
weight_lb.grid(row=4, column=1)

height = Entry(
    frame,
)
height.grid(row=3, column=2, pady=5)

weight = Entry(
    frame,
)
weight.grid(row=4,column=2,pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5,columnspan=3,pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn= Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)


ws.mainloop()