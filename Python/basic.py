#                                 tuple
# 1.Immutable
# 2.ordered
# 3.heterogenous
# tp=(1,2,3,"hi","hello",1)
# print(tp)
# print(len(tp))
# print(type(tp))
# print(tp.count(1))
# print(tp.index("hello"))
# print(tp[4])

#                              tuple collection.

# a=1,23,4,5,"hello","hi" #->tuple
# print(a)
# print(type(a))

#                              tuple unpacking
# a,b,c=(1,2,3) #assign each value of tuple to a variable
# print(a)
# print(b)
# print(c)

# a=(1,2,3)
# b=(4,5,6)
# print(a*b) #can't multiply sequence by non-int of type 'tuple'
# print(a*2)

# adding item to a tuple
# a=(1,2,3)
# tuple->list
# lst=list(a)
# lst.append(12)
# list->tuple
# a=tuple(lst)
# print(a)

#                                                         dict
# 1.mutable
# 2.ordered
# 3.keys are unique
# student={"name":"Hitesh","roll_no":33,"branch":"csc","address":"pilani"}
# print(student)
# print(student["roll_no"])
# student["branch"]="AI"
# print(student["branch"])

# print(student.get("name"))
# print(student.keys())
# print(student.values())
# print(student.items()) # return key and value pair

#update
#copy
#deepcopy
#from keys
#setdefaults
# student.pop("name") # delete given key
# print(student)
# student.popitem() # delete a key from last
# print(student)

# student.update({"name":"Hitesh"})
# print(student)

# dic={}
# name=input("enter name:")
# roll_no=input("enter roll_no:")
# branch=input("enter branch:")
# dic["name"]=name
# dic["roll_no"]=roll_no
# dic["branch"]=branch
# print(dic)

#                                                   set
# 1.unordered
# 2.hetrogenous
# 3.no duplicate vlues
# 4.mutable

# a={1,2,3,"hello"}
# print(a)
# print(len(a))
# print(type(a))

# a.add(10)
# print(a)

# seta={1,2,3}
# setb={4,3,1,5}

# print(seta.difference(setb))
# print(seta.union(setb))
# print(seta.intersection(setb))
# print(seta.issubset(setb))

# seta.remove(2)# throw error when element not found
# seta.discard(2)#Do not throw error when element not found
# print(seta)

# PYTHON OPERATORS
# 
# Operators are special symbols used to perform operations on variables and values.
# 
# 1. ARITHMETIC OPERATORS
#    +   Addition
#    -   Subtraction
#    *   Multiplication
#    /   Division
#    //  Floor Division
#    %   Modulus (Remainder)
#    **  Exponentiation (Power)
# 
# Example:
# """
# a = 10
# b = 3
# 
# print("Arithmetic Operators")
# print("a + b =", a + b)
# print("a - b =", a - b)
# print("a * b =", a * b)
# print("a / b =", a / b)
# print("a // b =", a // b)
# print("a % b =", a % b)
# print("a * b =", a * b)
# 
# """
# 2. ASSIGNMENT OPERATORS
#    =    Assign
#    +=   Add and Assign
#    -=   Subtract and Assign
#    *=   Multiply and Assign
#    /=   Divide and Assign
#    //=  Floor Divide and Assign
#    %=   Modulus and Assign
#    **=  Power and Assign
# """
# 
# x = 10
# 
# x += 5
# print("\nAssignment Operators")
# print("x += 5 :", x)
# 
# x -= 3
# print("x -= 3 :", x)
# 
# """
# 3. COMPARISON (RELATIONAL) OPERATORS
#    ==  Equal to
#    !=  Not Equal to
#    >   Greater than
#    <   Less than
#    >=  Greater than or Equal to
#    <=  Less than or Equal to
# """
# 
# print("\nComparison Operators")
# print("a == b :", a == b)
# print("a != b :", a != b)
# print("a > b  :", a > b)
# print("a < b  :", a < b)
# print("a >= b :", a >= b)
# print("a <= b :", a <= b)
# 
# """
# 4. LOGICAL OPERATORS
#    and  Returns True if both conditions are True
#    or   Returns True if at least one condition is True
#    not  Reverses the result
# """
# 
# p = True
# q = False
# 
# print("\nLogical Operators")
# print("p and q :", p and q)
# print("p or q  :", p or q)
# print("not p   :", not p)
# 
# """
# 5. BITWISE OPERATORS
#    &   AND
#    |   OR
#    ^   XOR
#    ~   NOT
#    <<  Left Shift
#    >>  Right Shift
# """
# 
# print("\nBitwise Operators")
# print("a & b  :", a & b)
# print("a | b  :", a | b)
# print("a ^ b  :", a ^ b)
# print("~a     :", ~a)
# print("a << 1 :", a << 1)
# print("a >> 1 :", a >> 1)
# 
# """
# 6. MEMBERSHIP OPERATORS
#    in       Checks if value exists in sequence
#    not in   Checks if value does not exist in sequence
# """
# 
# numbers = [1, 2, 3, 4, 5]
# 
# print("\nMembership Operators")
# print("3 in numbers     :", 3 in numbers)
# print("10 in numbers    :", 10 in numbers)
# print("10 not in numbers:", 10 not in numbers)
# 
# """
# 7. IDENTITY OPERATORS
#    is       Returns True if both variables refer to same object
#    is not   Returns True if variables refer to different objects
# """
# 
# list1 = [1, 2, 3]
# list2 = list1
# list3 = [1, 2, 3]
# 
# print("\nIdentity Operators")
# print("list1 is list2     :", list1 is list2)
# print("list1 is list3     :", list1 is list3)
# print("list1 is not list3 :", list1 is not list3)
# 
# """
# SUMMARY
# 
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Bitwise Operators
# 6. Membership Operators
# 7. Identity Operators
# 
# These are the 7 major types of operators in Python.
# """