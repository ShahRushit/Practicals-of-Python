fh = open("sample.txt","r")
line = fh.read()
pos = fh.tell()
print(line)
print("Current Position : ", pos)
