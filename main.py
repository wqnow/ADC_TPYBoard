import pyb,math
from array import array
import uio
from pyb import Pin,ADC,DAC
import time


tim = pyb.Timer(6, freq=10)

#buf = array('u',range(128))
# create a buffer containing a sine-wave, using half-word samples
buf_dac = array('H', 2048 + int(2047 * math.sin(2 * math.pi * i / 128)) for i in range(128))
buf_adc = array('H',range(128))


# output the sine-wave at 400Hz
dac = DAC(1, bits=12)
dac.write_timed(buf_dac,128, mode=DAC.CIRCULAR)
adc = pyb.ADC(Pin('Y12'))       # create an analog object from a pin
adc.ADCALL(bits=12)
adc.read_timed(buf_adc,tim)

file = uio.open('3.txt', mode='w')
file.write('DAC')
file.write(str(buf_dac))
file.write('ADC')
file.write(str(buf_adc))
file.close()