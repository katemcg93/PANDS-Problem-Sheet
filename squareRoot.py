#This programme will get the approximate square root of a number
#Will do this 

x=1
y=0
a=0

def squareRoot(a):
    x=1
    while True:
        print (a)
        y= (x + a/x)/2
        print(x)
        if abs(x-y) < 0.00000001:
            print(y)
            break
        x=y
squareRoot(25)