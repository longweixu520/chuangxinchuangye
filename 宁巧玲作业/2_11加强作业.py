import math

# 判断是不是完全平方数
def is_perfect_square(n):
    # 检查一个数是否为完全平方数
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

items = []
for i in range(0,1001):
    # 两个条件都满足就把它放到列表里面
    if is_perfect_square(i+100) and is_perfect_square(i+100+168):
        items.append(i)
        print(i)

file = open("result.txt","w")
for item in items:
    file.write(str(item) + "\n")
