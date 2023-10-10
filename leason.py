import random

rn = random.randint(1, 100)

number = int(input("输入数字: "))
while True:
    if number > rn:
        print("太高了")
        number = int(input("重新输入数字: "))
    elif number < rn:
        print("太低了")
        number = int(input("重新输入数字: "))
    else:
        break

print("猜对了！")