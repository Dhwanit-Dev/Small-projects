"""To write a Python Program to Create a binary file with roll number,name.and marks
Search for a given roll number and display the marks, if not found display appropriate
message."""
l=[]
import pickle
def create():
    f1=open("sample.dat","wb")
    opt='y'
    while opt=='y':
        roll_no=int(input("enter your roll number"))
        name=input("enter the name")
        marks=int(input("enter marks"))
        l=[roll_no,name,marks]
        pickle.dump(l,f1)
        opt=input("do you want to add more record y/n")
    f1.close()
def display():
    f=open("sample.dat","rb")
    try:
        while True:
            s=pickle.load(f)
            print(s)
    except:
        pass
def search():
    flag=0
    f=open("sample.dat","rb")
    no=int(input("enter roll number to search"))
    try:
        while True:
            s=pickle.load(f)
            if s[0]==no:
                print("found")
                print("Name of the student is",s[1])
                print("marks of the student is",s[2])
                flag=1
                break
    except:
        f.close()
    if flag==0:
        print("student not found")
while True:
    print("1... for create")
    print("2.... for display")
    print("3.... for search")
    ch=int(input("enter your choice"))
    if ch==1:
        create()
    elif ch==2:
        display()
    elif ch==3:
        search()
    else:
        break