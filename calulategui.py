from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()

GUI.title('ชื่อ')
GUI.geometry('600x600')

FONT=('TH SarabunPSK',20)

############################################
def add():
	messagebox.showinfo('การบวก','a + b = ?')

def plus():
	ta = valuel.get()
	sa = valuel2.get()
	res = ta + sa 
	r.set(f'ผลบวก = {res:,d}')

def cir():
	R = valuel3.get()
	pt = 3.14*(R**2)
	r2.set(f'พื้นที่วงกลม= {pt:,.2f}')

####################################
Tap = ttk.Notebook(GUI)

f1 = Frame(Tap)
f2 = Frame(Tap)

Tap.pack(fill=BOTH,expand=1)
Tap.add(f1,text='plus')
Tap.add(f2,text='circle')
###################################
def gui2():
	GUI2 = Toplevel()
	GUI2.title('ชื่อ2')
	GUI2.geometry('600x600')

	L1=Label(GUI2,text='ดีจ้า',font=FONT)
	L1.pack()

	GUI.mainloop()

####################################

menubar =Menu(GUI)
GUI.config(menu=menubar)

file = Menu(menubar,tearoff=0)
file.add_command(label='newfile',command=gui2)
file.add_command(label='close',command=GUI.quit)
menubar.add_cascade(label='File',menu=file)

cal = Menu(menubar,tearoff=0)
cal.add_command(label='บวก',command=add)
cal.add_command(label='ลบ')
cal.add_command(label='คูณ')
cal.add_command(label='หาร')
menubar.add_cascade(label='calculate',menu=cal)

#############################################3
L1 = Label(f1,text='yo!',font=FONT)
L1.pack()

valuel = IntVar()
valuel2 = IntVar()
r =IntVar()
r.set('------------------')

E1 = ttk.Entry(f1,textvariable=valuel,font=FONT)
E1.pack(anchor=S,pady=20,ipady=20)

E2 = ttk.Entry(f1,textvariable=valuel2,font=FONT)
E2.pack(ipady=20)

B1=ttk.Button(f1,text='กดสิ',command=plus)
B1.pack(pady=20)

Lr = Label(f1,textvariabl=r,foreground='red',font=FONT)
Lr.pack()
#########################################
L2 = Label(f2,text='circle!',font=FONT)
L2.pack()

valuel3 = DoubleVar()
r2 =DoubleVar()
r2.set('------------------')

E3 = ttk.Entry(f2,textvariable=valuel3,font=FONT)
E3.pack(anchor=S,pady=20,ipady=20)

B2=ttk.Button(f2,text='กดสิ',command=cir)
B2.pack(pady=20)

Lr2 = Label(f2,textvariabl=r2,foreground='red',font=FONT)
Lr2.pack()
##############################################3

GUI.mainloop()
