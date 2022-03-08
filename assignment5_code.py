###  QUESTION 1
from tkinter import *
from tkinter import font

def find_gst():                  # formula to find gst rate
    org_cost=int(org_price.get())
    net_cost=int(net_price.get())
    gst_rate=((net_cost - org_cost) * 100) / org_cost
    labell=Label(text=f"the gst rate is {gst_rate}%",font="calibre 14 bold")
    labell.grid(row=5,column=2)

win=Tk()
win.configure(background="light blue")
win.geometry("500x500")
win.title("QUESTION 1")
label_1=Label(win,text="Original price",bg="white",relief="ridge",font="calibre 14 bold")
label_1.grid(row=1,column=1,padx=10,pady=10)
label_2=Label(win,text="Net price",bg="white",relief="ridge",font="calibre 14 bold")
label_2.grid(row=2,column=1,padx=10,pady=10)
# button to calculate gst and display final ans
button_1=Button(win,text="Calculate",padx=3,pady=3,bg="white",font="calibre 14 bold",command=find_gst)
button_1.grid(row=3,column=2,padx=10,pady=10)

# code to get entry from user 
org_price=Entry(win)
org_price.grid(row=1,column=2,padx=10,pady=10)
net_price=Entry(win)
net_price.grid(row=2,column=2,padx=10,pady=10)
win.mainloop()





###  QUESTION 2
from tkinter import *
import calendar
# function to fetch the calender of that year
def show_calender():
    new_win=Tk()
    new_win.title("calender")
    new_win.geometry("700x700")
    fetch_year = int(year_field.get()) # get as been used to store the value of year, given by user
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(new_win, text = cal_content, font = "Consolas 10 bold")
    cal_year.grid(row = 5, column = 1, padx = 20)
    new_win.mainloop()


if __name__ == "__main__" :
# parent gui to ask the user for year whose calender he wants
    win = Tk()
    win.config(background = "light blue")
    win.title("QUESTION 2")
    win.geometry("250x140")
    label1 = Label(win, text = "CALENDAR", bg = "white",font = "lucida 28 bold")
    label2 = Label(win, text = "ENTER YEAR", bg = "light green")
    year_field = Entry(win)
    Show = Button(win, text = "SHOW CALENDER", fg = "Black",bg = "Red",command=show_calender)
 
    label1.grid(row = 1, column = 1)
    label2.grid(row = 2, column = 1)
    year_field.grid(row = 3, column = 1)
    Show.grid(row = 4, column = 1)
    win.mainloop()







###  QUESTION 3
from multiprocessing import Value
from tkinter import *

# code to set command for button C and =
def click(event):
    global entry_val
    text=event.widget.cget("text")
    print(text)
    if text == "=":
        if entry_val.get().isdigit():
            value=int(entry_val.get())
        else:
            value=eval(entry_screen.get()) 
#eval function evaluates string as expression and gives output in int
        entry_val.set(value)
        entry_screen.update()
    elif text == "C":
        entry_val.set("")
        entry_screen.update()
    else:
        entry_val.set(entry_val.get()+text)
        entry_screen.update()


win=Tk()
win.geometry("600x800")
win.title("QUESTION 3")

Label1=Label(text="CALCULATOR",font="lucida 40 ")
Label1.pack()

# code to get entry 
entry_val=StringVar()
entry_val.set("")
entry_screen=Entry(win,textvariable=entry_val,font="lucida 35 bold")
entry_screen.pack(fill=X)

# code used to make buttons C and =
f=Frame(win,bg="white")
b=Button(f,text="C",font="lucida 35 bold",padx=13.5,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 35 bold",padx=13.5,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
f.pack()

# code used to make buttons 9,8,7 and +
f=Frame(win,bg="white")
b=Button(f,text="9",font="lucida 35 bold",padx=15,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 35 bold",padx=15,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="7",font="lucida 35 bold",padx=16,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="+",font="lucida 35 bold",padx=9,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
f.pack()

# code used to make buttons 6,5,4 and -
f=Frame(win,bg="white")
b=Button(f,text="6",font="lucida 35 bold",padx=15,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 35 bold",padx=15,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="4",font="lucida 35 bold",padx=15,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="-",font="lucida 35 bold",padx=15,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
f.pack()

# code used to make buttons 3,2,1 and *
f=Frame(win,bg="white")
b=Button(f,text="3",font="lucida 35 bold",padx=15,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 35 bold",padx=15,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="1",font="lucida 35 bold",padx=15,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="*",font="lucida 35 bold",padx=15,pady=12)
b.pack(side="left")
b.bind("<Button-1>",click)
f.pack()

# code used to make buttons 0,1,% and /
f=Frame(win,bg="white")
b=Button(f,text="0",font="lucida 35 bold",padx=14,pady=17)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text=".",font="lucida 35 bold",padx=22,pady=17)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="%",font="lucida 35 bold",padx=8,pady=17)
b.pack(side="left")
b.bind("<Button-1>",click)
b=Button(f,text="/",font="lucida 35 bold",padx=17,pady=17)
b.pack(side="left")
b.bind("<Button-1>",click)
f.pack()
win.mainloop()







### QUESTION 4
print("QUESTION 4")
# code to make partition 
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# code for quicksort
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

n = int(input("enter the amount of numbers you want to sort= "))
print("enter the numbers by giving space between them keeping in mind test was of 100Marks")
list1 = list(map(int,input().split()))
print("list before sorting is=",list1)
quickSort(list1, 0, n - 1)
print("list after sorting is= ", list1)
print("-"*50)





### QUESTION 5
print("QUESTION 5")
# code to define function for binary search
def binary_search(arr,n,low,high):
    if low<=high:
        mid=(low+high)//2
        if arr[mid]==n:
            return mid

        elif arr[mid]<n:
            return binary_search(arr,n,mid+1,high)
        else:
            return binary_search(arr,n,low,mid-1)
    else:
        return -1


n=int(input("enter the amount of numbers you want in list= "))
list1=list(map(int,input().split()))
# part a= sort the list 
list1.sort()
print("list is= ",list1)

# part b= check if number occured in the list
search_num=int(input("which numbers index u want= "))
if search_num not in list1:
    print(f"number {search_num} isnt in the list")

else:
    result=binary_search(list1,search_num,0,len(list1))
    if result!=-1:
        print(f"the number {search_num} is found at index {result}")
    else:
        pass

#part c= check the occurence of the word
print(f"the number {search_num} occured {list1.count(search_num)} times in the given list")
print("-"*50)
