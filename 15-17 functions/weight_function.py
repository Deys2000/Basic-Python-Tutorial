print('''python program #15
Hashir - May 30 2018
This program is turning the last program into a function
''')

def moon_weight(mass, moon_gravity):
    for year in range(0,16):
        current_mass = mass + year
        print("Year %s: %skg" %(year,current_mass*moon_gravity))


moon_weight(30, 9.81*.165)
