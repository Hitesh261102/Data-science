# print("hello world")
# a=10
# name="Hitesh"
# print(a)
# print(name)
# a="This is a string"
# print(type(a))
# slicing
# print(len(a[2:6]))
# print(a[-1])
# print(a.upper())
# print(name.lower())
# print(name.title())
# print(a.capitalize()) #diff b/w title and capitalize
# print(a.casefold())
# print(a.count("i"))# count occurence of letter
# print(a.index("i"))# tells idx of letter

# intro="I love java"
# intro.replace("java","python")# replace word with another
# print(intro)

# string="python"
# print(string.startswith("py"))# checks word start with 
# print(string.endswith("on"))

# num="123"
# print(num.isdigit())
# char="hello"
# print(char.isalpha())

# ch="is 123 numeric "
# print(ch.isalnum())
# print(ch*3)
# print(ch+ch)
# print(ch.strip())

# string formating
# name="abc"
# address="pilani"
# print(f"Hello My name is {name} and I am from {address}")


#     list
# 1.list is a collection of items
# 2.hetrogenous
# 3.ordered
# 4.allow duplicate values

list=[1,2,3,3,"hello"]
# print(list)
# print(type(list))
# print(len(list))
# print(list[0:(len(list)):2])
# list[3]=4
# print(list)
# list.append(5)
# list.insert(3,2)
# list.extend([5,6,7,[1,2,[1,2]]])
# print(list[8][2][1])
# list.pop(3)
# list.remove(1)
# print(list.count(3))
# list.clear()
# print(list.copy())
# list.reverse()
# list.sort()

# print(list)
# lst1=[1,2,3]
# lst2=[2,3,4]
# print(lst1+lst2)
# print(lst1*2)
# 

# dict={"a":1,"b":2}
# print(dict)

# a={1,2,3,4,1}
# print(a)

# t=(1,2,3,1)
# print(type(t))
# print(t)
# print(type(dict))
# print(type(a))

# a=5
# b=5.4
# c=5+3j
# d=False
# x=len(a)+len(b)+len(c)+len(d) ->error, len only take string as input
# l="abc"
# j="adc"
# print(len(l)/len(j))
# print(l//j)

# a=1
# b=0
# c=-1
# if a and b :
    # print("hello")
    # if b or c:
        # print("hi")
    # else:
        # print("hii")
# else:
    # print("bye")

# for i in range(1,11):
    # print(i)

# student={"name":"Hitesh","age":20,"branch":"csc"}
# print(student["branch"]) # for extracting value of a key
# student["age"]=22
# student["phone no"]=1234567890
# print(student)
# print(student.keys())
# print(student.values())

# for key,val in student.items():
    # print(key,val)



# student={"Hitesh":{"age":20,"branch":"csc"},"Anurag":{"age":19,"branch":"csc"}}
# for key,val in student.items():
    #  print(key,val)

# print(student["Hitesh"]["branch"])
# name=["abc","qwe"]
# def greet(name):
    # for i in name:
        # print(f"Hello {i} ,how are you")

# greet(name)

#lambda function
# square=lambda x:x*x
# print(square(10))
import re
def checkpassword(password):
    score=0
    if len(password)>=8:
        score+=1
    if re.search(r"[A-z]",password):
        score+=1
    if re.search(r"[0-9]",password):
        score+=1
    if re.search(r"[!@#$%^&*()<>,.?/:|\"]",password):
        score+=1
    
    if score==1:
        print("password is weak")
    if score==2:
        print("password is moderate")
    if score==3:
        print("password is strong")
    if score==4:
       print("password is very strong")
     
password=input("enter your password : ")
checkpassword(password)
    
    
