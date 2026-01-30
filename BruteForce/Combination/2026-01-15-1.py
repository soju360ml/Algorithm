# 반복문으로 조합을 구성해보자

# 알파벳 리스트생성함수를 위한 모듈
import string
import random
import main
from tkinter import *

def handler1():
    edt = main.edt
    lstbox = main.lstbox
    result = []

    header1 = []
    header1.append('%s'.center(20) % '반복문을 통한 조합 구하기')
    header1.append(''.center(40, '-'))

    for s in header1:
        result.append(s)

    result.append(lst_gen(int(edt.get())))

    lstbox.delete(0, lstbox.size() - 1)

    for s in result:
        lstbox.insert(END, s)

# 랜덤한 조합을 만들어내는 함수
def lst_gen(count) -> list:
    # 알파벳 리스트 생성
    al = string.ascii_uppercase

    lst = []
    while True:
        if len(lst) == count:
            break
        n = random.randrange(len(al))
        if n not in lst:
            lst.append(n)

    comb = [al[i] for i in lst]
    return comb

main.tkfunc1(handler1)