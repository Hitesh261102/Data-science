#question 1
my_tuple = (10, 20, 30, 40, 50) 
#First element 
print("Frist element of tuple:",my_tuple[0])
#Last element
print("Last element of tuple:",my_tuple[-1])
#Length of the tuple
print("length of tuple:",len(my_tuple))
#Elements from index 1 to 3  
print("Elements from index 1 to 3:",my_tuple[1:4])


#question 2
fruits = ("apple", "banana", "mango", "orange")
#Second fruit  
print("Second element:",fruits[1])
#Last two fruits 
print("last two elements:",fruits[len(fruits)-2:len(fruits)])
#Total number of fruits 
print("total number of friuts:",len(fruits))


#question 3
numbers = {10, 20, 30, 40, 50}
# Complete set 
print("set:",numbers)
# Length of the set
print("length of set:",len(numbers)) 
#Check whether 30 is present in the set 
print("is 30 in numbers:",30 in numbers ) 


#question 4
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6} 
#Find 
# Union 
print("union of set1 and set2:",set1.union(set2)) 
# Intersection  
print("Intersection of set1 and set2:",set1.intersection(set2))


#question 5
student = {"name":"Kriti", "age":20, "course":"Python"} 
#Print: 
# Complete dictionary  
print("Student:",student)
#  Student name 
print("name of student:",student["name"]) 
# Student age  
print("Age of student:",student["age"]) 


numbers = [12, 45, 7, 23, 56, 89, 34] 
#Write a program to find: 
#  Largest element 
numbers.sort(key=None, reverse=False)
print(numbers)
print("Largest element:",numbers[-1])
#  Second largest element
print("second Largest element:",numbers[-2]) 
#  Smallest element 
print("second Largest element:",numbers[0])


#question 6
# Write a function that takes the list as input and returns the list in reverse order without using the reverse() 
arr = [10, 20, 30, 40, 50, 60]
i=0
def reverselist(lst): 
    return lst[::-1]
print("reversed list:",reverselist(arr))


#question 7
data = (5, 10, 15, 20, 25, 30, 35)
 #Write a program to:  
 # Count how many elements are divisible by 5
count=0
sum=0
for i in data:
    count+=int(i%5==0)
    sum+=i  
print("element divisible by 5:", count) 

# Find the sum of all elements 
print("sum of data is",sum)

# Find the average of the tuple 
print("avg of data is:",sum/len(data))


#question 8
students = { "Aman": 78, "Riya": 92, "Kriti": 88, "Rahul": 95 }
# Write a program to: 
# Find the student with the highest marks
higehest_mark=0
lowest_mark=100
for i in students.values():
    if higehest_mark<i:
        higehest_mark=i
    if lowest_mark>i:
        lowest_mark=i
print("higehest_mark:",higehest_mark)
#  ○ Find the student with the lowest marks 
print("lowest_mark:",lowest_mark)
#  Print only the students who scored more than 85 marks
print("students who score more than 85")
for k,i in students.items():
    if i>85:
        print(k) 



#question 9
#Write a function: count_frequency(arr) that takes a list as input and prints the frequency of each element.
arr = [1, 2, 2, 3, 1, 4, 2]
def freq(arr):
    st=set(arr)
    for i in st:
        a=arr.count(i)
        print(f"{i}->{a}") 
freq(arr)


#question 10
arr = [10, 20, 30, 20, 40, 10, 50, 30] 
def findduplicate(arr):
    st=set(arr)
    for i in st:
        if arr.count(i)>1:
            print(i)
findduplicate(arr)