#!/usr/bin/env python3
from cgi import test
from itertools import count
import pdfkit
import os
from markdown import markdown

output_filename = os.path.dirname(__file__)+"/Kobun_zh.pdf"
target_path = os.path.dirname(__file__)+"/source"
editorsNote = target_path + "/editors-note.md"  # 编者序
translatorsPreface = target_path + "/translators-preface.md" # 译者序

count = 1
fileList = [translatorsPreface, editorsNote]
while count < 29:
    if count < 10:
        fileList.append(target_path+"/chapter0"+str(count)+".md")
    else:
        fileList.append(target_path+"/chapter"+str(count)+".md")
    count = count + 1

text = ""
for file in fileList:
    # print(file)
    with open(file, encoding='utf-8') as f:
        text = f.read()
        html = markdown(text, output_format='html5')  # MarkDown转HTML
        with open(os.path.dirname(__file__)+"/template.html", encoding='utf-8') as f:
            template =f.read()
        html = template % html
        options_pdf = {
            'page-size': 'A6',
            'encoding': 'utf-8',
            'margin-top': '0.1in',
            'margin-right': '0.1in',
            'margin-bottom': '0.1in',
            'margin-left': '0.1in'
        }
        pdfkit.from_string(html, file+".pdf", options=options_pdf)  # HTML转PDF


# cover = os.path.dirname(__file__)+"/cover.html"

# pdfkit.from_string(html, output_filename, options=options_pdf, cover=cover, cover_first=True)  # HTML转PDF


# with open(os.path.dirname(__file__)+"/template.html", encoding='utf-8') as f:
#     template =f.read()


# pdfkit.from_string(html, output_filename, options=options_pdf) 