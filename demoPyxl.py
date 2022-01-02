a, b, c = 4, 6.4, "A String."

print("{}, {}, {}, {}".format(a, b, c, " -By Rahul"))
print(f"{a} is the function of {b} and basically {c}")

print(a, b, c)
print(type(a))
print(type(b))
print(type(c))
print("...........")

value = [22, 33, 44, "Moshiur", 55]
print(value)
print(value[3])
print(value[0])
print(value[-1])
value.insert(4, "Khan")
print(value)
value.append(66)
print(value)
print("..........")
value[3]="MOSHIUR"
print(value)
value[4]= "KHAN"
print(value)
del value[6]
print(value)
value.append(66)
print(value)
print(".......")
newDict = {"a": 2.4, 4: "Pam", "c": "String"}
print(newDict)
print(newDict[4])
print(newDict["c"])
empty_dict = {}
empty_dict["firstname"]="Moshiur"
empty_dict["lastname"]="Khan"
empty_dict["gender"]="Male"
print("....................")
print(empty_dict)
print(newDict)
print("::::::::::::::")
temperature = int(input("What is present temperature now: "))

if temperature >= 15:
    print("Its a warm temperature today.")
elif temperature >= 10:
    print("Its a cold temperature today.")
elif temperature == 9:
    print("Its very cold.")
else:
    print("Take care.")
print("'''''''''''''''''")













































