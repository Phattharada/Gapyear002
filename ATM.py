
money = 100000

print('กด 1 : ถอนเงิน')
print('กด 2 : เช็คยอดเงิน')
print('กด q : ยกเลิกการดำเนินรายการ')
print('---------------')
menu = input('กรุณาเลือกเมนู : ')

while menu != 'q':
	if menu == '1':
		print('- ถอนเงิน -')
		withdraw = int(input('กรุณากรอกจำนวนเงินที่ต้องการถอน: '))
		while withdraw > money:
			print('เงินในบัญชีไม่พอกุณากรอกยอดเงินให้ถูกต้อง')
			withdraw = int(input('กรุณากรอกจำวณเงิน : '))
		print('กรุณารับเงิน {} บาท'.format(withdraw))
		money = money - withdraw
		print('คุณมีเงินคงเหลือ {}  บาท'.format(money))

	elif menu == '2':
		print('ยอดเงินของุณคือ : {} บาท'.format(money))
	print('กด 1 : ถอนเงิน')
	print('กด 2 : เช็คยอดเงิน')
	print('กด q : ยกเลิกการดำเนินรายการ')
	menu = input('กรุณาเลือกเมนู : ')
