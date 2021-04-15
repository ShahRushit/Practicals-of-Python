def Big(no1,no2,no3):
	if no1==no2 and no1 == no3:
		print("All are same")
	elif no1>no2 and no1>no3:
		return no1
	elif no2>no3 and no2>no1:
		return no2
	return no3
num1 = int(input("Enter 1st no:"))
num2 = int(input("Enter 2nd no:"))
num3 = int(input("Enter 3rd no:"))
print(Big(num1,num2,num3))
