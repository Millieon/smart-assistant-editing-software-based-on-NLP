# encoding=utf-8


from docx import Document
import jieba.posseg as pseg
import jieba
jieba.setLogLevel(20)
import re

def company_order(list1):
    template = list1[0]
    mark = 0
    for ele in list1:
        if ele < template:
            mark += 1
        else:
            template = ele

    if mark != 0:
        return False
    else:
        return True


file = Document("E:\PyCharm\EditorAssistance\TEST1.docx")     #读取文档内容
str4 = re.sub("[A-Za-z\!\%\[\]\。\。\ \.]", "", file.paragraphs[1].text)

print(str4)
str1 = ' '
words = pseg.cut(str4)

AuthorSerialNum = 0
Info = []
AuthorInfo = []
for words, flag in words:
    if flag == 'nr':
        AuthorInfo = []
        AuthorSerialNum += 1
        Info.append(AuthorInfo)
        AuthorInfo.append(str(AuthorSerialNum))
    elif '0' <= words <= '9':
        AuthorInfo.append(words)

print(Info)

CompanyName=()
for i in Info:
    CompanyName = ','.join(i[1:])
    CompanyNum = len(i)-1
    if company_order(i[1:]):
     print("第"+i[0]+"名作者工作单位有"+str(CompanyNum)+"个，是"+CompanyName+",按顺序出现")
    else:
     print("第" + i[0] + "名作者工作单位有" + str(CompanyNum) + "个，是" + CompanyName+",没按顺序出现")
