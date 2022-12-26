import os
import time
img_path=input('请输入文件路径(结尾加上/)：') 

txt_path=input('请输入文件路径(保存地)：') 

name = input('请输入保存文件名：')

#获取该目录下所有文件，存入列表中
fileList=os.listdir(img_path)

txt= txt_path + "\\" + name

f=open(txt ,"a")

f.write("<!DOCTYPE html><html>")
f.write("<head><meta charset=\"utf-8\"><title>Welcome to my site!</title><style>body {width: 35em;margin: 0 auto;font-family: Tahoma, Verdana, Arial, sans-serif;}</style></head>")
f.write("<body>\n")
f.write("<table border=\"1\">\n")

n = 0
for i in fileList:

    # words_html =  <img src="smiley.gif" alt="Smiley face" height="42" width="42">

    url = "https://github.com/songxiao1018/blog-img/blob/main/2022-2023-1/" + fileList[n] + "?raw=true"

    words_html = "<tr><td><a href=\" " + url + "\">例会1</a></td></tr> \n"

    words_md = "![" + fileList[n] + "]" + "(https://github.com/songxiao1018/blog-img/blob/main/2022-2023-1/" + fileList[n] + ")"

    line_md = "| " + words_md + " | " + " ` " + words_md + " ` " + " | \n "

    line_html =  url + "\n" + words_html  + "\n"

    f.write(line_html)
    n += 1

f.write("</table></body></html>\n")
