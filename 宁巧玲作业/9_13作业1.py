def every_value(number):
    # 以9876为例
    # 个位 = 9876 mod 10 = 6
    # 十位 = 9876 mod 100 / 10 = 76 / 10 = 7
    # 百位 = 9876 / 100 mod 10 = 98 mod 10 = 8
    # 千位 = 9876 /1000 = 9
    # 记住一定要转化为 int 类型，不然就是小数了，毕竟python不是c语言
    ge = int(number % 10)
    shi = int(number % 100 / 10)
    bai = int(number / 100 % 10)
    qian = int(number / 1000)
    return ge, shi, bai, qian


print(every_value(9876))
