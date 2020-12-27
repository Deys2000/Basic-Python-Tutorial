print('''python program #17
Hashir - May 30 2018
This program upgrades program #16 to take input from user
''')

import sys
moon_gravity = 9.81*.165

def moon_weight():
    print("What is your initial mass?")
    initial_mass = int(sys.stdin.readline())
    print("How may kilos does you mass increase each year?")
    mass_increase = int(sys.stdin.readline())
    print("How many years will this occur")
    years = int(sys.stdin.readline())

    for year in range(0,years+1):
        current_mass = initial_mass + (mass_increase*year)
        print("Year %s: %skg" %(year,current_mass*moon_gravity))


moon_weight()
