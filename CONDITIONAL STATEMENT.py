

#1.Smallest number among two integers

x=int(input("enter value 1 : "))
y=int(input("enter value 2 : "))
if (x<y):
    print("Smallest=",x)
else:
        print("Smallest=",y)



#2.largest number among two integers

x=int(input("enter value 1 : "))
y=int(input("enter value 2 : "))
if (x>y):
    print("Smallest=",x)
else:
        print("Smallest=",y)


#3.Absolute value of a given integer

n=int(input("enter a number: "))
if n<0:
    n=-n
    print("Absolute value : ", n)



n=int(input("enter a number: "))
if n>0:
    n=-n
    print("Absolute value : ", n)
elif n>0:
    n=-n
    print("Absolute value : ",n)



#4.Check even number or odd number

n=int(input("enter a number: "))
if n%2==0:
    print("Even number")
else:
    print("Odd number")


#5.Check multiple of 5

n=int(input("enter a number: "))
if n%5==0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")




#6.Check multiple of 10

n=int(input("enter a number: "))
if n%10==0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")


#7.Check two-digit number

n=int(input("Enter a number : "))
if 10<=n<=99:
    print("Two-digit number")
else:
    print("Not two-digit number")


#8.Check three-digit number

n=int(input("Enter a number : "))
if 100<=n<=999:
    print("Three-digit number")
else:
    print("Not three-digit number")




#9.Check whether number ends with zero

n=int(input("enter a number: "))
if n%10==0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")




#10.Check square aboue or below 50

n=int(input("enter a number: "))
s=n*n
if s>50:
    print("Square is above 50")
else:
    print("Square is below or equal to 50")




#11.Check difference is zer or not

a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
n=a-b
if n==0:
    print("Difference is 0")
else:
    print("Difference is not 0")


#12.Student pass or fail

    
n=int(input("Enter computer science marks: "))
if n>=50:
    print("Passed")
else:
    print("Failed")



#13.Check divisible by 10


n=int(input("enter a number: "))
if n%10==0:
    print("Divisible of 10")
else:
    print("Not a divisible of 10")



#14.Find biggest digit of a two-digit number

n=int(input("Enter a two-digit : "))
a=n//10
b=n%10
if a>b:
    print("Biggest digit= ",a)
else:
    print("Biggest digit= ",b)



#15.Exam difficulty based on chice


n=int(input("Enter your choice: "))
if n==1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")




#16.Check value entered by user


n=int(input("Enter a value: "))
if n==1:
    print("You can go out and play")
else:
    print("You cannot go out and play")



#17.Square or rectangle

l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
if l==b:
    print("It is square")
else:
    print("It is rectangle")



#18.Check uppercase alphabet using ASSCII

n=int(input("Enter ASCII value: "))
if 65<=n<=90:
    print("ASCII value of a uppercase alphabe")
else:
    print("Not a uppercase alphabet ASCII value")




#19.Check lowwercase alphabet using ASCII

n=int(input("Enter ASCII value: "))
if 97<=n<=122:
    print("ASCII value of a lowercase alphabe")
else:
    print("Not a lowercase alphabet ASCII value")



#20.Check numeric character

n=int(input("Enter ASCII value: "))
if 48<=n<=57:
    print("ASCII value of a numeric character")
else:
    print("Not a numeric character ASCII value")



#21.Check multiple of both 5 and 3


n=int(input("Enter a number: "))
if n%5==0 and n%3==0:
    print("Multiple of both 5 and 3")
else:
    print("Not multiple 5 and 3")





#22.Three-digit number and multiple of 10


n=int(input("Enter a number: "))
if 100<=n<=999 and n%10==0:
    print("Three-digit number and multiple of 10")
else:
    print(" condition not satisfied")



#23.Three-digit number and multiple f 2,5 and 10
    

n=int(input("Enter a number: "))
if 100<=n<=999 and n%2==0 and n%5==0 and n%10==0:
    print("Condition satisfied")
else:
    print("Condition not satisfied")



#24.Both number even-product, otherwise sum


n=int(input("Enter first number: "))
m=int(input("Enter second number: "))
if n%2==0 and m%2==0:
    print("Product: ",n*m)
else:
    print("Sum: ",n+m)




#25.Buzz number



n=int(input("Enter a number: "))
if n%10==7 or n%7==0:
    print("Buzz number")
else:
    print("Not buzz number")






#IF ELIFE ELSE




#1.Largestnumber among three integers

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if a>b and a>c:
 print("Largest number: ",a)
elif b>a and b>c:
    print("Largest number: ",b)
else:
    print("Largest number: ",c)


#2.Smallest number among three integers

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if a<b and a<c:
 print("Smallest number: ",a)
elif b<a and b<c:
    print("Smallest number: ",b)
else:
    print("Smallest number: ",c)


#3.Positive,nagative or zero

n=int(input("Enter a number: "))
if n>0:
    print("Possitive")
elif n<0:
    print("Negative")
else:
    print("Zero")


#4.Library fine

n=int(input("Book return date: "))
if n>0 and n<=5:
    f=n*40
    print("Book return ",n,"days.")
    print("Fine amount ",f)
elif n>5 and n<=10:
    f=n*65
    print("Book return ",n,"days.")
    print("Fine amount ",f)
else:
    f=n*80
    print("Book return ",n,"days.")
    print("Fine amount ",f)




#5.Basic calculation

a=int(input("Enter a 1st number"))
b=int(input("Enter a 2nd number"))
n=input("Enter operation(+,-,*,/): ")
if n=="+":
    print(a+b)
elif n=="-":
    print(a-b)
elif n=="*":
    print(a*b)
elif n=="/":
    if n!=0:
        print(a/b)
    else:
        print("Cannot divide by zero ")
else:
    print("Invalid operation")




#6.multiple of 5,3 and 7

n=int(input("Enter a number: "))
if n%5==0 and n%3==0 and n%10==0:
    print("Number is a multiple of 5,3 and 10")
else:
    print("Number is not multiple of 5,3 and 10")




#7.Parcel booking charges


w=float(input("Enter parcel weight: "))
b=input("Enter booking type(O for Ordinary,E for Experss): ")
if w<=100:
     if b=='O':
         c=80
     elif b=='E':
        c=100
     else:
         c=-1
elif w<=500:
    if b=='O':
        c=150
    elif b=='E':
        c=200
    else:
        c=-1
elif w<=1000:
    if b=='O':
        c=210
    elif b=='E':
        c=250
    else:
        c=-1
else:
    if b=='O':
      c=250
    elif b=='E':
        c=300
    else:
            c=-1
if c==-1:
    print("Invalid booking type")
else:
    print("Parcel charge= ",c)





#8.Laptop discount


p=float(input("Enter price of laptop :"))
if p<=50000:
    d=p*5/100
elif p<=100000:
    d=p*10/100
else:
    d=p*15/100
t=p-d
print("Price of laptop :",p)
print("Discount        :",d)
print("Total price     :",t)






