from tkinter import *

window = None


def newFrame() -> Frame:
    if window:
        f = Frame(window)
        f.pack(side=LEFT, fill=BOTH, expand=1)
        return f
        

def gen():
    global window
    window = Tk()
    window.geometry('600x300')

    # 글로벌 변수에 window객체 등록 -> 여기서 생성한 window는 전역으로 사용 가능
    window.append(window)

    frame1 = Frame(window)
    frame1.pack(side=TOP, fill=BOTH, expand=1)

    # 프레임 생성 버튼 생성 및 패킹
    btn = Button(frame1, text="프레임 생성", command=newFrame); btn.pack(pady=10)

    window.mainloop()

gen()