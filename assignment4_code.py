print("QUESTION 1")

# here n refers to number of discs used 
#source refers to rod 1 , intermediate refers to rod 2 and destination refers to rod 3


def TowerofHanoi(n, source,destination, intermediate):
    if n == 1:     # base case 
        print("move disk 1 from source", source, "to destination", destination)
        return
    TowerofHanoi(n-1, source, intermediate, destination)
    print("move disk", n, "from source", source, "to destination", destination)
    TowerofHanoi(n-1, intermediate, destination, source)

n = 3
TowerofHanoi(n, "Rod_1", "Rod_2", "Rod_3")

print("\n")
print("-"*50)

print("QUESTION 2")


def factorial(n):    # function for factorial
    value=1
    for i in range(1,n+1):
        value=value*i
    return value


# # dont enter negative number otherwise code will exit
n=int(input("enter the number of rows = "))
if n<=0:
    exit()
else:
    print("using iterative method")                              ## iterative method
    for row in range(n):
        for col in range(n-row+1):
            print(end=" ")
        for col in range(row+1):
            combinatorics=(factorial(row)//(factorial(row-col)*factorial(col)))   # this represents nCr
            print(combinatorics,end=" ")
        print("")
print("\n")

print("using recusrive method")                                 ## recursion method
def pascals_Triangle(n):
        if n == 1:
            return [[1]]
        else:
            answer=pascals_Triangle(n-1)
            new_row = [1]
            last_row=answer[-1]
            for i in range(len(last_row)-1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row += [1]
            answer.append(new_row)
        return answer

triangle=pascals_Triangle(n)
for i in triangle:
        print(i)   
print("\n")
print("-"*50)




print("QUESTION 3")

first_num=int(input("enter the divident="))
second_num=int(input("enter the divisor="))
quotient=first_num//second_num
remainder=first_num%second_num
print(f"the quotient is {quotient} and remainder is {remainder}")
print("\n")

#part_a=check if values are callable or not
print("part_a=")
a=print("value of first_num is",callable(quotient))
b=print("value of second_num is",callable(remainder))
c=print("value of quotient is",callable(first_num))
d=print("value of remainder is",callable(second_num))
print("\n")


#parT_b=Check whether all the values are non zeros or not
print("part_b=")
if (quotient==0 and remainder!=0):
    print("only the quotient is zero")
if (remainder==0 and quotient!=0):
    print("only the remainder is zero")
if(quotient!=0 and remainder!=0):
    print("both the quotient and remainder are not zero")
if(quotient==0 and remainder==0):
    print("both the quotient and remainder are zero")
print("\n")

#part_c
print("part_c=")
list=list()
list.append(quotient)
list.append(remainder)
list.append(4)
list.append(5)
list.append(6)
new_list=[]
for i in list:
    if i>4:
        new_list.append(i)
print("new list is=",new_list)
print("\n")

#part_d=Convert the result into set datatype.
print("part_d=")
set=set(new_list)
print("the set is=",set)
print("\n")

#part_e=Make that set immutable.
print("part_e=")
print("immutable set is=",frozenset(set))
print("\n")

#part_f=Evaluate the maximum value from set and find out its hash value
print("part_f=")
print("max value is=",max(set))
print("hash value is=",hash(max(set)))
print("\n")
print("-"*50)





print("QUESTION 4")

class Student():

    def __init__(self, name, sid):
        self.name = name
        self.sid = sid

    def details(self):
        return(f"name of child is {self.name} and roll no is {self.sid}")

    def __del__(self):    #destructor has been called 
        print("details of the object have been deleted successfully")

    
Dheeraj = Student("Dheeraj", 21104030)
print(Dheeraj.details())

del Dheeraj  # object has been deleted
print("\n")
print("-"*50)


print("QUESTION 5")

class Employee_Details():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        return(f"name of employe is {self.name} and his/her salary is {self.salary}")

Mehak = Employee_Details("Mehak", 40000)
Ashok = Employee_Details("Ashok", 50000)
Viren = Employee_Details("Viren", 60000)
print(Mehak.details())
print(Ashok.details())
print(Viren.details())
print("\n")

# part A
Mehak.salary = 70000
print("congo mehak ur salary has been updated to= ", Mehak.salary)
print("\n")

# part B
del Viren       #del function as been called to delete object viren
print("details of viren have been deleted successfully")
print("\n")
print("-"*50)




print("QUESTION 6")

george_word=input("george please enter a word=").lower()

#concept of anagrams has been used here 
def anagrams(word):
    if word=="":
        return [word]
    else:
        ans=[]
        for char in anagrams(word[1:]):
            for pos in range(len(char)+1):
                ans.append(char[:pos]+word[0]+char[pos:])
        return ans
possible_combination=anagrams(george_word)       
# possible_combination variable stores all the anagrams possible

barbie_word=input("barbie please enter a word=").lower()
if barbie_word in possible_combination:
    print("the friendship is real")
else:
    print("the friendship is not real")
print("-"*50)
