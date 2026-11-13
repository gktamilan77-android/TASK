


#1.Find n natural numbers


n=int(input("Enter n :"))

for i in range(1,n+1):
    
 print(i)




#2.First n even natural numbers

n=int(input("Enter n :"))

for i in range(1,n+1):
    
 print(i*2)




#3.First n dd natural numbers


n=int(input("Enter n :"))

for i in range(1,n+1):
    
 print(i*2-1)






 #4.First n multiples of 3


n=int(input("Enter n :"))

for i in range(1,n+1):
    
 print(i*3)






#5.First n multiples of 5


n=int(input("Enter n :"))

for i in range(1,n+1):
    
 print(i*5)




#6.multiles of 2 till n


 n=int(input("Enter n :"))

for i in range(2,n+1,2):
    
 print(i)





#7.multiples of 2 or 3 till n



n=int(input("Enter a number :"))
for i in range(1,n+1):
    if i%2==0 or i%3==0:
     print(i,end=" ")




#8.multiples of 2,5 or 7 till n


n=int(input("Enter a number :"))
for i in range(1,n+1):
    if i%2==0 or i%5==0 or i%7==0:
        print(i,end=" ")






#9.First n multiples of 3,5 or 7


n=int(input("Enter n :"))
c=0
i=1

while c<n:
    if i%3==0 or i%5==0 or i%7==0:
        print(i,end=" ")
    c+=1
    i+=1





#10.Sum of digits


n=int(input("Enter a number :"))
sum=0

while n>0:
    sum+=n%10
    n=n//10
print(sum)





#11.Count number of digits


n=int(input("Enter a number :"))
c=0
while n>0:
    c+=1
    n=n//10
print(c)





#12.Find factors


n=int(input("Enter a number :"))
for i in range(1,n+1):
    if n%i==0:
      print(i,end=" ")





#13.Count factors


n=int(input("Enter a number :"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
print(c)





#14.Prime number check


n=int(input("Enter a number :"))

count=0

for i in range(1,n+1):
    
  if n%i==0:
    count+=1

if n>1 and count==2:
    print("Prime number")
    
else:
    print("Not a prime number")




#15.Prime number up to n

n=int(input("Enter N :"))

for i in range(2,n+1):
    prime=True

    for j in range(2,i):
        if i%j==0:
            prime=False
            break

    if prime:
        print(i,end=" ")




#16.Greatest common factor(GCF/GCD)

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))

while b!=0:
    a,b=b,a%b

print("GCD:",a)



#17.Common factors

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))

for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        print(i,end=" ")




#18.Fibonacci series between 0 and 50

a=0
b=1

while a<=50:
    print(a,end=" ")
    a,b=b,a+b


#19.Factorial calculation

n=int(input("Enter first number :"))
factorial=1

for i in range(1,n+1):
      factorial*=i

print("Factorial :",factorial)




#20.Sum of Even and Odd number

even=0
odd=0

while True:
    n=int(input("Enter a number (0 to stop) :"))

    if n==0:
        break
    if n%2==0:
        even+=n
    else:
        odd+=n

print("Even sum :",even)
print("Odd sum :",odd)




#21.Palindrome number check

n=int(input("Enter first number :"))

temp=n
reverse=0

while n>0:
    x=n%10
    reverse=reverse*10+x
    n//=10

if temp==reverse:
    print("Palindrome")

else:
    print("Not a plindrome")




#22.Armstrong number check

n=int(input("Enter first number :"))

temp=n
x=len(str(n))
total=0

while n>0:
    y=n%10
    total+=y**x
    n//=10

if temp==total:
    print("Armstrong number")

else:
    print("Not a aemstrong number")



#23.Pattern prining using nested loops
    #A_Right-angled triangle

for i in range(6):
    for j in range(i):
       print("*",end=" ")
    print()



    #B_Number pyramid

for i in range(1,6):
    for j in range(1,i+1):
       print(j,end=" ")
    print()





