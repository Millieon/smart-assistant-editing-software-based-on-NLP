str1='中国农业大学信息与电气工程学院'
str2='中国农业大学信电学院'

L1=len(str1)+1
L2=len(str2)+1


matrix= [[0 for i in range(L1)] for i in range(L2)]

for i in range(1,L1):
   matrix[0][i]=matrix[0][i-1]+1

for j in range(1,L2):
   matrix[j][0]=matrix[j-1][0]+1

for i in range(1,L2):
    for j in range(1, L1):
        if str1[j-1]==str2[i-1]:
            matrix[i][j]=min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1])
        else:
            matrix[i][j]=min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+2)
print(matrix[L2-1][L1-1])
#

import xlrd

# import pandas as pd
# list=pd.read_excel('E:\\PyCharm\\EditorAssistance\\chart.xlsx',usecols=[0],names=None)
# list = list.values.tolist()
# StandardName = []
# for s_li in list:
#     StandardName.append(s_li[0])
#
# print(StandardName)
# def takeSecond(elem):
#     return elem[1]
#
# list=[[1,3],[2,5],[3,6],[4,1]]
# list.sort(key=takeSecond)
# print(list)