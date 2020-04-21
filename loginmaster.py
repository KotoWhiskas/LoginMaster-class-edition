#!/usr/bin/env python3
import getpass
print("Введите конфигурацию программы. Убедитесь, что Вы правильно ввели, иначе программа не зарабоатет.")
cfg1 = input("Название файла и путь к нему(если не указывать путь то файл будет там где программа) - напр. <home/user/passw.txt>:  ")
cfg2 = input("запрещенные символы напр. </;\%]>  :   ")
cfg3 = input("минимальная и макс. длинна логина - <4-12> :  ")
cfg4 = input("'минимальная и макс. длинна пароля - <5-16> :  ")
class LoginSystem:
	flag = "" #Флаги на всеinput()
	flag1 = True #        случаи программы
	flag2 = "Теперь п"
	illegal = [] #Wait, that's illegal!
	minlognum = 0
	maxlognum = 0
	minpasswnum = 0
	maxpasswnum = 0
	answer_versplus = ["yes", "", "go", "да", "ага", "+", "da"]
	answer_verminus = ["no", "нет", "-", "net"]
	def __init__(self, stor, symbols, lognum, passwnum): #это для того, чтобы указать: хранилище и путь к ниму
		self.symbols = symbols
		self.stor = stor # способ сепарации данных и запрещенные символы, а также их макс количество
		for i in self.symbols:
			self.illegal.append(i)
		self.minlognum = int(lognum.split("-")[0])
		self.maxlognum = int(lognum.split("-")[1])
		self.minpasswnum = int(passwnum.split("-")[0])
		self.maxpasswnum = int(passwnum.split("-")[1])
	def register(self):
			while True:
				inf = input("Придумайте логин%s: " % self.flag)
				aflag = len(inf)
				if aflag < self.minlognum or aflag > self.maxlognum:
					print("Логин не должен быть короче %d символов или длиннее %d" % (self.minlognum, self.maxlognum))
					continue
				elif any([symbol in inf for symbol in self.illegal]):
					print("Вы ввели ник с запрещеными символами - '%s' " % ", ".join(map(str, self.illegal)))
					continue
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
					print("Допустимая длинна пароля - %d - %d" % (self.minpasswnum, self.maxpasswnum))
					continue
				else:
					inf3 = getpass.getpass("Подтвердите пароль: ")
					if inf2 == inf3:
						print("Успешно")
						break
					else:
						print("Пароли не совпадают")
						self.flag2 = "П"
						continue
			somefile = open(self.stor, "a+")
			somefile.write(inf + ":" + inf2 + ";")
			somefile.close()
logsys = LoginSystem(cfg1, cfg2, cfg3, cfg4)
logsys.register()
