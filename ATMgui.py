
from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()

GUI.title('ATM')
GUI.geometry('500x300')

FONT=('TH SarabunPSK',20)

#ข้อมูลสมมติ
datas = {1000 : {'name':'accoun1','money':100000},2000:{'name':'accoun2','money':90000}}
########################################
tap = ttk.Notebook(GUI)

F2 = Frame(GUI)
F1 = Frame(GUI)

tap.pack(fill=BOTH,expand=1)
tap.add(F2,text='เช็คยอดเงิน')
tap.add(F1,text='ถอนเงิน')

#################################

def ton():
	key = int(code.get())
	g = int(mon1.get())
	global mons
	mons = datas[key]['money']
	if  g<=mons:
		mons = mons - g
		mo.set(f'ถอนเงินจำนวน {g:,d} บาท\nคุณมียอดเงินคงเหลือ {mons:,d} บาท')
	else:
		mo.set('คุณมีจำนวนเงินไม่เพียงพอที่จะถอน')

def check():
	n = int(num.get())
	mons = datas[n]['money']
	yen.set(f'คุณมียอดเงินคงเหลือในบัญชี {mons:,d} บาท')
###################หน้าถอนเงิน########################

mon1 = IntVar()
mo = IntVar()
code = IntVar()
mo.set(' ')

L1 = Label(F1,text='กรุณากรอกเลขบัญชี')
L1.pack(pady=10)

E1 = Entry(F1,textvariable=code)
E1.pack()

L2 =Label(F1,text='กรุณากรอกจำนวนเงินที่ต้องการถอน')
L2.pack(pady=10)

E2 = Entry(F1,textvariable=mon1)
E2.pack()

B2 = Button(F1,text='ถอน',command=ton)
B2.pack(pady=10)

Lr = Label(F1,textvariable=mo)
Lr.pack(pady=10)
####################หน้าเช็คยอดเงิน#########################

num = IntVar()
yen= StringVar()
yen.set(' ')

L3 = Label(F2,text='กรุณากรอกเลขบัญชี')
L3.pack(pady=10)

E3 = Entry(F2,textvariable=num)
E3.pack()

B3 = Button(F2,text='เช็คยอดเงิน',command=check)
B3.pack(pady=10)

Lr2 = Label(F2,textvariable=yen)
Lr2.pack(pady=10)



GUI.mainloop()