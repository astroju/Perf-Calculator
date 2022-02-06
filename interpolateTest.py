import numpy as np
import Saab340 as SF34
import matplotlib.pyplot as plt

def test_rwyLength():
    value_x = np.linspace(0, 6, 60)

    plt.plot(value_x, SF34.rwyLength(value_x,0,0))
    plt.xlabel('value')
    plt.ylabel('rwy length')

    plt.show()

def test_valueWeight_15OffOff_weight():
    #value_x = np.linspace(0, 6, 60)
    value_weight = np.linspace(20000, 29000, 11)

    #print(value_x)
    print(value_weight)
    print(SF34.valueWeight_15OffOff(1,value_weight))

    plt.plot(value_weight, SF34.valueWeight_15OffOff(1,value_weight))

    plt.xlabel('weight')
    plt.ylabel('value')

    plt.show()

def main():
    test_rwyLength()
    test_valueWeight_15OffOff_weight()

if __name__ == '__main__':
    main()