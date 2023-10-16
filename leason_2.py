fruit_list = ["apple", "banana", "orange", "watermelon", "peach"]

for fruit in fruit_list:
    if fruit == "apple":
        print(fruit, "is good")
    elif fruit != "apple":
        print(fruit, "is bad")

if "grapes" in fruit_list:
    print("grapes are yummy")
else:
    print("there is no grapes")