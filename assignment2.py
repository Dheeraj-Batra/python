"""
#question 1
mystr="Python is a case sensitive language"
print("original string is= ",mystr)

#part a=find length of string
print(len(mystr))

#part b=reverse the order of the string
print(mystr[::-1])

#part c=store “a case sensitive” in new string
new_string=mystr[10:26]
print(new_string)

#part d=replace
print(mystr.replace("a case sensitive","object oriented"))

#part e=find index of "a"
print(mystr.find("a"))

#part f=remove the white spaces
print(mystr.replace(" ",""))
"""

"""
#QUESTION 2
name="Dheeraj Batra"
sid=21104030
department="Electrical Engineering"
cgpa=9.9
print("Hey,",name,"Here!\nMy sid is",sid,"\nI am from",department,"department and my cgpa is ",cgpa)
"""

"""
#QUESTION 3
a=56
b=10
print(a & b)     #and operator
print(a|b)       #or operator
print(a^b)       #xor operator
print(a<<2)      #Left shift a by 2 bits
print(b<<2)      #Left shift b by 2 bits
print(a>>2)      #Right shift a by 2 bits
print(b>>4)      #Right shift b by 4 bits
"""

"""
#question 4  print max number
a=float(input("enter 1st number= "))
b=float(input("enter 2nd number= "))
c=float(input("enter 3rd number= "))

if a>b:
    if a>c:
        print("max number is=",a)
    else:
        print("max number is=",c)
else:
    if b>c:
        print("max number is=",b)
    else:
        print("max number is=",c)
"""

"""
#QUESTION 5
enter_string=input("enter the string= ")
if "name" in enter_string:
    print("yes")
else:
    print("no")
"""

""""
#question 6
side1=int(input("enter 1st side= "))
side2=int(input("enter 2nd side= "))
side3=int(input("enter 3rd side= "))

if side1>(side2+side3) or side2>(side3+side1) or side3>(side1+side2):
    print("NO triangle is not possible")
else:
     print("YES triangle is possible")
"""
