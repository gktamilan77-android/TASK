

#1.Reverse a number

def reverse(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev

n=12345
print(reverse(n))






#2.Sum of digits

def s(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n=n//10
    return total

n=5832
print(s(n))





#3.Prime number checker

def prime(n):
    if n<2:
        return False

    for i in range(2,n):
        if n%i==0:
            return False

    return True

n=29

if prime(n):
    print("Prime")
else:
    print("Not prime")





#4.Prime number in a range

def prime(n):
    if n<2:
        return False

    for i in range(2,n):
        if n%i==0:
            return False

    return True

def rank(i,r):
    for i in range(i,r+1):
        if prime(i):
            print(i,end=" ")

l=10
r=30

rank(l,r)





#5.Palindrome number

def p(n):
    temp=n
    rev=0

    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//10

    return temp==rev

n=1221

if p(n):
    print("Palindrome")
else:
    print("Not polindrome")





#6.Reverse a string

def r(s):
    rev=""

    for i in s:
        rev=i+rev

    return rev

s="programming"
print(r(s))




#7.Cunt vowals

def v(s):
    count=0

    for i in s:
        if i.lower() in "aeiou":
          count+=1

    return count

s="python programming"
print(v(s))





#8.Character frequency

def f(s):
    for i in s:
        if s.index(i)==s.find(i):
            count=0

            for j in s:
                if i==j:
                    count+=1

            print(i,":",count)

s="banana"
f(s)




#9.First non-repeating character

def r(s):
    for i in s:
        count=0

        for j in s:
            if i==j:
                count+=1

        if count==1:
            return i

    return "No unique character"

s="aabbcdde"
print(r(s))




#10.Remove duplicate characters

def d(s):
    r=""

    for i in s:
        if i not in r:
            r+=i

    return r

s="programming"
print(d(s))




#11.Find the second largest number

def s_l(s):
    large=s[0]
    sec=None

    for i in s:
        if i>large:
            sec=large
            large=i
        elif i<large:
            if sec is None or i>sec:
                sec=i

    return sec

s=(10,45,23,67,34)
print(s_l(s))






#12.Remove duplicate elements from a list

def d(s):
    r=[]

    for i in s:
        if i not in r:
            r.append(i)

    return r

s=(10,20,10,30,20,40)
print(*d(s))





#13.Move all zeros to the end

def z(s):
    r=[]

    for i in s:
        if i!=0:
            r.append(i)

    for i in s:
        if i==0:
            r.append(i)

    return r

s=(0,5,0,3,8,0,2)
print(*z(s))




#14.Find the missing number

def s(n,a):
    total=n*(n+1)//2
    return total-sum(a)
n=6
a=(1,2,3,5,6)

print(s(n,a))




#15.Find pairs with given sum

def p(a,t):

    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j]==t:
                print(a[i],a[j])

a=(2,7,11,15,3,6)
t=9

p(a,t)





#16.Anagram without sorting

def s(a,b):
    if len(a)!=len(b):
        return False

    for i in a:
        if a.count(i)!=b.count(i):
            return False

    return True

a="listen"
b="silent"

if s(a,b):
    print("Anagram")
else:
    print("Not anagram")





#17.String compression

def n(s):
    r=""
    count=1

    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            r+=s[i-1]+str(count)
            count=1

    r+=s[-1]+str(count)

    return r

s="aaabbcccc"
print(n(s))




#18.Find leaders in an array

def l(a):
    leaders=[]
    right=a[-1]

    leaders.append(right)

    for i in range(len(a)-2,-1,-1):
        if a[i]>right:
            right=a[i]
            leaders.append(a[i])

    for i in range(len(leaders)-1,-1,-1):
        print(leaders[i],end=" ")

a=(16,17,4,3,5,2)
l(a)
        
        


#19.Employee salary ranking

def s(a):
    high=a[0]
    second=None

    for name,salary in a:
        if salary>high[1]:
            second=high
            high=(name,salary)

        elif salary<high[1]:
            if second is None or salary>second[1]:
                second=(name,salary)

    print("Highest :",high[0],high[1])

    if second is not None:
        print("Secnd Highest :",second[0],second[1])

a=[("Arun",45000),("Priya",52000),("Kumar",48000),("Divya",60000)]
s(a)




#20.Student result processing

def c_result(a):
    total=sum(a)
    avg=total/5

    if avg>=90:
        grade="A"

    elif avg>=80:
        grade="B"

    elif avg>=70:
        grade="C"

    elif avg>=60:
        grade="D"

    else:
        grade="F"


    if avg >=40:
        result="Pass"
    else:
        result="Fail"

    print("Total :",total)
    print("Average :",avg)
    print("Grade :",grade)
    print("Result :",result)

a=(78,85,67,92,88)
c_result(a)
        



        
