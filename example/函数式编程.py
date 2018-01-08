"""
函数式编程

"""


def f(x):
    return x * x


mList = list(range(10))
r = map(f, mList)

print(list(r))

"""
filter() 函数过滤
"""


def is_add(x):
    return x % 2 == 1


list(filter(is_add, [1, 2, 4, 5, 6, 9, 10, 15]))

print(list(filter(is_add, list(range(100)))))

print(list(filter(is_add, [1, 2, 3, 4, 5])))

"""
sorted 排序
"""
print("-------------------------------------------------------")
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
