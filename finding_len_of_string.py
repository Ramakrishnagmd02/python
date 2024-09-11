data = "capgemini"

# To find len of a string  we can use len() function or we can write len() function code

print(len(data)) # here we can get len

# implemention fo len() function:

def find_len(s):
    start_count = 0
    for char in s:
        start_count += 1
    return start_count

data = "capgemini"
exat_len = find_len(data)
print(exat_len)



# if i use simple langeage 

data = "capgemini"
count = 0
for i in data:
    count +=1
print(count)

# using while loop

data = "capgemini"
lenth = 0
index = 0
while index < len(data):
    lenth +=1
    index+=1
print(lenth)