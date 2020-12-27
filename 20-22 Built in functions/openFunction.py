print('''python program #22
Hashir - May 30 2018
This program in an intro to opening files to get data and creating files
the first part of this code reads a file that was already created
the second part of the code creates a new copy of the file previously read
''')

old_file = open('c:\\Users\\aquadri\\test.txt')
contents_of_old_file = old_file.read()
print("--original file")
print(contents_of_old_file)

new_file = open('c:\\Users\\aquadri\\newtest.txt','w')
new_file.write(contents_of_old_file)
new_file.close()

new_file = open('c:\\Users\\aquadri\\newtest.txt')
contents_of_new_file = new_file.read()
print("")
print("--copied file")
print(contents_of_new_file)

