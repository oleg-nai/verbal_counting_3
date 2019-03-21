# это прога для того, чтобы научиться быстро считать
import random
import math
import sys

def f_2_to_2_read():
	print("Press F to stop")		
	while True:
		a = random.randint(10,99)
		b = random.randint(10,99)
		print (a, "+", b)
		c = a + b
		answer = input("answer: ")
		print ("________________________")		
		if answer == 'f':
			break
		else:
			answer = int(answer)	
			if answer == c: 
				continue
			else:
				print ("wrong! \nwrong! \nwrong!\n==========================")
				print ("correct answer is ", c)
				print ("==========================")
				continue


def f_2_to_2_subtract():
	print("Press F to stop")
	while True:
		a = random.randint(10,99)
		b = random.randint(10,99)
		if a < b: 
			a = random.randint(10,99)
			b = random.randint(10,99)
		print (a, "-", b)
		c = a - b
		answer = input("answer: ")
		print ("________________________")		
		if answer == 'f':
			break
		else:
			continue
		answer = int(answer)	
		if answer == c: 
			continue
		else:
			print ("wrong! \nwrong! \nwrong!\n==========================")
			print ("correct answer is ", c)
			print ("==========================")
			continue


def kind_of_game():
	print ("Great! Do you like read or subtract?")
	asnwer_2 = int(input("1-read, 2-subtract: "))
	while True:
		if asnwer_2 == 1: 
			f_2_to_2_read()
		elif asnwer_2 == 2: 
			f_2_to_2_subtract() 
		else:
			print("Please, write correct answer")
			continue

print ("Hi! Would you like to count?")
asnwer_1 = int(input("1-yes, 2-no: "))
while True:
	if asnwer_1 == 1:
		kind_of_game()
	elif asnwer_1 == 2:
		sys.exit
	else:
		print("Please, write correct answer")
		continue

