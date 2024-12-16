#  √2在区间[1, 2]内，所以我们定义最小值为low = 1，最大值high = 2

low = 1.0
high = 2.0

while abs(low ** 2 - 2) > 1e-10:
    mid = (low + high) / 2
    if mid ** 2 < 2:
        low = mid  # mid可能是√2，向右查找
    else:
        high = mid  # mid大于√2，向左查找

result = round(mid,3)

file = open("根号2.txt","w")

file.write(str(result))
file.close()
