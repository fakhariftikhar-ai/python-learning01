# Writing to a file
file = open("myfile.txt", "w")
file.write("Hello World!")
file.close()

# Reading from a file
file = open("myfile.txt", "r")
print(file.read())
file.close()