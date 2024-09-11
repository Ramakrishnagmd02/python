# enter a string and if we provide index number that is not have remove from string
#if there is no string print emptyif index number if less then

name = input("please enter name")

index_number = int(input("please enter index number"))

if len(name) < index_number:
    print("index out of range")
else:
    s = ""
    for i in range(len(name)):
        if i != index_number:
            s += name[i]
    print(s)
