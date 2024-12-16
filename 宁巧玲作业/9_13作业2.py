def judge():
    # abcd * 9 = dcba
    # 首先abcd是一个四位数，他的9被dcba也是四位数
    # 我们分析一下，四位数是范围在1000——9999之间的
    for number in range(1000, 10000):
        # 我们分别求出a,b,c,d代表原来四位数的千位，百位，十位，个位
        a = int(number / 1000)
        b = int((number % 1000) / 100)
        c = int((number % 100) / 10)
        d = int(number % 10)

        # 那么我们原来的四位数abcd就是 a*1000 + b*100 + c*10 + d，也就是number
        # 乘以9后的四位数dcba就是 d*1000 + c*100 + b*10 + a
        # 接下来进行一下判断, abcd的9倍是否等于dcba
        if (number * 9) == (d * 1000 + c * 100 + b * 10 + a):
            print(f"abcd: {number}, dcba: {d * 1000 + c * 100 + b * 10 + a}")
            return True

    return False


judge()
