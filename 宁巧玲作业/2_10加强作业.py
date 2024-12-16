list = []
sum = 0 # 统计个数
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j) and (i!=k) and (j!=k):
                item = 100*i + 10*j + k
                sum = sum + 1
                print(item)
                list.append(item)

print("一共有"+str(sum)+"个数")

# 写入到文件
file = open('list.txt','w')
for i in list:
    file.write(str(i)+'\n')