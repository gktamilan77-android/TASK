



#1.Linear search

a=[101,205,304,405,502]
target=304

for i in range(len(a)):
    if a[i]==target:
        print("Element fount ")
        break



#2.Find second largest

a=[45,12,89,67,34,90]
s=n=float("-inf")

for i in a:
    if i>s:
        n=s
        s=i
    elif i>n and i!=s:
        n=i

print("Second largest :",n)



#3.Find second smallest

a=[45,12,89,67,34,90]
s=n=float("inf")

for i in a:
    if i<s:
        n=s
        s=i
    elif i<n and i!=s:
        n=i

print("Second largest :",n)



#4.Sort without built-in function

a=[64,34,25,12,22,11,90]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)




#5.Remove duplicate

a=[10,20,10,30,20,40]
b=[]

for i in a:
    if i not in b:
        b.append(i)

print(b)



#6.Find missing number

a=[1,2,3,5,6]

n=len(a)+1
total=n*(n+1)//2

missing=total-sum(a)

print("Missing number",missing)



#7.Find common elements

a=[10,20,30,40]
b=[30,40,50,60]
c=[]

for i in a:
    if i in b and i not in c:
        c.append(i)

print(c)




#8.Move zeros to end

a=[0,5,0,3,8,0,2]
b=[]

for i in a:
    if i!=0:
        b.append(i)

for i in a:
    if i==0:
        b.append(i)

print(b)



#9.Frequency of elements

a=[10,20,10,30,20,10]

for i in a:
    if a.index(i)==a.index(i):
        if i not in []:
            pass

s={}

for i in a:
    s[i]=s.get(i,0)+1

for key,value in s.items():
    print(key,":",value)




#10.Stock price analysis

a=[120.5,132.0,118.4,145.2,128.9]

high=max(a)
low=min(a)
avg=sum(a)/len(a)

print("Highest :",high)
print("Lowest :",low)
print("Average :",round(avg,1))




#11.Tuple search

a=(101,202,303,404,)
target=303

for i in range(len(a)):
    if a[i]==target:
        print("Index :",i)
        break



#12.Tuple soring

a=(50,10,40,20,30)

b=tuple(sorted(a))

print(b)




#13.Find maximum and minimum

a=(15,82,24,95,33)

maximum=a[0]
minimum=a[0]

for i in a:
    if i> maximum:
        maximum=i
    if i<minimum:
        minimum=i

print("Max :",maximum)
print("Min :",minimum)



#14.Count duplicate values

a=(10,20,10,30,20,10)

for i in set(a):
    print(i,":",a.count(i))




#15.Remove duplicate values

a=(1,2,2,3,4,4,5)
b=tuple(dict.fromkeys(a))
print(b)




#16.Tuple comparison

a=(1,2,3)
b=(3,2,1)

print("Equal elements :",set(a)==set(b))




#17.Find common elements

a=(10,20,30,40)
b=(30,40,50,60)
c=tuple(i for i in a if i in b)

print(c)





#18.Student ranking

mark=(78,92,85,88,95,60)

top=sorted(set(mark),reverse=True)[:3]


print("Top 3 :",top)




#19.Tuple of employee records

employees=(("E101","Arun",45000),("E102","Priya",52000),("E103","Kumar",48000))

high=employees[0]

for i in employees:
    if i[2]>high[2]:
        high=i

print("Highet salary :",high)




#20.Sort employee records

employees=(("E101","Arun",45000),("E102","Priya",52000),("E103","Kumar",48000))

result=tuple(sorted(employees,key=lambda x:x[2]))

print(result)




#21.Find common skills

a={"Python","Java","Sql","Git"}
b={"Python","Sql","Html","Git"}

print(a.intersection(b))




#22.Unique elements

a=[1,2,2,3,4,4,5]
b=set(a)

print("Unique count :",len(b))




#23.Find missing employee IDs


id={101,102,103,104,105}
present={101,103,105}

absent=id-present

print("Absent :",absent)




#24.Find duplicate values

a=[10,20,30,10,20,40]

n=set()
dup=set()

for i in a:
    if i in n:
       dup.add(i)
    else:
        n.add(i)

print("Duplicates :",dup)





#25.Union of skills

a={"Python","Sql"}
b={"Java","Sql","Git"}

print(a.union(b))




#26.Set difference


a={"Python","Java","Sql"}
b={"Sql","Git"}

print(a.difference(b))





#27.Course registration

python={"Arun","Priya","Kumar"}
java={"Divya","Rahul"}

print("Both :",python&java)
print("Python only :",python-java)
print("Java only :",java-python)
print("Total unique :",len(python|java))





#28Unique visitors

a={101,102,101,103,104,102,105}

unique=set(a)

print(len(unique))





#29.Subset validation

required={"Python","SQL","Git"}
candidate={"Python","SQL","Git","Java"}

if required.issubset(candidate):
    print("Eligible")
else:
    print("Not eligible")




#30.Common products

store1={"P101","P102","P103"}
store2={"P102","P103","P104"}

print(store1.intersection(store2))




#31.Employee search

employees={101:"Arun",102:"Priya",103:"Kumar"}
target=102

print(employees[target])




#32.Find highest salary

employees={"Arun":45000,"Priya":52000,"Kumar":48000,"Divya":60000}
high=max(employees,key=employees.get)

print(high,"With salary",employees[high])




#33.Sort dictionary by values

employees={"Arun":45000,"Priya":52000,"Kumar":48000,"Divya":60000}
result=dict(sorted(employees.items(),key=lambda x:x[1]))

print(result)




#34.Sort dictionary by keys 

employees={"Priya":102,"Arun":101,"Kumar":103}

s=dict(sorted(employees.items()))

print(s)




#35.Word frequency

a="python java python sql java python"

word=a.split()
frequency={}

for i in word:
    frequency[i]=frequency.get(i,0)+1

print(frequency)





#36.Character frequency

a="programming"
f={}

for i in a:
    f[i]=f.get(i,0)+1

print(f)




#37.Highest frequency element

a=[10,20,10,30,20,10]
f={}

for i in a:
    f[i]=f.get(i,0)+1

high=max(f,key=f.get)

print(high)




#38.Group emplooyees by department

employees={"Arun":"IT","Priya":"HR","Kumar":"IT","Divya":"Finance","Rahul":"IT"}

r={}

for name,dept in employees.items():
    if dept not in r:
        r[dept]=[]

    r[dept].append(name)

print(r)





#39.Product inventory

products={"Laptop":15,"Mouse":8,"Keyboard":25,"Monitor":5}

high=max(products,key=products.get)
low=min(products,key=products.get)
total=sum(products.values())

below=[]

for name,stock in products.items():
    if stock<10:
        below.append(name)

print("Highest :",high)
print("Lowest :",low)
print("Total :",total)
print("Below :",below)





#40.Student ranking


students={"Arun":85,"Priya":92,"Kumar":78,"Divya":95,"Rahul":88}

high=max(students,key=students.get)
low=min(students,key=students.get)

std=sorted(students.items(),key=lambda x:x[1],reverse=True)

print("Highest :",high,students[high])
print("Lowest :",low,students[low])
print("Top 3 :",std[:3])







