# def fibonaci(n):
# 	n = int(n)
# 	if n <= 1 :
# 		return n
# 	return fibonaci(int(n) – 1) + fibonaci(int(n) – 2)

# print(fibonaci(5))
n = int(input("Enter Number : "))
f = [0,1]

while len(f)<n:
	f.append(0)
print(f)
for i in range(2,n):
		f[i] = f[i-1]+f[i-2]
	# f[i].append(f[i-1] + f[i-2])
	# f[i].append(f[i-1])
	
	# print(f[i])
print(f)
