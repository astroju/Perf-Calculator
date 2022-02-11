# Current thinking:
#   Set default temp 15C, elev 0, winds calm, weight 22000 lbs, flaps 15, AI and ECS off.
#   These values can then be changed by entering one letter, then usre enters value.
#   Computation is then run using those values. 
#   QNH computation still needs adding
#   Consider adding ability to read a METAR, perhaps from SimBrief


import numpy as np
import math
from scipy import interpolate

def oatAltValue_15OffOff(oat,alt):
    
    oat_range_x = np.arange(-20,41,20)
    alt_range_y = np.arange(0,8001,4000)

    midvals = np.array(
            #alt
        [[0.5, 0.8, 1.3]
        ,[0.6, 1.1, 1.7] #oat
        ,[0.8, 1.4, 2.6]
        ,[1.1, 2.2, 4.4]])

    fnc = interpolate.RectBivariateSpline(oat_range_x, alt_range_y, midvals,ky=2)

    return fnc(oat,alt)

def valueWeight_15OffOff(value,weight):

    weight_range_x = np.arange(20000, 29001, 2000)
    val_range_y = np.array([0.2, 1.0, 1.8, 2.5, 3.3, 4.0])

    midvals = np.array(
            #val
        [[0.2, 0.9, 1.4, 1.8, 2.2, 2.7]
        ,[0.2, 1.0, 1.8, 2.5, 3.3, 4.0] #weight
        ,[0.4, 1.4, 2.4, 3.6, 4.7, 5.9]
        ,[0.6, 2.0, 3.5, 4.0, 6.0, 6.0]
        ,[0.8, 2.8, 4.6, 6.0, 6.0, 6.0]])

    fnc = interpolate.RectBivariateSpline(weight_range_x, val_range_y, midvals)

    return fnc(weight,value)

def rwyLength15OffOff(value, headwind, slope):

    headwind_range_x = np.array([-10,-5,0,15,30])
    val_range_y = np.array([0.0,0.5,1.0,2.0,3.0,4.0,5.0,5.5])

    midvals = np.array(
            #val
        [[0.6, 1.2, 1.80, 3.0, 4.10, 5.2, 6.0, 6.00]
        ,[0.3, 0.6, 1.40, 2.5, 3.55, 4.6, 5.8, 6.00]
        ,[0.0, 0.5, 1.00, 2.0, 3.00, 4.0, 5.0, 5.50] #headwind
        ,[0.0, 0.0, 0.75, 1.7, 2.60, 3.6, 4.5, 5.00]   
        ,[0.0, 0.0, 0.50, 1.4, 2.10, 3.2, 4.1, 4.60]])

    fnc = interpolate.RectBivariateSpline(headwind_range_x, val_range_y, midvals, kx = 1)

    value = fnc(headwind,value)

    return 2000 + value * 1000


def takeoff_flaps15_ecsOff_aiOff_weight(oat,alt,weight, headwind, slope):
    return rwyLength15OffOff( valueWeight_15OffOff( oatAltValue_15OffOff(oat, alt), weight), headwind, slope)


def oatAltValue_0OffOff(oat,alt):
    
    oat_range_x = np.arange(-20,41,20)
    alt_range_y = np.arange(0,8001,4000)

    midvals = np.array(
            #alt
        [[0.5, 1.0, 1.7]
        ,[0.7, 1.3, 2.2] #oat
        ,[1.0, 1.8, 3.2]
        ,[1.4, 2.8, 4.9]])

    fnc = interpolate.RectBivariateSpline(oat_range_x, alt_range_y, midvals,ky=2)

    return fnc(oat,alt)

def valueWeight_0OffOff(value,weight):

    weight_range_x = np.arange(20000, 29001, 2000)
    val_range_y = np.arange(0.5, 5.1, 0.5) #array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])

    midvals = np.array(
            #val
        [[0.4, 0.6, 1.0, 1.4, 1.7, 2.1, 2.5, 2.8, 3.2, 3.4]
        ,[0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0] #weight
        ,[0.9, 1.6, 2.2, 2.8, 3.4, 4.1, 4.8, 5.5, 6.0, 6.0]
        ,[1.4, 2.2, 2.9, 3.6, 4.4, 5.4, 6.0, 6.0, 6.0, 6.0]
        ,[2.0, 2.8, 3.7, 4.6, 5.7, 6.0, 6.0, 6.0, 6.0, 6.0]])

    fnc = interpolate.RectBivariateSpline(weight_range_x, val_range_y, midvals, kx = 2, ky = 2)

    return fnc(weight,value)

def rwyLength0OffOff(value, headwind, slope):

    headwind_range_x = np.array([-10,-5,0,15,30])
    val_range_y = np.array([0.0,0.5,1.0,2.0,3.0,4.0, 4.75, 5.0,5.5])

    midvals = np.array(
            #val
        [[0.50, 1.20, 1.70, 3.10, 4.10, 5.20, 6.00, 6.00, 6.00]
        ,[0.25, 0.85, 1.35, 2.50, 3.55, 4.60, 5.38, 5.70, 6.00]
        ,[0.00, 0.50, 1.00, 2.00, 3.00, 4.00, 4.75, 5.00, 5.50] #headwind
        ,[0.00, 0.28, 0.75, 1.70, 2.65, 3.60, 4.33, 4.55, 5.05]   
        ,[0.00, 0.05, 0.50, 1.40, 2.30, 3.20, 3.90, 4.10, 4.60]])

    fnc = interpolate.RectBivariateSpline(headwind_range_x, val_range_y, midvals, kx = 1)

    value = fnc(headwind,value)

    return 2000 + value * 1000

def takeoff_flaps0_ecsOff_aiOff_weight(oat,alt,weight, headwind, slope):
    return rwyLength0OffOff( valueWeight_0OffOff( oatAltValue_0OffOff(oat, alt), weight), headwind, slope)

def main():
    flaps = '15'
    oat = 15
    alt = 0
    weight = 22000
    windDir = 0
    windSpeed = 0
    rwyDir = 0
    antiIce = False
    ecs = False 
    userInput = '' 

    while userInput.upper() != 'X':
        print(f'Temp {oat} deg C, elevation {alt} ft, weight {weight} lbs, flaps {flaps}, winds {windDir} at {windSpeed} knots, runway direction {rwyDir}, flaps {flaps}, anti-ice {antiIce}, ECS {ecs}' )
        headwind = windSpeed * math.cos((windDir - rwyDir) * math.pi / 180)
        
        if flaps == '15':
            rwyLength = takeoff_flaps15_ecsOff_aiOff_weight(oat,alt,weight, headwind, 0)[0][0]
        elif flaps == '0': 
            rwyLength = takeoff_flaps0_ecsOff_aiOff_weight(oat,alt,weight, headwind, 0)[0][0]
        print(f'Runway length {rwyLength:.0F} ft')
        print('Press F to change flaps; T to change temperature; E for elevation; W for weight; D for wind direction; S for wind speed; R for runway direction; X to exit.')

        userInput = input() 

        if userInput.upper() == 'F':
            if flaps == '0':
                flaps = '15'
            else:
                flaps = '0'

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