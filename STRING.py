

#1.Count characters

a="HELLO WORLD"
count=0

for i in a:
    count+=1
print("Total characters :",count)




#2.Reverse a string

a="PYTHON"
rev=""

for i in a:
    rev=i+rev

print(rev)




#3.Palindrome string

a="mom"

if a==a[::-1]:
    print("Palindrome")

else:
    print("Not palindrome")



#4.Count vowals

a="memory"
count=0

for i in a:
    if i in "aeiou":
        count+=1

print(count)



#5.Count consonants

a="coding"
count=0

for i in a:
    if i.isalpha()and i not in "aeiou":
        count+=1

print(count)



#6.Count digits

a="py123th4"
count=0

for i in a:
    if i.isdigit():
        count+=1

print(count)




#7.Count spaces

a="Python is fun"
count=0

for i in a:
    if i==" ":
        count+=1

print(count)




#8.Character occurrence

a="banana"
b="a"
count=0

for i in a:
    if i==b:
        count+=1

print(count)





#9.Remove spaces

a="p y t h o n"

count=a.replace(" ","")
print(count)



#10.Swap case

a="PyThOn"
print(a.swapcase())



#11.Count words

a="Data structures and algorithms"

word=a.split()

print(len(word))



#12.Largest word

n="Mechine learnig is powerful"

word=n.split()
long=""

for i in word:
    if len(i)>len(long):
        long=i

print(long)



#13Remove duplicate charactes

n="programming"
result=""

for i in n:
    if i not in result:
        result+=i

print(result)



#14.character frequency

a="code"

for i in a:
    if a.index(i)==a.rindex(i):
        print(i,":",a.count(i))



#15.First repeated character

a="programming"

for i in a:
    if a.count(i)>1:
        print(i)
        break



#16.First non-repeating character

a="swiss"

for i in a:
    if a.count(i)==1:
        print(i)
        break



#17.Anagram check

a="listen"
b="silent"

if sorted(a)==sorted(b):
    print("Anagram")

else:
    print("Not anagram")



#18.Reverse words

a="python is easy"

word=a.split()
reverse=" ".join(word[::-1])

print(reverse)



#19.Reverse each word

a="python is easy"
word=a.split()
reverse=""

for i in word:
    reverse+=i[::-1]+" "

print(reverse.strip())




#20.Remove vowals

a="education"
s=""

for i in a:
    if i not in "aeiou":
        s+=i

print(s)



#21.String rotation

a="ABCD"
b="CDAB"

if len(a)==len(b) and b in a+a:
    print("Rotation")

else:
    print("Not rotation")



#22.Most frequent character

n="success"
t=0
s=""

for i in n:
    count=n.count(i)

    if count>t:
        t=count
        s=i

print(s)




#23.String compression

n="aaabbc"
s=""
count=1

for i in range(len(n)):
    if i<len(n)-1 and n[i]==n[i+1]:
        count+=1
    else:
        s+=n[i]+str(count)
        count=1

print(s)




#24.Password validation condition

n=input("Enter password :")

upper=False
lower=False
digit=False

for i in n:
    if i.isupper():
        upper=True
    elif i.islower():
        lower==True
    elif i.isdigit():
        digit=True

if len(n)>=8 and upper and lower and digit:
    print("Valid password")
else:
    print("Invalid password")



#25.Email validation

email=input("Enter email :")

if ("@" in email and "." in email and email.index("@")<email.rindex(".") and " " not in email):
    print("Valid email")
else:
    print("Invalid email")







