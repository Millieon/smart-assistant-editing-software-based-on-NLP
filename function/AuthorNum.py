# encoding=utf-8


from docx import Document
import jieba.posseg as pseg
import jieba
jieba.setLogLevel(20)
import re
file = Document("E:\PyCharm\EditorAssistance\TEST1.docx")     #读取文档内容
str2 = re.sub("[A-Za-z0-9\!\%\[\]\,\。\。\，\ \.]", "", file.paragraphs[1].text)
print(str2)
str1=' '
words = pseg.cut(str2)
m=0
n=0
for  word,flag in words:
    if flag == 'nr':
        n += 1
print(n)

