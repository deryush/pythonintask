# задача 7. Вариант 1.
# Напишите программу, которая бы при запуске случайным образом отображала
# название одного из семи чудес светаю
# Болатукаев.А.З
# 21.03.2017
import random
sput =  ["Атос", "Портос", "Арамис"]
rsput = random.choice(sput)
score = 10
psput = ""
while psput != rsput:
	psput = input("Назовите одиного из трех товарищей д'Артаньяна: ")
	if psput == rsput:
		print("\nХорооош!")
		print("У вас", score,"баллов.")

	else:
		score-=5
		print("\nНе правильно((\nПопробуйте еще раз\n\n")
input("\n\nНажмите Enter для выхода")