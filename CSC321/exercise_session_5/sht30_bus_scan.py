from sht3x import SHT3X
from machine import I2C, Pin

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

def scan():
    """
    Visual representation of the available I2C addresses
    """
    print('Scanning the I2C bus')
    addresses = i2c.scan()
    print(addresses)
    hexVals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    postHexVals = ['00', '10', '20', '30', '40', '50', '60', '70', '90', 'a0', 'b0', 'c0', 'd0', 'e0', 'f0']
    print('  ', '  '.join(hexVals))
    
    for i in range(len(postHexVals)):
        line = []
        for j in range(len(hexVals)):
            _hexa = '0x' + postHexVals[i][0] + hexVals[j]
            if int(_hexa, 16) in addresses:
                line.append(_hexa[-2:])
            else:
                line.append('__')
        print(postHexVals[i], ' '.join(line))

    
scan()