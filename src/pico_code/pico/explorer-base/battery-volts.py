from machine import ADC
import time
              
def log_voltages(file_name):
    adc = ADC(26)
    with open(file_name,'w') as csv:
        while True:
            voltage = 3.3 * adc.read_u16() / 65535.0
            text = '%5.3f' % voltage
            print(text)
            csv.write(text)
            csv.write('\n')
            time.sleep(60)
        
log_voltages('rechargeable.csv')
