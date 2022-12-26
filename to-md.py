import os
import time
img_path=input('请输入文件路径(结尾加上/)：') 

txt_path=input('请输入文件路径(保存地)：') 

name = input('请输入保存文件名：')

#获取该目录下所有文件，存入列表中
fileList=os.listdir(img_path)

txt= txt_path + "\\" + name

f=open(txt ,"a")

f.write("---\n")
f.write("title: img\n")
f.write("date: 2014-11-10 00:13:05\n")
f.write("tags: \n")
f.write("---\n")

f.write("| 预览 | 地址 |\n")
f.write("| ---- | ---- |\n")
f.write("|      |      |\n")

n= 0
for i in fileList:

    # words_html =  <img src="smiley.gif" alt="Smiley face" height="42" width="42">

    url = "http://www.xiaoxiaosky.top/images/" + fileList[n]

    words_html = "<img src= \" " + url + " \" alt=\"Smiley face\" height=\"42\" width=\"42\"> "

    words_md = "![" + fileList[n] + "]" + "(http://www.xiaoxiaosky.top/images/" + fileList[n] + ")"

    line = "| " + words_md + " | " + " ` " + words_md + " ` " + " | \n "

    f.write(line)
    
    n+=1