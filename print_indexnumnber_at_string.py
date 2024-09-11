# write a program to find index number of string an if index out of range print erroe ms
indexnumber = int(input("pease enter index number"))

name = "ramakrishna"

try:
    print(name[indexnumber])
except IndexError:
    print("index out of range")


if len(name) ==0:
    print("sring is empty")
elif indexnumber < len(name):
    print(name[indexnumber])
else:
    print("index out of range")