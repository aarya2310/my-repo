
def temp():
    while True:
        a=int(input('enter choice /n 1. Celsius to Fahrenheit /n 2. Fahrenheit  to Celsius'))
        if a==1:
            celsius()
        elif a==2:
            fahrenheit()
        elif a==3:
            print('exit')
            break
def celsius():
    # f=float(input('celsius to fahrenheit'))
    b=int(input('enter temperature in celsius'))
    Fahrenheit = (9/5)*b +32
    print(Fahrenheit)
def fahrenheit():
    c=int(input('enter temperature in fahrenheit'))
    Celsius = (5/9)*(c-32)
    print(Celsius)
temp()
# celsius()
# temperature()