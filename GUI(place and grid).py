
from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('400x250')
GUI.title('my cal')

FONT = ('TH SarabunPSK',14)

v_width = StringVar()
v_long = StringVar()

L1 = Label(GUI,text='คำนวณหาพื้นที่สนามฟุตบอล',font=FONT)
L1.place(x=135,y=10)

im = PhotoImage(file='football.png').subsample(6)
im2 = PhotoImage(file='cat.png').subsample(4)
IM = Label(GUI,image=im)
IM.place(x=20,y=45)

f1 = Frame(GUI)
f1.place(x=220,y=60)

E1 = Entry(f1,textvariable=v_width,font=FONT)
E1.grid(column=0,row=0)

E2 = Entry(f1,textvariable=v_long,font=FONT)
E2.grid(column=0,row=1,pady=7)

def calc():
	w = int(v_width.get())
	l = int(v_long.get())
	cal = w*l
	print(cal)
	v_result.set('สนามมีพื้นที่ {:,d} ตร.ม. '.format(cal))

B1 = Button(f1,text='calculate',image=im2,command = calc)
B1.grid(column=0,row=2)

v_result = StringVar()
v_result.set('ผลลัพธ์')
re = Label(GUI,textvariable=v_result,font=FONT,foreground='red')
re.place(x=30,y=180)



GUI.mainloop()