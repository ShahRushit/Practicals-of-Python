hrs = input()
rate = input()

hrs = int(hrs)
rate = int(rate)

if hrs>10 :
	sum = 10*rate
	sum = sum + (((hrs-10)*rate)*2)
	print(sum)
else :
	print(hrs*rate)

