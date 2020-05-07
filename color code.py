global T_digit,O_digit,multipl,toler

def black():
    digit = 0
    multi = 1
    tole = 0
    return digit,multi,tole

def brown():
    digit = 1
    multi = '10'
    tole = 1
    return digit,multi,tole

def red():
    digit = 2
    multi = '10^2'
    tole = 2
    return digit,multi,tole

def orange():
    digit = 3
    multi = '10^3'
    tole = 0
    return digit,multi,tole

def yellow():
    digit = 4
    multi = '10^4'
    tole = 0
    return digit,multi,tole

def green():
    digit = 5
    multi = '10^5'
    tole = 0.5
    return digit,multi,tole

def blue():
    digit = 6
    multi = '10^6'
    tole = 0.25
    return digit,multi,tole

def violet():
    digit = 7
    multi = '10^7'
    tole = 0.1
    return digit,multi,tole

def grey():
    digit = 8
    multi = '10^8'
    tole = 0
    return digit,multi,tole

def white():
    digit = 9
    multi = '10^9'
    tole = 0
    return digit,multi,tole

def gold():
    digit = None
    multi = '10^-1'
    tole = 5
    return digit,multi,tole

def silver():
    digit = None
    multi = '10^-1'
    tole = 10
    return digit,multi,tole

def blank():
    digit = None
    multi = None
    tole = 20
    return digit,multi,tole



def choice(color):
    if color =='black':
        digit,multi,tole =black()
    elif color =='brown':
        digit,multi,tole =brown()
    elif color =='red':
        digit,multi,tole =red()
    elif color =='orange':
        digit,multi,tole =orange()
    elif color =='yellow':
        digit,multi,tole =yellow()
    elif color =='green':
        digit,multi,tole =green()
    elif color =='blue':
        digit,multi,tole =blue()
    elif color =='violet':
        digit,multi,tole =violet()
    elif color =='grey':
        digit,multi,tole =grey()
    elif color =='white':
        digit,multi,tole =white()
    elif color =='gold':
        digit,multi,tole =gold()
    elif color =='silver':
        digit,multi,tole =silver()
    elif color =='':
        digit,multi,tole =blank()

    return digit,multi,tole



def tens(color):
    digit,multi,tole = choice(color)
    
    global T_digit 
    T_digit = digit*10

def ones(color):
    digit,multi,tole = choice(color)
    global O_digit
    O_digit = digit

def mult(color):
    digit,multi,tole = choice(color)
    global multipl 
    multipl = multi

def tol(color):
    digit,multi,tole =choice(color)
    global toler 
    toler = tole

s = input("Enter choice of resistor(4/5) : ")

if s =='4':
    tens(color = input("Enter first color :"))
    ones(color = input("Enter second color :"))
    mult(color = input("Enter third color :"))
    tol(color = input("Enter fourth color :"))
    print("Total resistance is : " + str((T_digit+O_digit)) + " * " + multipl + " ohm +/- " + str(toler)+"%")




#if s=='5':
#    print("Enter first color :",color1 = input())
#    print("Enter second color :",color2 = input())
#    print("Enter third color :",color3 = input())
#    print("Enter fourth color :",color4 = input())
#    print("Enter fifth color :",color5 = input())