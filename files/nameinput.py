f = open('nameloc.txt', 'w')
name = raw_input('What is your name? ')
print(name)
f.write(name)
location = raw_input('Where do you live? ')
print(location)
f.write(location)
f.close()