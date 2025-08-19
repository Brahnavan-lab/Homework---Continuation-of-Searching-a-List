list1 = [5,14,3,19,28]
search = int(input("Enter a search item"))
count = 0
for i in range(len(list1)):
    if list1[count] == search:
        print("Well done. The search item has been found. It is in position",count+1)
    elif list1[count] != search:
        print("This is not search item. Try again")
        count = count+1
else:
    print("You have reached the end of the list. The value is not in the list")
    


