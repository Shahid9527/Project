from list import *
lst=[]
while True:
    n=int(input(" 1: For create list: \n 2: For Display list: \n 3: For Sort list:"))
    if n==1:
        lst=create()

    elif n==2:
        display(lst)

    elif n==3:
        n=int(input("Enter a element you want to search:"))
        search(lst,n)

    elif n==4:
        val=int(input("Enter new value:"))
        loc=int(input("Enter location:"))
        lst=insert(lst,val,loc)
        print('Value inserted successfully...')
        print('After insertion end:')
        display(lst)

    elif n==5:
        n=int(input("Enter a no to delete:"))
        lst=delete(val,n)
        print("After deletion.....",end='')
        display(lst)

    elif n==6:
        lst=sort(lst)
        print("After sorting.....",end='')
        display(lst)

    else:
        print("Invalid Choice:")
    n=int(input("For continue the program enter 1:-"))
    if (n!=1):
        break


    