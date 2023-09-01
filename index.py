from tkinter import *
import tkinter.messagebox as msbox

root = Tk() # 창 구성
root.title("Ticketing Macro Program !!!") # 프로그램 제목 구성

site_label = Label(text="매크로 URL 주소").grid(row=0)
site_entry = Entry(root)

def checkEvent():
    if len(site_entry.get()) == 0:
        msbox.showerror(title="확인", message="사이트 URL 값이 존재하지 않음")
    else:
        print(site_entry.get())

def closeEvent():
    msbox.showwarning(title="종료", message="종료하시겠습니까?")

site_entry.grid(row=0, column=1)

Button(root, text="확인", command=checkEvent).grid(row=1, column=0, sticky=W, pady=4)
Button(root, text="종료", command=closeEvent).grid(row=1, column=1, sticky=W, pady=4)

root.mainloop() # 화면 실행