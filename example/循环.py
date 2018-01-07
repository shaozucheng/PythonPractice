# -*- coding: utf-8 -*-
"""
计算从 1+2+3...+100
使用for 循环和while 循环 两种方法

知识点： range() 函数生成数列
比如 range(5) = [1,2,3,4]


"""

mSum = 0
mList = list(range(101))
for x in mList:
    mSum = mSum + x
else:
    print(mSum)

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

'''
打印* 
'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end='')
    print('\r')
