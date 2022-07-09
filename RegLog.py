import hashlib
import pickle


data_password = {}


def registration():
	while True:
		login = input('Введите логин: ')
		if login in data_password:
			print('Логин существует, придумайте новый')
		else:
			break
	while True:
		password_1 = hashlib.md5(pickle.dumps(input('Введите пароль: '))).hexdigest()
		password_2 = hashlib.md5(pickle.dumps(input('Введите пароль повторно: '))).hexdigest()
		if password_1 == password_2:
			print('Вы успешно зарегестрировались!')
			break
		else:
			print('Пароли не совпадают, введите ещё раз')
	password_data = password_1
	data_password[login] = password_data	


def login():
	login_input = input('Введите логин: ')
	password_input = hashlib.md5(pickle.dumps(input('Введите пароль: '))).hexdigest()

	try:
		if data_password[login_input] == password_input:
			print('Вы успешно авторизовались!')
			pass
		else:
			print('Пароль неверный!')
			pass
	except Exception:
		print('Пользователь не существует')

