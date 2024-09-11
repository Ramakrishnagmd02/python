#first and last three letters and if less tehn 6 letters pringt empy

name = input("please enter a string")
fir,secon = [name[:3:]],[name[-3::]]

if len(name) < 6:
    print("")
else: 
    print(fir+secon)


#
if len(name) < 6:
    result = ""
else:
    result = name[:3:] + name[-3::]
print(result)

new = "" if len(name) <6 else name[3::]+name[-3::]
print(new)
    
