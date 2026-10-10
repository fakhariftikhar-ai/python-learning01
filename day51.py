file = open("myfile.txt", "w")
file.write("Hello World")
file.close()

file = open("myfile.txt", "r")

print(file.tell())

file.seek(6)
print(file.read())
print(file.tell())

file.close()