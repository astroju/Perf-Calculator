# Current thinking:
#   Set default temp 15C, elev 0, winds calm, weight 22000 lbs, flaps 15, AI and ECS off.
#   These values can then be changed by entering one letter, then usre enters value.
#   Computation is then run using those values. 
#   Consider adding ability to read a METAR, perhaps from SimBrief

import Saab340 as SF34
import numpy as np
import matplotlib.pyplot as plt
import math 

def main():
    oat = 15
    alt = 0
    weight = 22000
    flaps = 15
    windDir = 0
    windSpeed = 0
    rwyDir = 0
    antiIce = False
    ecs = False 
    userInput = '' 

    while userInput.upper() != 'X':
        print(f'Temp {oat} deg C, elevation {alt} ft, weight {weight} lbs, flaps {flaps}, winds {windDir} at {windSpeed} knots, runway direction {rwyDir}, anti-ice {antiIce}, ECS {ecs}' )
        headwind = windSpeed * math.cos((windDir - rwyDir) * math.pi / 180)
        rwyLength = SF34.takeoff_flaps15_ecsOff_aiOff_weight(oat,alt,weight, headwind, 0)[0][0]
        print(f'Runway length {rwyLength:.0F} ft')
        print('Press T to change temperature; E for elevation; W for weight; D for wind direction; S for wind speed; R for runway direction; X to exit.')

        userInput = input() 

        if userInput.upper() == 'T':
            userInput = input('Enter temperature in Celsius\n')
            if userInput.isnumeric():
                oat = float(userInput)
            else:
                print('Entered temperature is not a numeric value.')
                
        elif userInput.upper() == 'E':
            userInput = input('Enter elevation in ft\n')
            if userInput.isnumeric():
                alt = float(userInput)
            else:
                print('Entered elevation is not a numeric value.')

        elif userInput.upper() == 'W':
            userInput = input('Enter weight in lbs\n')
            if userInput.isnumeric():
                weight = float(userInput)
            else:
                print('Entered weight is not a numeric value.')

        elif userInput.upper() == 'D':
            userInput = input('Enter wind direction\n')
            if userInput.isnumeric():
                windDir = float(userInput)
            else:
                print('Entered wind direction is not a numeric value.') 

        elif userInput.upper() == 'S':
            userInput = input('Enter wind speed\n')
            if userInput.isnumeric():
                windSpeed = float(userInput)
            else:
                print('Entered wind speed is not a numeric value.') 

        elif userInput.upper() == 'R':
            userInput = input('Enter runway direction\n')
            if userInput.isnumeric():
                rwyDir = float(userInput)
            else:
                print('Entered runway direction is not a numeric value.') 

if __name__ == '__main__':
    main()