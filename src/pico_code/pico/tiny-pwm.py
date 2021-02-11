from machine import ADC, PWM

inputs = [ADC(i) for i in [26, 27, 28]]
outputs = [PWM(i) for i in [18, 19, 20]]
for pwm in outputs:
    pwm.freq(1000)
io = zip(inputs, outputs)
while True:
    for (adc, pwm) in io:
        pwm.duty_u16(adc.read_u16)