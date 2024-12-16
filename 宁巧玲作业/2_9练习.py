filename = "9x9.txt"

# 打开文件写入
with open(filename, "w") as file:
    for i in range(1, 10):
        for j in range(1, i + 1):
            file.write(f"{j}*{i}={i * j}\t")
        file.write("\n")
