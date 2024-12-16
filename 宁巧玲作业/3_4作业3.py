# 鸡公 x   最多20只
# 鸡母 y   最多33只
# 鸡崽 z   最多100只

file = open("鸡.txt",'w')
for x in range(21):
    for y in range(34):
        for z in range(101):
            if 5*x + 3*y + z/3 == 100 and x+y+z == 100:
               file.write(str(x)+','+str(y)+','+str(z)+'\n')

file.close()
