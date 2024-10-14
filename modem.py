#socat -d -d pty pty
#import serial
import hayes
import petscii
from machine import UART
#import wifi
import time

petscii = petscii.petscii()
modem = hayes.hayes_modem()
modem.wifi.load()#load settings
modem.wifi.wifi_connect()
ser = UART(0, 2400)                         # init with given baudrate
ser.init(2400, bits=8, parity=None, stop=1) # txbuf init with given parameters

buffer = ""
bs = bytearray()
while True:
    if modem.Busy == True:
        dta = modem.bbs.read_data()
        if dta:
            ser.write(dta)
            ser.flush()
    bs = ser.read(1)
    if bs:
        if modem.Busy == False or chr(bs[0])=="+":
            buffer+=petscii.petscii2ascii(bs)
            if bs[0] == 20:#detect delete and remove characters from buffer
                buffer = buffer [:-1]
        if modem.Busy == True:
            if not modem.bbs.send_data(bs):
                modem.close_connection()
                ser.write(petscii.ascii2petscii("Lost Connection\n"))
        elif modem.Echo:
            ser.write(bs)

        if  petscii.petscii2ascii(bs) == "\n" or buffer == "+++":
            cmd = buffer
            buffer = ""
            response = modem.process_command(cmd)
            if response:
                for item in response:
                    item = petscii.ascii2petscii(item)
                    ser.write(item)
