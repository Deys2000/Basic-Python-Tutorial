print('''python program #14
Hashir - May 30 2018
This program will get your weight on the moon as your mass increases by a kilo each year
''')

gravity_earth = 9.81
gravity_moon = gravity_earth*.165
initial_mass = 30
mass = None

for year in range(0,15):
    mass = initial_mass + year
    print("Year %s: %skg" %(year+1,mass*gravity_moon))
