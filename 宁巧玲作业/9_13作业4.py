def is_prime(n):
    if n <= 1:
        return False  # 0 和 1 不是素数
    if n <= 3:
        return True  # 2 和 3 是素数
    # 排除偶数和3的倍数
    if n % 2 == 0 or n % 3 == 0:
        return False

    # 检查从 5 开始到 sqrt(n) 的所有奇数
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


number1 = 29
if is_prime(number1):
    print(f"{number1} 是素数")
else:
    print(f"{number1} 不是素数")


# 另外其实还有一种很笨拙的方法,宁巧玲同学见下

def is_prime_naive(n):
    # 小于1的数字肯定不是
    if n <= 1:
        return False
    # 对于大于2的的数字，只要在2到它本身之前有一个数能够被它整除，那么他也不是，因为素数只能被他自己和1整除
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


number2 = 15
if is_prime_naive(number2):
    print(f"{number2} 是素数")
else:
    print(f"{number2} 不是素数")
