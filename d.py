counter = 0
def calc(a,b):
	c = 0
	global counter
	counter += 1
	if b==3 :
		return (a*a*a)
	else :
		c = calc(a,b//3)
		return (c*c*c)
calc(4,81)
print(counter)
