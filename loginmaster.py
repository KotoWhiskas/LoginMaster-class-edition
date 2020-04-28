#!/usr/bin/env python3
import os
import getpass
print("Введите конфигурацию программы. Чтобы загрузить базовые значения, напишите recent в консоль")
tess = input('')
def printcl(text):
	print(text)
	os.system('clear')
def inputcl(text):
	os.system('clear')
	return input(text)
if tess == "recent":
	cfg1 = "base.txt"
	cfg2 = "%]/][;:"
	cfg3 = "3-12"
	cfg4 = '2-20'
if tess == '':
	cfg1 = inputcl("Название файла и путь к нему(если не указывать путь то файл будет там где программа) - напр. <home/user/passw.txt>:  ")
	cfg2 = inputcl("запрещенные символы напр. </;%]>  :   ")
	cfg3 = inputcl("минимальная и макс. длинна логина - <4-12> :  ")
	cfg4 = inputcl("'минимальная и макс. длинна пароля - <5-16> :  ")
class LoginSystem:
	flag = "" #Флаги на все
	flag1 = True #        случаи программы
	flag2 = "Теперь п"
	illegal = [] #Wait, that's illegal!
	minlognum = 0
	maxlognum = 0
	minpasswnum = 0
	maxpasswnum = 0
	answer_versplus = ["yes", "", "go", "да", "ага", "+", "da", 'ok', 'ок']
	answer_verminus = ["no", "нет", "-", "net"]
	def __init__(self, stor, symbols, lognum, passwnum): #это для того, чтобы указать: хранилище и путь к ниму
		self.symbols = symbols
		self.stor = stor 
		for i in self.symbols:
			self.illegal.append(i)
		self.illegal = sorted(list(set(self.illegal)), key=self.illegal.index)
		self.minlognum = int(lognum.split("-")[0])
		self.maxlognum = int(lognum.split("-")[1])
		self.minpasswnum = int(passwnum.split("-")[0])
		self.maxpasswnum = int(passwnum.split("-")[1])
		if all([self.minlognum > self.maxlognum, self.minpasswnum > self.maxpasswnum]):
			raise
		test = open(self.stor, 'a+')
		test.close()
		del test
	def register(self):
			somefile = open(self.stor, "r+")
			self.flag = ''
			myfile = somefile.read()
			while True:
				inf = input("Придумайте логин%s: " % self.flag)
				aflag = len(inf)
				if aflag < self.minlognum or aflag > self.maxlognum:
					printcl("Логин не должен быть короче %d символов или длиннее %d" % (self.minlognum, self.maxlognum))
				elif any([symbol in inf for symbol in self.illegal]):
					printcl("Вы ввели ник с запрещеными символами - '%s' " % ", ".join(self.illegal))
				elif somefile.read() != '':
					if aflag in dict(x.split(":") for x in myfile.split(";")):
						printcl("Такой никнейм уже занят") 
				else:
					lel = input("Ваш логин - %s. Вы подтверждаете (Да/Нет)? : " % inf)
					if lel.lower() in self.answer_versplus:
						break
					elif lel.lower() in self.answer_verminus:
						self.flag = " еще раз"
			while True:
				inf2 = getpass.getpass("%sридумайте пароль: " % self.flag2)
				aflag = len(inf2)
				if aflag < self.minpasswnum or aflag > self.maxpasswnum:
					printcl("Допустимая длинна пароля - %d - %d" % (self.minpasswnum, self.maxpasswnum))
					continue
				else:
					inf3 = getpass.getpass("Подтвердите пароль: ")
					if inf2 == inf3:
						printcl("Успешно")
						break
					else:
						printcl("Пароли не совпадают")
						self.flag2 = "П"
						continue
			somefile.write((lambda x: '' if x == '' else ';')(somefile.seek(0).read()) + inf + ":" + inf2)
			somefile.close()
	def login(self):
		while True:
			self.flag = ''
			inf = inputcl("Введите логин%s: " % self.flag)
			inf2 = getpass.getpass("Введите пароль: ")
			astor = open(self.stor, 'r')
			if (inf, inf2) in dict(x.split(':') for x in astor.read().split(';')):
				printcl('Добро поажаловать!')
				break
			else:
				printcl('Неправильный логин или пароль')
				self.flag = ' еще раз'
while True:
	try:
		get = LoginSystem(cfg1, cfg2, cfg3, cfg4)
	except:
		cfg1 = inputcl("Введите ПРАВИЛЬНЫЕ аргументы (как в примере) \n Название файла и путь к нему(если не указывать путь то файл будет там где программа) - напр. <home/user/passw.txt>:  ")
		cfg2 = inputcl("запрещенные символы напр. </;%]>  :   ")
		cfg3 = inputcl("минимальная и макс. длинна логина - <4-12> :  ")
		cfg4 = inputcl("'минимальная и макс. длинна пароля - <5-16> :  ")
	else:
		break
get = LoginSystem(cfg1, cfg2, cfg3, cfg4)
get.register()
get.login()
