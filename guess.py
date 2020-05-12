start = input('請輸入一個起始數字: ')
end = input('請輸入一個結尾數字: ')
start = int(start)
end = int(end)
count = 0
import random
r = random.randint(start, end)
while True:
    count = count + 1
    num = input('請猜一個數字: ')
    num = int(num)
    if num == r:
        print('恭喜你答對了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('答案太大了!')
    else:
        print('答案太小了!')
    print('這是你猜的第', count, '次')            