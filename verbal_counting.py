# это прога для того, чтобы научиться быстро считать
import math
import random
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
		print ("Press F to stop")
		continue
	answer = int(answer)	
	if answer == c: 
		continue
	else:
		print ("wrong! \nwrong! \nwrong!\n==========================")
		print ("correct answer is ", c)
		print ("==========================")
		continue

	

