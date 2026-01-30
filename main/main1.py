from tkinter import *
from tkinter import messagebox

# 외부 소스코드에서 이 tk를 사용하려 할 때 해당 소스코드에서의 프로시저를 이 함수로 전달한다
def tkfunc1(handler1: function):
    global edt, lstbox
    window = Tk()
    window.geometry('600x300')
    window.title('default window')

    frame1 = Frame(window)
    frame2 = Frame(window)
    frame1.pack(side=TOP)
    frame2.pack(side=BOTTOM, fill=BOTH, expand=1)

    edt = Entry(frame1, width=10); edt.pack(side=LEFT, padx=10, pady=10)
    btn = Button(frame1, text='입력', command=handler1); btn.pack(side=LEFT, padx=10, pady=10)

    lstbox = Listbox(frame2, bg='#ffffff'); lstbox.pack(side=LEFT, fill=BOTH, expand=1)

    window.mainloop()
    
edt = None
lstbox = None