from machine import Pin, PWM, ADC
from time import sleep
# creating PWM and ADC objects
adc = machine.ADC(28)
pwm0 = PWM(Pin(0))     
Led = PWM(Pin(2)) 
# setting frequency of PWM output
pwm0.freq(50)       
Led.freq(50)  
IN1 = Pin(1, Pin.OUT)
# continuously control the brightness of the LED and the motor speed using the potentiometer
while True:
        digital_value = adc.read_u16()   
        # reading analog values from the potentiometer
        pwm0.duty_u16(digital_value)      # set duty cycle, range 0-65535
        IN1.low()  
        Led.duty_u16(digital_value)  # writing analog values to the LED 
        print(digital_value)
        sleep(1)  
