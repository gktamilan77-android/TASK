


#1.Print Hello world

print("Hello world")




#2.Add,subtract,multiple,divide and modulus


a=int(input("Enter a first number  :"))
b=int(input("Enter a second number :"))

print("Addition :",a+b)
print("Subtraction :",a-b)
print("Multiplication :",a*b)
print("Division :",a/b)
print("Modulus :",a%b)



#3.Find square root


n=int(input("Enter a number :"))

s=n**0.5

print("Square root :"s)


#4.Area of triangle


b=int(input("Enter a base :"))
h=int(input("Enter a height :"))     #A=1/2*BH

a=0.5*b*h

print("area of triangle",a)



#5.Solve mathematical formulas 



a=int(input("Enter a :"))
b=int(input("Enter b :"))

print("(a=b)^2 :",a**2+b**2+2*a*b)
print("(a-b)^2 :",a**2-b**2+2*a*b)
print("a^2-b^2 :",a**2-b**2)






#6.Swap two variables

#1....Using third variable
a=int(input("Enter a 1st number :"))
b=int(input("Enter a 2nd number :"))

c=a
a=b
b=c

print("a=",a)
print("b=",b)


#2....Without third variable
a=int(input("Enter a 1st number :"))
b=int(input("Enter a 2nd number :"))

a,b=b,a

prinr("a="a)
print("b="b)







#7.Convert kilometers to miles


km=float(input("Enter kilometers :"))

miles=km*0.63

print("Miles",miles)






#8.Convert celsius to fahrenheit



celsius=float(input("Enter celsius :"))

fahrenheit=(celsius*1.8)+32

print("Fahrenheit :",fahrenheit)





#9.Find last digit of a number


n=int(input("Enter a number :"))

ld=n%10

print("Last_digit :",ld)






#10.Find last two digit of a number



n=int(input("Enter a number :"))

ld=n%100

print("Last two_digit :",ld)






#11.Find middle digit and its sqare


n=int(input("Enter a integer :"))

md=(n//100)%10
s=md**2

print("Square of",md,"is",s)




