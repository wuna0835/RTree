# !/usr/bin/env python 3
# !-*-Coding:UTF-8-*


pathIn = "D:/work/shape/errorShape.txt"
pathOut = "D:/work/shape/errorShapeID.txt"
fileWriter = open(pathOut, 'w')

with open(pathIn, 'r', newline='', encoding='UTF-8') as fileReader:
    num = 0
    for line in fileReader:
        fileWriter.write(line.strip().split(':')[0]+",")
        num += 1
fileWriter.close()
print("输入完成！"+str(num))

