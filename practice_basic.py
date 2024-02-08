#!/usr/bin/env python
# coding: utf-8

# In[1]:


# # 1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the output.
# # BMI = weight / (square of height)


def bmi(hei,wei):
    bmi = wei/hei**hei
    return bmi

height = float(input("Enter your height in meter"))
weight = int(input("Enter your weight in kg"))

bm = bmi(height,weight)
print(bm)


# In[3]:


# # 2- write a program which takes the name of the user as input and replace all the occurence of character 
# 'a' in the name to 'b' and print it.

def name(nam):
    rep_name = nam.replace('a','b')
    return rep_name

user_name = input("enter your name")
name(user_name)


# In[7]:


# # 3- write a program which takes 2 inputs from user as principle amount (int) and rate of annual interest
# (float) and print the expected total amount  after  2 years.

def intrst(amt,rate,yr):
    ra = amt +(amt*yr*rate)/100
    return ra
    
amount = float(input('Enter your principal amount'))
intr = float(input("enter your interst"))
year = int(input("enter your year of maturity"))

d = intrst(amount,intr,year)
print(d)



# In[10]:


# 4- write a program which takes city name from user input. irrespective of in which case user 
#enters the city name, print the city name in camel case meaning first letter should be capital and rest in small.

# example : input : MYSORE ,  print - > Mysore 

def camelcase(name):
    name = name.capitalize()
    return name


name_u = input("Enter your name")
c = camelcase(name_u)
print(c)


# In[12]:


# 5- write a program which takes the name of the user as input and print the index of character 
#'a' in the string. if 'a' is not there then return -1.

def ind(name):
    name = name.find('a')
    return name

name_r = input("Enter your name")
ind = ind(name_r)
print(ind)


# In[1]:


# 6-  Display the number of letters in the below string
# my_word = "antidisestablishmentarianism"


def leng(name):
    name = len(name)
    return name

word = 'antidisestablishmentarianism'
leng = leng(word)
print(leng)


# In[8]:


# 7- take 3 inputs from user : first name , last name and age . Display the information in below format
# exmaple 
# first name : MOhit
# last name : sharma 
# age 32


def name(first,last,age):
    print(f"first name : {first.capitalize()}\nlast name : {last.capitalize()}\nage : {age}")
    
    
nam = name('indra','raga',23)
print(nam)


# In[20]:


# 8-take 3 inputs from user : first name , last name and company name. 
# create the email alias for the user and display it.  Email alias is first 2 letters of first name , 
# last 3 letters of last name and @company.com
# example 
# first name : MOhit
# last name : sharma 
# company : infosys

# Display : morma@infosys.com 

# note full email id should -be in lower case


def mail(fir,las,com):
    print(f"{fir[0:2].lower()}{las[-3:].lower()}@{com.lower()}.com")
          
          
          
fir = 'Indra'
las = 'Ragavi'
com = 'Virtusa'

mail(fir,las,com)

          
          

# 1- write a program which takes single input from user contaning first name,last name and age as comma separated value and display then in 3 lines in given format below.

# example user input : Ankit,Bansal,35

# output:
# First name is Ankit
# last name is Bansal
# Ankit is 35 years old 

# note : do not hardcode name at any place



def fun(name):
    print(f"First Name is {name[0].capitalize()}\nLast name is {name[1].capitalize()}\n{name[0].capitalize()} is {name[2]} years old")
    

name = input("Enter your first,last name and age separated by ,")
name = name.split(',')
n = fun(name)




# In[7]:


# 2- given 2 list as list1= [1,3,4] and list2 = [2,4,6]

# combined the 2 list and diplay the same without using extend metho
list1= [1,3,4] 
list2 = [2,4,6]
def apen(list1,list2):
    for i in list1:
        list2.append(i)
        return i

app = apen(list1,list2)

print(app)
print(list2)


# In[21]:


# 3- given a list list1=[1,2,3,4,5,6,7,8]
# diplay a new list which contains only odd position index values from above list.

def odd_pos(li):
    res = []
    for i in range(len(li)):
        if i%2 !=0:
            res.append(li[i])
            
    return res
    
    
lis = [1,2,3,4,5,6,7,8]
b = odd_pos(lis)
print(b)


# In[8]:


# 4- ipl= ['CSK','MI','KKR','LSG','PBKS']

# take a ipl team name as input from user and display a list of all elements from that name.

# example : input : KKR
# output : ['KKR','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']

def fin(name,ipl):
    for i in ipl:
        if i == name:
            ind = ipl.index(i)
            print(ipl[ind:])
            
            
            
nam = input("Name")
f = fin(nam,ipl)

        


# In[31]:


# 5- ipl= ['CSK','MI','KKR','LSG','PBKS']

# take a ipl team name as input from user and display a list of all elements except input one

# example : input : KKR
# output : ['CSK','MI','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']
def cont(name,ipl):
    for i in ipl:
        if i == name:
            continue
        print(i)
            
nam = input("name")
v = cont(nam,ipl)


# In[54]:


# 6- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma seprated values index,new_team . replace the index element of list with new value 
#and display the same

# example : input : 2,SRH
# output : ['CSK','MI','SRH','LSG','PBKS']

ipl= ['CSK','MI','KKR','LSG','PBKS']
nam = input("enter index and name with ,")
nam  = nam.split(",")

ipl[int(nam[0])] = ipl[int(nam[0])].replace(ipl[int(nam[0])],nam[1])
print(ipl)


# In[68]:


# 7- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take ipl team name as user input. display True if the team exists else display False.

ipl= ['CSK','MI','KKR','LSG','PBKS']
nam = input("enter team\n")

def chck(ipl,nam):
    if nam in ipl:
        print(True)
    else:
        print(False)
            
v = chck(ipl,nam)


# In[80]:


# 8-ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma seprated values index,new_team . Add the new value at that index in the list. 
# Display the old list , new list,length of original and new list

# example : input : 2,SRH
# output : 
# old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
# new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6

ipl= ['CSK','MI','KKR','LSG','PBKS']


nam = input("Enter index and team name with , as sep\n")
nam  = nam.split(",")


def lis(ipl,nam):
        ipl.insert(int(nam[0]),nam[1])
        print(ipl)
        
        
li = lis(ipl,nam)


#!/usr/bin/env python
# coding: utf-8

# In[18]:


# 1- given a list of numbers, write a program to find the mean of the numbers in list

li = [2,3,23,31,432,2]


def mean(li):
    sum1 = 0
    for i in li:
        sum1 = sum1 +i
    return sum1/len(li)
    
m = mean(li)
print(m)


# In[33]:


# 2- given a list of numbers unsorted, write a program to find the median of the numbers in list

lis = [2,2,3,23,31,33,432] 
# [2,3,23,31,432,3,2]- [2,2,3,23,31,33,432] 
lis.sort()
def med(lis):
    if len(lis)%2==0:
        med = (lis[len(lis)//2] + lis[(len(lis)//2)+1])/2
        print(med)
    else:
        med = lis[len(lis)//2]
        print(med)
        
m = med(lis)


# In[44]:


# 3- from a list of numbers create 2 list , one containing only the even numbers and other only the odd numbers

lis = [1,2,3,4,5,6,7,8,9]

def od_ev(lis):
    li_od = []
    li_ev = []
    for i in lis:
        if i %2==0:
            li_ev.append(i)
        else:
            li_od.append(i)
            
    return li_od, li_ev
            
v = od_ev(lis)
print(v)


# In[43]:


# 4- create a dictionary to store following attributes of CSK 
# key "CSK" ; attributes : team full name , captain , playing 11 for each match(name of players),
#oppenont name (assume there are 3 matches only against MI, RCB , GT ) and result won/loss

ipl = {'CSK':{'Fullname':'Chennai Super Kings',
              'Captain':'Dhoni',
              'payer_name':['Rohit','Dhoni','Sachin','Tendul','Dravid','Virat','shvin','Mohit','Ram'],
              'opponent':['MI','RCB','GT'],
              'result':'won'}}


# In[37]:


res = {'exam':'tnpsc','People':12,'Result':'pass'}


# In[40]:


print(type(ipl))


# In[41]:


# 5- in the previous dictonary add one more item for RCB. you can choose any 3 opponents.
ipl['RCB']={'fullname':'Royal Challen','captain':'virat','player_name':['Virat','ndioe','vijay','oild'],'opponet':['csk','mi'],
           'result':'won'}


# In[42]:


print(ipl)


# In[1]:


# 6- write a program to take a positive number as input from user.
#if the user enters negative number then keep promting him to enter positive number until he
#enters the positive number and then print the same

def pos(num):
    while True:
        if num > 0:
            print("positive no is ",num)
            break
        else:
            num = int(input('Enter a positive no'))
    
    
num = int(input('Enter a positive no'))
pos = pos(num)



# In[35]:


# 7- consider the below list of list conatins following information :
# 1. The name of a university 
# 2. The total number of enrolled students
# 3. The annual tuition fees

# universities = [
# ['California Institute of Technology', 2175, 37704],
# ['Harvard', 19627, 39849],
# ['Massachusetts Institute of Technology', 10566, 40732],
# ['Princeton', 7802, 37000],
# ['Rice', 5879, 35551],
# ['Stanford', 19535, 40569],
# ['Yale', 11701, 40500]
# ]
# write a program to print follwoing information :
# 1- a list of all the universitites  : ['California Institute of Technology','Harvard',..so on]
# 2- total number of student entrolled in all the unversities together 
# 3- mean of tuition fees
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

# un = []
# def univ(uni):
    
#     for i in uni:
#         un.append(uni[i][0])
        
# uni = universities
# u = univ(uni)
# print(un)

un = []
def func(uni):
    sum = 0
    mean = 0
    total_fee=0
    for i in uni:
        print("University of",i[0])
        sum = sum+i[1]
        total_fee+=i[2]
        mean = total_fee//len(uni)
    return "sumo is", sum, 'mean is ',mean

d = func(universities)
print(d)
        
    
    


# In[ ]:


# 8- write a program to convert above universities list to a dictionary. the keys should be the name of the university

# 9-  write a program that reverses a given string. For example, if the input is "Hello" from user, the output should be "olleH"

# 10- write a program that finds the largest number in a list(unsorted) of integers without using sort/sorted method.


# In[46]:


for i in range(1,21):
    print(f"{i} * 2 = {i*2}")


# In[49]:


a = int(input("Enter a"))
b = int(input("Enter b"))

for i in range(a+1,b):
    print(i)


# In[55]:


for i in range(1,11):
    if i%2==0:
        print(i)
    print(i)


# In[72]:


a = 0
for i in range(1,11):
    if i %2 ==0:
        a = a+1
print(a)
    


# In[73]:


cou_odd = 0
cou_ev = 0

for i in range(1,11):
    if i%2 ==0:
        cou_odd = cou_odd + 1
    else:
        cou_ev = cou_ev+1
print("odd_count",cou_odd)
print("even_count",cou_ev)


# In[77]:


count = 0
for i in range(1,101):
        if i%3==0 and i%5==0:
            count = count +1
print(count)


# In[1]:


sum = 0
for i in range(1,6):
    sum = sum + i
print(sum)


# In[4]:


def su(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)
    
s = su(1,2,3,4,5)
        


# In[6]:


sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)
    
    


# In[7]:


a = []
for i in range(3):
    num = int(input())
    a.append(num)
    
print(a)


# In[18]:


a = []
sum  = 0
for i in range(5):
    inp = int(input("enter no"+str(i+1)+"\n"))
    a.append(inp)

sum = 0
for i in range(len(a)+1):
    sum = sum + i
    avg = sum/len(a)
print(sum)
print(avg)


# In[27]:


a = []
sum = 0
n = int(input("enter n"))
for i in range(1,n+1):
    a.append(i)
    sum = sum + i

print(sum)
print(n,"natural no is",a)


# In[36]:


n = int(input("enter n for cube"))
import math
for i in range(1,n+1):
    print("the cube of ",i,"is",pow(i,3))


# In[40]:


for i in range(1,3):
    for j in range(1,6):
        print(i,j,"apple")


# In[44]:


for i in range(1,3):
    print("Week",i)
    for j in range(1,4):
        print("Day",j)


# In[56]:


for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end="")


# In[65]:


for i in range(1,6):
    print("*")
    for j in range(1,i+1):
        print(" * ",end="")


# In[79]:


for i in range(1,6):
    
    for j in range(1,6):
        print("()",end=" ")
    print()


# In[94]:


for i in range(1,6):
    print()
    for j in range(1,i+1):
        print("* ",end="")


# In[88]:


for i in range(1,6):
    for j in range(i,6):
        print('*',end=' ')
    print()


# In[119]:


for i in range(1,6):
    for j in range(i,6):
        print('',end=" ")
    for j in range(i):
        print("*",end=' ')
    print( )


# In[111]:


for i in range(1,6):
    for j in range(i,6):
        print('',end='')
    for j in range(1,i+1):
        print('*',end="")
    print()


# In[113]:


for i in range(1,4):
    for j in range(i,4):
        print('*',end='')
    print()


# In[114]:


for i in range(1,4):
    for j in range(1,i+1):
        print('*',end='')
    print()


# In[117]:


for i in range(1,4):
    for j in range(i,4):
        print('*',end='')
    for j in range(1,i+1):
        print('.',end='')
    print()


# In[134]:


for i in range(1,4):
    for j in range(i,4):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end='')
    for j in range(i-1):
        print('*',end='')
    print()


# In[156]:


for i in range(1,6):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,6-1):
        print('*',end='')
    for j in range(i,6):
        print('*',end='')
    print()


# In[161]:


for i in range(1,6):
    for j in range(i,6):
        print(' ',end='')
    for j in range(i,6-1):
        print('*',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,6-1):
        print('*',end='')
    for j in range(i,6):
        print('*',end='')
    print()


# In[1]:


for i in range(1,4):
    for j in range(1,i+1):
        print('*',end='')
    print()


# In[2]:


for i in range(1,4):
    for j in range(i,4):
        print('*',end='')
    print()


# In[16]:


for i in range(1,4):
    for j in range(i+1,4):
        print(' ',end='')
    for j in range(1,i+1):
        print('* ',end='')
    print()


# In[20]:


def star(n):
    for i in range(1,n):
        for j in range(1,i+1):
            print('* ',end='')
        print()
        
star(5)


# In[28]:


def add(*args):
    sum = 0
    print(args,type(args))
    for i in args:
        sum = sum + i
    return sum

s = add(1,2,3)

print(s)


# In[31]:


def key_a(**kwargs):
    print(kwargs,type(kwargs))
    
    
key_a(a='keyword',b='ndk')









