import math
zero=0
color=[0,0,0]
size=0
line=0
co1=[]
co2=[]

this=__file__.split("\\")
name=""
name+=this[0]
for I in range(1,len(this)-1):
    name+="/"
    name+=this[I]
textlocate=name+"/로직.txt"

with open(textlocate,"r",encoding="UTF-8") as file:
    print("기존 디스플레이는 몇곱몇이었나요?")
    while True:
        try:
            xy=int(input("일반은 80, 대형은 176 "))
        except:
            print("정수로 입력하세요.")
        else:
            if xy>0 :
                print()
                break
            else :
                print("양수로 입력하세요.")
    while True:
        try:
            cx=float(input("변환할 화면의 가로 길이를 입력하세요. "))
            cy=float(input("변환할 화면의 세로 길이를 입력하세요. "))
        except:
            print("유리수로 입력하세요.")
        else:
            if cx!=0 and cy!=0 :
                print()
                break
            else :
                print("0은 안 되죠...")
    import turtle
    turtle.speed(0)
    turtle.colormode(255)
    print("진행중...")
    passed=0
    while True:
        if line//100>passed :
            print(str(line)+"줄 돌파!")
            passed+=1
        x=file.readline().strip()
        if x=="" :
            turtle.penup()
            turtle.color(255,255,255)
            turtle.goto(2*cx,2*cy)
            break
        else :
            y=x.split()
            if y[0]=="draw" :
                if y[1]=="clear" :
                    turtle.color(int(y[2]),int(y[3]),int(y[4]))
                    turtle.pensize(0)
                    turtle.goto(-((cx/2)-1),-((cy/2)-1))
                    turtle.begin_fill()
                    turtle.setheading(0)
                    for I in range(2):
                        if cx>=0 :
                            turtle.forward(cx-2)
                        else :
                            turtle.forward(cx+2)
                        turtle.left(90)
                        if cy>=0 :
                            turtle.forward(cy-2)
                        else :
                            turtle.forward(cy+2)
                        turtle.left(90)
                    turtle.end_fill()
                    turtle.color(color[0],color[1],color[2])
                    turtle.pensize(size)
                    line+=1
                elif y[1]=="color" :
                    turtle.color(int(y[2]),int(y[3]),int(y[4]))
                    color=[int(y[2]),int(y[3]),int(y[4])]
                    line+=1
                elif y[1]=="stroke" :
                    if int(y[2])==0 :
                        turtle.pensize(0)
                        size=0
                        zero=1
                    else :
                        turtle.pensize(int(y[2])-1)
                        size=int(y[2])-1
                        zero=0
                    line+=1
                elif y[1]=="line" :
                    if zero==0 :
                        turtle.penup()
                        turtle.goto((int(y[2])-(xy/2))*(cx/xy),(int(y[3])-(xy/2))*(cy/xy))
                        turtle.pendown()
                        turtle.goto((int(y[4])-(xy/2))*(cx/xy),(int(y[5])-(xy/2))*(cy/xy))
                    line+=1
                elif y[1]=="rect" :
                    turtle.penup()
                    turtle.goto((int(y[2])-(xy/2))*(cx/xy),(int(y[3])-(xy/2))*(cy/xy))
                    turtle.pendown()
                    turtle.pensize(0)
                    turtle.begin_fill()
                    turtle.setheading(0)
                    for I in range(2):
                        turtle.forward(int(y[4])*(cx/xy))
                        turtle.left(90)
                        turtle.forward(int(y[5])*(cy/xy))
                        turtle.left(90)
                    turtle.end_fill()
                    turtle.pensize(size)
                    line+=1
                elif y[1]=="lineRect" :
                    if zero==0 :
                        turtle.penup()
                        turtle.goto((int(y[2])-(xy/2))*(cx/xy),(int(y[3])-(xy/2))*(cy/xy))
                        turtle.pendown()
                        turtle.setheading(0)
                        for I in range(2):
                            turtle.forward(int(y[4])*(cx/xy))
                            turtle.left(90)
                            turtle.forward(int(y[5])*(cy/xy))
                            turtle.left(90)
                    line+=1
                elif y[1]=="poly" :
                    s=int(y[5])*(2*math.sin(math.pi/int(y[4])))
                    a=(180*(int(y[4])-2))/int(y[4])
                    turtle.penup()
                    turtle.goto((int(y[2])-(xy/2))*(cx/xy),(int(y[3])-(xy/2))*(cy/xy))
                    turtle.setheading(int(y[6])%360)
                    co1=list(turtle.position())
                    turtle.forward(int(y[5]))
                    co2=list(turtle.position())
                    turtle.back(int(y[5]))
                    turtle.goto(co1[0]+((co2[0]-co1[0])*(cx/xy)),co1[1]+((co2[1]-co1[1])*(cy/xy)))
                    turtle.pensize(0)
                    turtle.left(180-(a/2))
                    turtle.begin_fill()
                    for I in range(int(y[4])):
                        turtle.penup()
                        co1=list(turtle.position())
                        turtle.forward(s)
                        co2=list(turtle.position())
                        turtle.back(s)
                        turtle.pendown()
                        turtle.goto(co1[0]+((co2[0]-co1[0])*(cx/xy)),co1[1]+((co2[1]-co1[1])*(cy/xy)))
                        turtle.left(180-a)
                    turtle.end_fill()
                    turtle.pensize(size)
                    line+=1
                elif y[1]=="linePoly" :
                    if zero==0 :
                        s=int(y[5])*(2*math.sin(math.pi/int(y[4])))
                        a=(180*(int(y[4])-2))/int(y[4])
                        turtle.penup()
                        turtle.goto((int(y[2])-(xy/2))*(cx/xy),(int(y[3])-(xy/2))*(cy/xy))
                        turtle.setheading(int(y[6])%360)
                        co1=list(turtle.position())
                        turtle.forward(int(y[5]))
                        co2=list(turtle.position())
                        turtle.back(int(y[5]))
                        turtle.goto(co1[0]+((co2[0]-co1[0])*(cx/xy)),co1[1]+((co2[1]-co1[1])*(cy/xy)))
                        turtle.pensize(0)
                        turtle.left(180-(a/2))
                        for I in range(int(y[4])):
                            turtle.penup()
                            co1=list(turtle.position())
                            turtle.forward(s)
                            co2=list(turtle.position())
                            turtle.back(s)
                            turtle.pendown()
                            turtle.goto(co1[0]+((co2[0]-co1[0])*(cx/xy)),co1[1]+((co2[1]-co1[1])*(cy/xy)))
                            turtle.left(180-a)
                        turtle.pensize(size)
                    line+=1
                elif y[1]=="triangle" :
                    turtle.penup()
                    turtle.goto((int(y[2])-(xy/2))*(cx/xy),(int(y[3])-(xy/2))*(cy/xy))
                    turtle.pendown()
                    turtle.pensize(0)
                    turtle.begin_fill()
                    turtle.goto((int(y[4])-(xy/2))*(cx/xy),(int(y[5])-(xy/2))*(cy/xy))
                    turtle.goto((int(y[6])-(xy/2))*(cx/xy),(int(y[7])-(xy/2))*(cy/xy))
                    turtle.end_fill()
                    turtle.pensize(size)
                    line+=1
                    
print("\n작업 완료! 총 "+str(line)+"줄의 코드를 처리하였습니다.")
input("엔터를 눌러 종료합니다.")
exit(0)
