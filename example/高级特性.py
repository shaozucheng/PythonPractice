"""
python 高级编程
1，切片

L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
L[-1] 取倒数第一个数据

"""

L = list(range(100))

print(L[0:10])
print(L[-1])

"""
生成集合 list(range(1,10))
"""

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
