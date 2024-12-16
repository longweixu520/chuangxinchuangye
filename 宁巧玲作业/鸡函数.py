def ji_number():
    with open("鸡的数量1.txt",'w')as f:
        ## 鸡爸爸最多20只，鸡妈妈最多33只，买百只鸡，所以鸡宝宝最多100只
        for farther in range(20+1):
            for mother in range(33+1):
                for baby in range(100+1):
                    # father，mother，baby总共100只鸡，花了100元钱
                    if farther+mother+baby == 100 and 5*farther +3*mother + baby/3 == 100:
                        print(f"鸡爸爸{farther}只，鸡妈妈{mother}只，鸡宝宝{baby}只")
                        f.write(f"鸡爸爸{farther}只，鸡妈妈{mother}只，鸡宝宝{baby}只\n")
                    else:
                        pass
    return 0
        

ji_number()


