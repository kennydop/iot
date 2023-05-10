import array
import dht
from dht11Raw import dht11ReadRaw
from machine import Pin
from time import sleep
import uos

pin = 22
d = dht.DHT11(Pin(22))

def build_final_bin_str(data_bin):
    # read 6 consecutive 1's as 1 but 0 if less than 6
    count = 0
    final_bin_data = ''
    for c in data_bin:
        if c == '1':
            count += 1
        else:
            if count > 6:
                final_bin_data += '1'
            elif count > 0 and count < 7:
                final_bin_data += '0'
            count = 0
    print('\n\nfinal binary string:', final_bin_data, '|| length:', len(final_bin_data))
    return final_bin_data

def verify(bin_str):
    intg_hum = int(bin_str[:8], 2)
    dec_hum = int(bin_str[8:16], 2)
    intg_tempt = int(bin_str[16:24], 2)
    dec_tempt = int(bin_str[24:32], 2)
    check_sum = int(bin_str[32:], 2)
    return check_sum == (intg_hum + dec_hum + intg_tempt + dec_tempt)

def humidity(bin_str):
    intg_hum = int(bin_str[:8], 2)
    dec_hum = int(bin_str[8:16], 2)
    return '{}.{}'.format(intg_hum, dec_hum)

def temperature(bin_str):
    intg_tempt = int(bin_str[16:24], 2)
    dec_tempt = int(bin_str[24:32], 2)
    return '{}.{}'.format(intg_tempt, dec_tempt)
    

def read_data():
#     while True:
        dht11Data = array.array("I",[0]*32)
        dht11ReadRaw(Pin(pin), dht11Data)
        dirs = uos.listdir()
        data_bin = ''
        if 'data' in dirs:
#             try:
                dht11_file = open ("data/dht11.txt", "w")
                dht11_hex_file = open ("data/dht11_hex.txt", "w")
                dht11_bin_file = open ("data/dht11_bin.txt", "w")
                
                # build bin and hex strings
                for i in dht11Data:
                    hexa = hex(i)
                    dht11_file.write("%s\n" % i)
                    dht11_hex_file.write("%s\n" % hexa)
                    bin_str = bin(int(hexa, 16))[2:]
                    bin_str = ('0' * (32 - len(bin_str))) + bin_str
                    data_bin += bin_str
                fs = build_final_bin_str(data_bin)
                print('\nis data is correct:', verify(fs))
                print('humidity:', humidity(fs))
                print('temperature:', temperature(fs))
                                
#             except:
#                 uos.mkdir("data")
#                 read_data()
        else:
            uos.mkdir("data")
#             read_data()
#         sleep(30)

sleep(2)
read_data()
d.measure()

print('\ndht humidity:', d.humidity())
print('dht temperature:', d.temperature())