def odd_even(no):
	if no % 2 == 0:
		return "even"
	else:
		return "Odd"
num = int(input("Enter Number"))
print(odd_even(num))