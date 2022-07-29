#!/usr/bin/env python3
import os
from PyPDF2 import PdfFileMerger

output_filename = os.path.dirname(__file__)+"/Kobun_zh.pdf"
target_path = os.path.dirname(__file__)+"/source"
editorsNote = target_path + "/editors-note.md.pdf"  # 编者序
translatorsPreface = target_path + "/translators-preface.md.pdf" # 译者序

count = 1
fileList = [os.path.dirname(__file__)+"/cover.pdf", translatorsPreface, editorsNote]
while count < 29:
    if count < 10:
        fileList.append(target_path+"/chapter0"+str(count)+".md.pdf")
    else:
        fileList.append(target_path+"/chapter"+str(count)+".md.pdf")
    count = count + 1

file_merger = PdfFileMerger()
for pdf in fileList:
    print(pdf)
    file_merger.append(pdf, import_bookmarks=False)     # 合并pdf文件

file_merger.write(os.path.dirname(__file__)+"/Kobun_zh.pdf")