# assignment 3

# QUESTION1
"""program to count number of occurrences of each word or character"""

original_string=input("enter the string= ")
a=" "
string_1=original_string.lower()    #converting the string into lower case and assigning it to a new variable

# condition used to check if " " is there is string so that specific function can be called
if a in string_1:
    def word_times(string_1):              # word_times is a function used to count occurrence of word
        string_1 = string_1.split()
        list_of_words = []

        for word in string_1:
            if word not in list_of_words:
                list_of_words.append(word)
        for word in range(0, len(list_of_words)):
            print("frequency of", list_of_words[word], "is: ", string_1.count(list_of_words[word]),"times")
    word_times(string_1)

else:                # character_times is a function used to count occurrence of characters in case only 1 word is given
    def character_times(string_1):
        if len(string_1) >=1:
            list_of_character=[]
            for character in string_1:
             if character not in list_of_character:
                list_of_character.append(character)
                print(character,"occured",string_1.count(character),"times")
    character_times(string_1)
# count function was used to count te occurrences
print("-"*50)






# QUESTION 2

"""program to find next date """

year=int(input("input a year (1800-2025)= "))
if year in range(1800,2026):
    if (year%400==0):
        Leap_Year=True
    elif (year % 4 == 0):
        Leap_Year = True             # code to detect leap year
    elif (year%100==0):
        Leap_Year=False
    else:
        Leap_Year=False
else:
    print("enter year in given range")
    exit()   # in the program exit() has been used so that if user enters data out of given condition;code exits



month=int(input("input a month (1-12)= "))
if month in range(1,13):
    if month in (1,3,5,7,8,10,12):
        month_length=31
    elif month in (4,6,9,11):
        month_length=30
    elif month==2:
        if Leap_Year:
            month_length=29
        else:
            month_length=28
else:
   print("please enter month in given range")
   exit()

day=int(input("input a day (1-31)= "))
if day in range(1,32):
    if day<month_length:
        day+=1
    else:
        day=1
        if month==12:
            month=1
            year+=1
        else:
            month+=1
else:
    print("please enter day in given range")
    exit()

date=f"the next date is {day}-{month}-{year}"
print(date)
print("-"*50)





# QUESTION 3

"""program to create a list of tuples with 1st element as number and 2nd as square of that number """

n=int(input("""enter the amount of numbers whose square you wish to find 
(then enter the numbers one by one by pressing enter key)== """))

first_number=[]
for i in range(0,n):
    first_num=int(input())
    first_number.append(first_num)

squared_number=[]
for i in range(0,n):
    second_num=first_number[i]**2
    squared_number.append(second_num)

answers=list(zip(first_number,squared_number))
# zip function is used so that it links the 1st num with its square and return it as a tuple
print(answers)
print("-"*50)




# QUESTION 4

"""program to check grade and performance"""

grade = int(input("please enter grade between 4 and 10= "))
if grade == 10:
    print("Your Grade is 'A+' and Outstanding Performance")
elif grade == 9:
    print("Your Grade is 'A' and Excellent Performance")
elif grade == 8:
    print("Your Grade is 'B+' and Very Good Performance")
elif grade == 7:
    print("Your Grade is 'B' and Good Performance")
elif grade == 6:
    print("Your Grade is 'C+' and Average Performance")
elif grade == 5:
    print("Your Grade is 'C' and Below Average Performance")
elif grade == 4:
    print("Your Grade is 'D' and Poor Performance")
else:
    print("There is an error please confirm your marks again")
# exit function has been used because if persons enters input out of range code exits
    exit()
print("-"*50)




# QUESTION 5

""" program to print the given pattern """

n = 6
for i in range(n):
    # loop used for printing spaces
    for j in range(i):
        print(' ', end='')
    # loop used for printing alphabet
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')       # ascii values have been used to print the alphabets
    print()
print("-"*50)




# QUESTION 6

"""student details"""

details_dict = {}
user_sid = int(input("enter the sid= "))
user_name = input("enter the name= ")
details_dict[user_sid] = [user_name]

"""if you will enter any character except y/n then loop will close and output will be given according to value 
entered till now"""

def again():
    cal_again = input("""
    do you want to call again?
    please type y for yes and n for no
    """)

    if cal_again == "y":
        user_sid = int(input("enter the sid= "))
        user_name = input("enter the name= ")
        details_dict[user_sid] = [user_name]
        again()
    elif cal_again == "n":
        print(" ")
again()

# part a = students details stored in dictionary
print("details of the students are as follows= ", details_dict)

# part b = sorted dictionary using student names
sort_by_values={k: v for k,v in sorted(details_dict.items(), key=lambda v: v[1])}
print("\nsorted dictionary using names is= ", sort_by_values)

# part c = sorted dictionary using sid
print("\nsorted dictionary using sid is= ", sorted(details_dict.items()))

# part d = code to print name of student whose sid has been entered
word1=int(input("\nenter the sid of student whose name you want to search= "))
if word1 in details_dict.keys():
    print("name of student with sid",word1,"is",details_dict[word1])
else:
    print("sorry no match found in database")
print("-"*50)





# QUESTION 7

"""fibonacci sequence calculator"""

n=int(input("for how many terms you want the sequence= "))
fibonacci_list=[]

# program used to calculate fibonacci sequence
n1,n2=0,1
i=0
if n<=0:
    print("invalid input")
elif n==1:
    print("the fibonacci sequence for",n,"term is",n1)
else:
    print("fibonacci sequence is= ")
    while (i<n):
        print(n1)
        a_n=n1+n2
        fibonacci_list.append(n1)
        n1=n2
        n2=a_n
        i+=1

# program used to calculate sum of resultant fibonacci sequence
sum = 0
for i in range(0,len(fibonacci_list)):
    sum+=fibonacci_list[i]
    average_1=sum/len(fibonacci_list)
print("the average of resultant fiboncci series is= ",average_1)
print("-"*50)




# QUESTION 8

"""program used to do operations on given sets"""

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

print("Given sets are= ")
print("set1= ", set1)
print("set2= ", set2)
print("set3= ", set3)

# part a
A = set1 | set2
B = set1 & set2
part_a = A-B
print("\nset of all elements that are in set1 and set2 but not both is= ", part_a)

# part b
part_b = (set1 - (set2 | set3)) | (set2 - (set1 | set3)) | (set3 - (set1 | set2))
print("\nset of all elements that are only in one of the three sets= ", part_b)

# part c
part_c = (set1 & set2) | (set2 & set3) | (set1 & set3) - (set1 & set2 & set3)
print("\nset of elements that are exactly in two of the three sets= ", part_c)

# part d
part_d = set(range(1, 11))-set1
print("\nset of integers in range 1-10 that are not in set1= ", part_d)

# part e
part_e = set(range(1, 11))-(set1 | set2 | set3)
print("\nset of integers in range 1-10 that are not in any of the set1,set2,set3", part_e)
print("-"*50)