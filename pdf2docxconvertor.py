from pdf2docx import Converter
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
# pdffile="D:\Learning only\Python\\reportEaxm-OCT-NOV 202212100.pdf"
USER_INP = simpledialog.askstring(title="File name", prompt="Enter the file name:")
# docx_file="examform.docx"
USER_INP=USER_INP+".docx"
cv=Converter(filename)
cv.convert(USER_INP)
cv.close
