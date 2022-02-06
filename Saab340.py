import numpy as np
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

def rwyLength(value, headwind, slope):
    return 2000 + value * 1000


def takeoff_flaps15_ecsOff_aiOff_weight(oat,alt,weight, headwind, slope):
    return rwyLength( valueWeight_15OffOff( oatAltValue_15OffOff(oat, alt), weight), headwind, slope)

