print('''python program #16
Hashir - May 30 2018
This program upgrades the last program to change parameters
''')

def moon_weight(mass,mass_increase,years):
    moon_gravity = 9.81*.165
    for year in range(0,years+1):
        current_mass = mass + (mass_increase*year)
        print("Year %s: %skg" %(year,current_mass*moon_gravity))


moon_weight(30, 2, 20)
