for abcd in range(1000, 10000):  # 四位数范围
        dcba = abcd * 9             # 乘以9
        if str(dcba) == str(abcd)[::-1]:  # 判断是否为反转
            print(f"abcd: {abcd}, dcba: {dcba}")

