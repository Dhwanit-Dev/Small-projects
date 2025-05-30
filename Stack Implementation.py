s = []
top = -1

# Defining Functions

def isEmpty(top):
    if top == -1:
        return True
    else:
        return False

def push(top):
    a = input("Enter data to be pushed: ")
    s.append(a)
    top = top + 1
    print(s)
    return top

def pop(top):
    if isEmpty(top):
        print("Underflow!")
    else:
        s.pop()
        top = top - 1
    print(s)
    return top

def peek(top):
    if isEmpty(top):
        print("Underflow!")
    else:
        print("Top of the list is: ", s[top])

def display(top):
    if isEmpty(top):
        print("Stack is empty!")
    else:
        print("Stack contents (top to bottom):")
        for i in range(top, -1, -1):
            print(s[i])

# Main program

while True:
    print("""
    1... push
    2... pop
    3... peek
    4... display
    5... exit""")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        top = push(top)
    elif ch == 2:
        top = pop(top)
    elif ch == 3:
        peek(top)
    elif ch == 4:
        display(top)
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Error. Try again.")