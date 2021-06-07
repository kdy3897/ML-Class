import numpy as np
import pandas as pd
from tkinter import *
import os



path = "C:/Users/pc/PycharmProjects/CapstoneDesign/testvideo"
file_list = os.listdir(path)


# numpy 배열로 data frame 생성
my_darray = np.array(file_list) #############
student_pd = pd.DataFrame(my_darray)
print(student_pd)
print(student_pd.shape)
print(len(student_pd))


def CurSelect(evt):
    value = str((lb.get(lb.curselection())))
    f = open("test.txt", 'w')
    f.write(value)
    f.close()

    text_file_path = 'C:/Users/pc/PycharmProjects/CapstoneDesign/test.txt'
    new_text_content = ''
    target_word = '.mp4'
    new_word = ''
    with open(text_file_path, 'r') as f:
        lines = f.readlines()  ## 기존 텍스트파일에 대한 내용을 모두 읽는다.
        for i, l in enumerate(lines):
            new_string = l.strip().replace(target_word, new_word)
            if new_string:
                new_text_content = new_string
            else:
                new_text_content

    with open(text_file_path, 'w') as f:
        f.write(new_text_content)

    return value

window = Tk()
window.geometry("600x550")

frame = Frame(window)
frame.pack()

#리스트박스 속성 설정
lb = Listbox(frame, height=30, width=60, selectmode="extended")
lb.bind('<<ListboxSelect>>', CurSelect)
lb.pack(side="left", fill="y")

scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.config(command=lb.yview)
scrollbar.pack(side="right", fill="y")

lb.config(yscrollcommand=scrollbar.set)

for x in range(0):
    lb.insert(END, str(x))


for i in student_pd.index:
      val = student_pd.loc[i, 0]
      lb.insert(END, val)

#def closecallback():
#
#    root.destroy()
#
#Button(root,text="Close",command=closecallback).pack()


def CallBack():
    os.system('python main.py')

Button(window, text="Run",command= CallBack).pack()


window.mainloop()