
print("Name: Aditya kulkarni ")
print("Age : 19")
print("Course : Python")
print("College : GP Ahilynagar")


print("hello",end="@@")
print("world")


print("Welcome to Python!")
print('"Python" is very (easy)')


a=10
b=20
print("value of a= ",a,"and value of b= ",b)
print(f"value of a= {a} and value of b = {b}")


a,b=10,20
a,b=b,a
print(a,b)


a=10
print("Square of no. is :",a**2)


l=10
b=20
print("Area of rectangle : ",l*b)


b=10
h=20
print("Area of triangle : ",1/2*b*h)


a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
print("Addition : ",a+b)
print("Subtraction : ",a-b)
print("Multiplication : ",a*b)
print("Division : ",a/b)
print("Modulus : ",a%b)
print("Exponent : ",a**b)
print("Floor Division : ",a//b)


a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
c=int(input("Enter third no. : "))
a=a*2
b=b*2
c=c*2
print("Average of double of 3 no. is : ",(a+b+c)/3)


amount=int(input("Enter amount in doller"))
inr = amount*97.4
print("inr")


a=2+3j
b=4+5j
c=a+b
print("Addition of 2 complex no. is : ",c)
print("real part is : ",c.real)
print("imaginary part is : ",c.imag)


a=input("Enter first no. : ")
b=input("Enter second no. : ")
a=int(a)
b=int(b)
print("a= ",a,"b= ",b)


c=int(input("Enter temperature in celcius : "))
f=(c*9/5)+32
print("Temperature in fahrenheit : ",f)
f=int(input("Enter temperature in fahrenheit : "))
c=(f-32)*5/9


a=10
b=20
a=a^b
b=a^b
a=a^b
print("a= ",a,"b= ",b)



a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
print("Left shift : ",a<<b)


print("''")


a=2+3j
b=1+10j
print("Addition : ",a+b)
print("Subtraction : ",a-b)
print("Multiplication : ",a*b)
print("Division : ",a/b)


a=10
b=10
print(a is b)
print(a is not b)


print(id(a))
print(id(b))


n=input("Enter student name : ")
chr=input("Enter a single charecter : ")
if chr in n:
    print("charecter is present")
else:
    print("charecter is not present")


a=int(input("Enter a number : "))
if a%5==0:
    print("number is multiple of 5")
else:
    print("number is not multiple of 5")


a=int(input("Enter a number : "))
if a>0:
    print("number is positive")
else:
    print("number is negative")


a=int(input("Enter selling price : "))
b=int(input("Enter cost price : "))
if a>b:
    print("profit") 
else:
    print("loss")


a=int(input("Enter length :"))
b=int(input("Enter breadth :"))
if a==b:
    print("shape is square")
else:
    print("shape is rectangle")


a=int(input("Enter a number : "))
if a%3==0 and a%5==0:
    print("number is multiple of 3 and 5")
else:
    print("number is not multiple of 3 and 5")


print("1 - ",1**2)
print("2 - ",2**2) 
print("3 - ",3**2)
print("4 - ",4**2)
print("5 - ",5**2)


a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
c=int(input("Enter third no. : "))
if a>b and a>c:
    print("a is maximum")
elif b>a and b>c:
    print("b is maximum")
else:
    print("c is maximum")


y=int(input("Enter a year : "))
if ( y%4==0 and y%100!=0) or y%400==0 :
    print("Leap year")
else:
    print("Not a leap year")



p=int(input("Enter price : "))
if p>5000 and p<10000:
    print("Final price after discount : ",p-(p*5/100))
elif p>10000 and p<15000:
    print("Final price after discount : ",p-(p*10/100))
elif p>50000:
    print("Final price after discount : ",p-(p*20/100))
else:
    print("No discount")
    

c=int(input("Enter current reading : "))
l=int(input("Enter last reading : "))
u=c-l
if c>0 and c<100 and c>l:
    print("Current unit : ",c)
    print("Last unit : ",l)
    print("unit are : ",u)
    print(" bill is : ",u*2)
elif c>100 and c<250 and c>l:
    print("Current unit : ",c)
    print("Last unit : ",l)
    print("unit are : ",u)
    print(" bill is : ",u*4)
elif c>250 and c>l:
    print("Current unit : ",c)
    print("Last unit : ",l)
    print("unit are : ",u)
    print(" bill is : ",u*6)
else:
    print("Current unit must be greater than last unit!!! ")


f=input("Is festival sell is (on/off)) : ")
m=input("Do you have membership (yes/no) : ")
c=int(input("Enter cart value : "))
if f=="on":
    print("Discount is : ",c*30/100)
    if m=="yes":
        print("Discount is :",c*20/100)
elif f=="off" and m=="yes" and c>5000:
    print("Discount is : ",c*20/100)
elif f=="off" and m=="yes" and c<5000:  
    print("Discount is : ",c*10/100)
else:    print("No discount")



r=input("Are you registered (yes/no) : ")
if r=="no":
    print("Access denied")
else:
    f=input("Is fee paid (yes/no) : ")
    if f=="no":
        print("Access denied")
    else:
        t=int(input("Enter system time in 24 hr format : "))
        if t>=9 and t<=17:
            print("Exam started")
        else:
            print("Exam not started")
