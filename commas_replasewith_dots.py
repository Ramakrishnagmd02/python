input = input("please enter comma seperated values")

replace = input.replace(",", ".")
print(replace)
new = ""
for i in input:
    if i == ",":
        new += "."
    else:
        new += i 
print(new)
# one line is added here 