age = int(input("What is your age: "))
if age <= 18:
    print("You are too small to drive")
elif 70 < age:
    print("You are too old to drive")
else:
    print("You can drive")
