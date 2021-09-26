#알아본 문법
#sticky =할당된 공간 내에서의 위치 조정
#Text = 서식화된문자 출력.
#widget = 인터페이스에서 응용프로그램을 구성하는 모든 빌딩 블록 용어
#    위젯ex)buttons, radio buttons, text fields, frames, and text labels
#frame = 레이아웃 기본 구성 단위. 다른위젯을 포함하는 직사각형
#height = 위젯의 원하는 높이 ; 1보다 크거나 같아야함
#width = 위젯의 원하는 너비.
#from tkinter.font import Font = 폰트 설정할수있게 임포트함
#   family=문자열폰트패밀리,size=포인트 정수폰트높이,
#Entry=보통 User가 한 줄의 text를 입력하도록 한다
#grid =Widget을 parent grid위에 둔다,,자신의 box나 cell을 grid내에서 표시된다
#오늘의커피 가능하면 랜덤으로 구현


#카페에 사용가능한 자동주문 셀프 키오스크
import tkinter as tk #tkinter 임포트
from tkinter import  messagebox
import tkinter #tkinter 메세지 박스임포트
from tkinter.font import Font #tkinter  폰트임포트
import random


# font.pack()
# textExample.configure(font=font)


price = {"아메리카노" : 3500 , "카페라떼":4000, "자바칩 프라프치노" : 5000, "히비스커스":3500,"오늘의 커피":3000,"랜덤 생과일쥬스":5000}
# 랜덤쥬스라 칭하고 한정수량만 판매
juice = ["바나나","딸기","샤인머스켓","수박","망고"]

#gui환경이름과 크기
window = tk.Tk()
window.title("자동음료 주문 키오스크.ver 0.5")
window.geometry("228x766")  #크기 설정

# font=tkinter.font.Font(family="맑은 고딕", size=10, slant="italic")
font =tkinter.font.Font(family="Arial", size=10, weight="bold", slant="italic")
# label=tkinter.Label(window, text="파이썬 3.6", font=font)
# label.pack()


#변수
order = []
total = 0
random1 = random.randint(1,5) #랜덤쥬스를 가져올 랜덤변수

for key, value in price.items(): #카페 음료를 가져올 키와 값
    print(key, value)

#랜덤쥬스함수
def random_juice():
    global total
    global textarea
    msgbox3=tk.messagebox.askquestion("선택", "랜덤생과일쥬스 입니다.\n추가하시겠습니까?")
    if msgbox3 == "yes":
        this_price = 5000
        total = total + this_price
        order.append(juice[random1])
        textarea.insert(tk.INSERT,juice[random1] + "\n")
        lbl["text"] = "가격 : " + str(total) + "원"

#카페 메뉴추가 함수
def add(cafe):
    global total
    global textarea
    if cafe not in price:
        print("No Drink")
    if cafe == "아메리카노":
        msgbox4 = tk.messagebox.askquestion("샷 선택", "샷추가하시겠습니까?")
        if msgbox4 == "yes":
            this_price = price.get(cafe)-3000
            total = total + this_price
            order.append(cafe)
            textarea.insert(tk.INSERT,"샷추가\n")
            lbl["text"] = "가격 : " + str(total) + "원" 

    this_price = price.get(cafe)
    total = total + this_price
    order.append(cafe)
    textarea.insert(tk.INSERT, cafe +  "\n")
    lbl["text"] = "가격 : " + str(total) + "원"

#나가기(주문 완료)버튼 함수
def button_exit():
    msgbox= tk.messagebox.askquestion("확인", '주문을 마치시겠습니까?')
    if msgbox == 'yes':
        exit()

#오늘의 커피 함수
def today_coffee():
    global total
    global key
    global textarea
    msgbox2=tk.messagebox.askquestion("선택", "오늘의커피는 바닐라 라떼 입니다.\n추가하시겠습니까?")
    if msgbox2 == "yes":
        this_price = price.get("오늘의 커피")
        total = total + this_price
        order.append(price.get("오늘의 커피"))
        textarea.insert(tk.INSERT,"오늘의 커피\n")
        lbl["text"] = "가격 : " + str(total) + "원"

#프레임
frame1 = tk.Frame(window,relief="solid", bd=20)
frame1.pack()

text_entry1 = tk.Entry(frame1, width = 30, fg = 'blue')
text_entry1.insert(0,"insert first text")
text_entry1.pack

#커맨드 지정및,width=가로 ,height = 세로
#연결된 함수에 인수를 전달해야하는경우 command에서 안됨#lambda 표현식쓰기
b1=tk.Button(frame1, text="아메리카노" , command=lambda:add("아메리카노"), width = 20,height=2, fg="blue",bg = 'light yellow',font=font).grid(row=0 , column=0)
b2=tk.Button(frame1, text="카페  라떼", command=lambda:add("카페라떼"), width = 20,height=2,fg="blue",bg = 'light yellow',font=font).grid(row=1 , column=0)
b3=tk.Button(frame1, text="자바칩 프라프치노", command=lambda:add("자바칩 프라프치노"), width = 20,height=2,fg="blue",bg = 'light yellow',font=font).grid(row=2 , column=0)
b4=tk.Button(frame1, text="히비스커스", command=lambda:add("히비스커스"), width = 20,height=2,fg="blue",bg = 'light yellow',font=font).grid(row=3 , column=0)
b5=tk.Button(frame1, text="오늘의커피", command=today_coffee, width = 20,height=2,fg="blue",bg = 'light yellow',font=font).grid(row=4 , column=0)
b6=tk.Button(frame1, text="랜덤생과일쥬스", command=random_juice, width = 20,height=2,fg="blue",bg = 'light yellow',font=font).grid(row=5 , column=0)
b7=tk.Button(frame1, text="주문  완료", command=button_exit, width = 20,height=2,fg="blue",bg = 'yellow',font=font).grid(row=6 , column=0)

#가격의 값 저장
textarea = tk.Text(window)
textarea.pack()


#주문 요청사항과 가격을 나타내는 창
lbl = tk.Label(window, text="주문 요청사항",width=10, height=2)
lbl.pack()


text_test=tk.Text(window)
text_test.pack()


window.mainloop()
