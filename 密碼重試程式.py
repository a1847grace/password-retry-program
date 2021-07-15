#這是一個密碼輸入程式
password = 'a123456'
x = 2
enter_password = input('請輸入密碼')
while enter_password != password:
	print ('密碼錯誤')
	print ('您還可以輸入', x,'次') 
	if enter_password != password:
		if x == 0:
			print ('密碼錯誤三次，系統將自動關閉')
			SystemExit
			break
		else:
			x = x - 1
			enter_password = input('請輸入密碼')
if enter_password == password:
	print ('密碼正確，成功登入系統')