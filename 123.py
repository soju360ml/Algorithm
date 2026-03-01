import tkinter as tk
import random

# 주사위 굴리기 로직 함수
def roll_dice():
    # 유니코드 주사위 문자 배열 (1~6)
    dice_faces = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    
    # 랜덤으로 하나 선택
    result = random.choice(dice_faces)
    
    # 라벨의 텍스트를 랜덤 결과로 업데이트
    label_dice.config(text=result)
    
    # (선택 사항) 결과 텍스트도 업데이트
    label_text.config(text=f"결과: {dice_faces.index(result) + 1}")

# 메인 윈도우 설정
root = tk.Tk()
root.title("🎲 주사위 굴리기")
root.geometry("400x400")
root.resizable(False, False)  # 창 크기 고정

# 타이틀 라벨
title = tk.Label(root, text="행운의 주사위", font=("맑은 고딕", 20, "bold"))
title.pack(pady=20)

# 주사위가 표시될 라벨 (초기값은 1)
# 폰트 크기를 150으로 설정하여 그래픽처럼 보이게 함
label_dice = tk.Label(root, text='\u2680', font=("Helvetica", 150))
label_dice.pack(pady=10)

# 결과 텍스트 라벨
label_text = tk.Label(root, text="결과: 1", font=("맑은 고딕", 15))
label_text.pack(pady=10)

# 굴리기 버튼
btn_roll = tk.Button(root, text="굴리기!", command=roll_dice, 
                     font=("맑은 고딕", 15, "bold"), 
                     bg="#4f46e5", fg="white", # 버튼 색상 (파란색 계열)
                     width=10, height=2)
btn_roll.pack(pady=20)

# 메인 루프 실행
root.mainloop()