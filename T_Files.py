filepath = r'C:\Users\fan\Documents\file1.txt'

f = open(filepath, 'w')
f.write('Hello, ')  # append to the end of file
f.write('world')
f.close()

f = open(filepath, 'r')
print(f.read(4))
print(f.read())

f = open(filepath, 'w')
f.truncate(0)  # clear file
f.write('01234567890123456789')
f.seek(5)
f.write('Hello')
f.close()

f = open(filepath, 'r')
print(f.read())

f = open(filepath, 'r')
f.read(3)
f.read(2)
print(f.tell())

# try to change
