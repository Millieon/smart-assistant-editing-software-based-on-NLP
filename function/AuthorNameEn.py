# encoding=utf-8


from docx import Document
import jieba
jieba.setLogLevel(20)
import re


def judge_capitolization(str1):
    mark=0
    for i in str1:
        if i > 'Z' or i <'A' :
            mark+=1
    if mark != 0:
        return False
    else:
        return True

file = Document("E:\PyCharm\EditorAssistance\TEST1.docx")     #读取文档内容
str2 = re.sub("[0-9\!\%\[\]\,\。\。\，\.]", "", file.paragraphs[7].text)
print(str2)
str1=str2.split()
AuthorSerialNum=0
mark=0
Info=[]
NameInfo=[]
for i in str1:
    Info.append(i)
    AuthorSerialNum=AuthorSerialNum+0.5
    mark+=1
    if mark==2:
        Info.append(str(int(AuthorSerialNum)))
        NameInfo.append(Info)
        Info = []
        mark = 0

for i in NameInfo:
    if judge_capitolization(i[0])==True:
        print("第"+i[2]+"位作者的英文名姓字母为大写"+i[0])
    else:
        print("第" + i[2] + "位作者的英文名姓字母不全为大写" + i[0])





