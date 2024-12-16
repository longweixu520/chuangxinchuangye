import math
def square_number(n):
    if n < 0:
        return False  # 负数不是完全平方数
    square_root = int(math.sqrt(n))  # 计算平方根并取整 ,比如100的平方根是10
    return square_root * square_root == n  # 检查平方根的平方是否等于原数，如果10*10 == 原来的数字n，即100 ，就是True


# 示例用法
number = 16
if square_number(number):
    print(f"{number} 是完全平方数")
else:
    print(f"{number} 不是完全平方数")
