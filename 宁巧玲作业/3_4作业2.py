import math

def f(x, y):
    return math.exp(x-y) * (x ** 2 - 2 * y ** 2)


max_f = -float('inf')
min_f = float('inf')

max_record = (0, 0)
min_record = (0, 0)

# 生成x和y的取值范围，手动定义步长为0.2
x_values = [i * 0.2 for i in range(-500, 501)]  # 从 -100 到 100，步长为0.2
y_values = [i * 0.2 for i in range(-500, 501)]  # 从 -100 到 100，步长为0.2

# 遍历x和y的所有组合，寻找最大值和最小值
for x in x_values:
    for y in y_values:
        value = f(x, y)
        if value > max_f:
            max_f = value
            max_record = (x, y)
        if value < min_f:
            min_f = value
            min_record = (x, y)

with open("最大最小.txt", 'w') as f:
    f.write(f"函数f(x, y)最大值为：{max_f:.3f}，对应的 (x, y) 为：({max_record[0]:.3f}, {max_record[1]:.3f})\n")
    f.write(f"函数f(x, y)最小值为：{min_f:.3f}，对应的 (x, y) 为：({min_record[0]:.3f}, {min_record[1]:.3f})")

print("已经写入文件了，不信你看")