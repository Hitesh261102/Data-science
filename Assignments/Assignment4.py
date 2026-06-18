#question 1
lst=[1,2,31,4,6,7,13,11,12,3]
for i in lst:
    count=0
    for j in range(2,(int)(i/2)+1):
        if i%j==0:
            count+=1
    if count==0:
        print(i,end=" ")

#question 2
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()

#question 3
def counteven(lst):
    count=0
    sum=0
    for i in lst:
        if i%2==0:
            count+=1
        else:
            sum+=i
    print("count of even element is:",count)
    print("sum of odd element is:",sum)
lst=[1,2,3,4,5]
counteven(lst)

#question 4
def simpleinterest(P,R=5,T=2):
    SI=(P*R*T)/100
    return SI
# postional argument 
si1=simpleinterest(10000)
print("Simple Interest:",si1)
# keyword argument
si2=simpleinterest(P=50000)
print("Simple Interest:",si2)

#question 5,6
class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def garde(self):
        if self.marks >=90:
            print("you got A+")
        elif self.marks >=80:
            print("you got A")
        elif self.marks>=70:
            print("you got B")
        elif self.marks>=60:
            print("you got c")
        elif self.marks>=50:
            print("you got d")
        elif self.marks>=40:
            print("you got E")
        else:
            print("you fail")
st=Student("Hitesh",98)
st1=Student("abc",48)
st.garde()
st1.garde()


#question 7
class BankAccount:
    
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount>self.__balance:
            print("insufficent balance")
        else:
            self.__balance-=amount
    def displaybalance(self):
        print("balance:",self.__balance)
a=BankAccount("abc",100000)
a.deposit(1000)
a.displaybalance()


#question 8
try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print("Division:",a/b)
except ZeroDivisionError as e:
    print("error:",e)
except ValueError as e:
    print("error:",e)

# question 9
file=open("student","a")
file.write("name:Hitesh\tmarks:90")
file.close()
file=open("student","r")
print(file.read())
file.close()

#question 10
total = 0
count = 0
try:
    with open("data", "r") as file:
        for line in file:
            number = float(line.strip())
            total += number
            count += 1
    
    if count > 0:
        average = total / count
        print("Total =", total)
        print("Average =", average)
except FileNotFoundError as e:
    print("error:",e)