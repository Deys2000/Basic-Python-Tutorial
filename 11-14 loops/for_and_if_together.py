print('''python program #12
Hashir - May 29 2018
This program increments in 2 till your age, even or odd depends on age as well
''')

age = 23
start = 1
if age%2 == 0:
    start = 2
for x in range(start,age+1,2):
    print(x)
