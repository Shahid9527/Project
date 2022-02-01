def create():
    lst=[]
    while True:
        n=int(input("Enter value to list:"))
        lst.append(n)
        n=int(input("If you want to add more element press 1:"))
        if n!=1:
            break;
    return lst

def display(lst):
    print("The list is:")
    for i in lst:
        print(i)

def delete(lst,val):
    lst.remove(val)
    return lst

def sort(lst):
    lst.sort()
    return lst

def search(lst,val):
    print(val,'Element found at position',lst.index(val)+1)

def insert(lst,val,loc):
    lst.insert(loc,val)
    return lst
