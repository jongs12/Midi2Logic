import math
zero=0
color=[0,0,0]
size=0
line=0

this=__file__.split("\\")
name=""
name+=this[0]
for I in range(1,len(this)-1):
    name+="/"
    name+=this[I]
textlocate=name+"/로직.txt"

with open(textlocate,"r") as file:
    input("엔터를 눌러 작업을 시작합니다.")
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
            turtle.goto(-200,-200)
            break
        else :
            y=x.split()
            if y[0]=="draw" :
                if y[1]=="clear" :
                    turtle.color(int(y[2]),int(y[3]),int(y[4]))
                    turtle.pensize(0)
                    turtle.goto(-88,-88)
                    turtle.begin_fill()
                    turtle.setheading(0)
                    for I in range(4):
                        turtle.forward(176)
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
                elif y[1]=="line" and zero==0 :
                    turtle.penup()
                    turtle.goto(int(y[2])-88,int(y[3])-88)
                    turtle.pendown()
                    turtle.goto(int(y[4])-88,int(y[5])-88)
                    line+=1
                elif y[1]=="rect" :
                    turtle.penup()
                    turtle.goto(int(y[2])-88,int(y[3])-88)
                    turtle.pendown()
                    turtle.pensize(0)
                    turtle.begin_fill()
                    turtle.setheading(0)
                    for I in range(2):
                        turtle.forward(int(y[4]))
                        turtle.left(90)
                        turtle.forward(int(y[5]))
                        turtle.left(90)
                    turtle.end_fill()
                    turtle.pensize(size)
                    line+=1
                elif y[1]=="lineRect" and zero==0 :
                    turtle.penup()
                    turtle.goto(int(y[2])-88,int(y[3])-88)
                    turtle.pendown()
                    turtle.setheading(0)
                    for I in range(2):
                        turtle.forward(int(y[4]))
                        turtle.left(90)
                        turtle.forward(int(y[5]))
                        turtle.left(90)
                    line+=1
                elif y[1]=="poly" :
                    s=int(y[5])*(2*math.sin(math.pi/int(y[4])))
                    a=(180*(int(y[4])-2))/int(y[4])
                    turtle.penup()
                    turtle.goto(int(y[2])-88,int(y[3])-88)
                    turtle.setheading(int(y[6])%360)
                    turtle.forward(int(y[5]))
                    turtle.pendown()
                    turtle.pensize(0)
                    turtle.begin_fill()
                    turtle.left(180-(a/2))
                    for I in range(int(y[4])):
                        turtle.forward(s)
                        turtle.left(180-a)
                    turtle.end_fill()
                    turtle.pensize(size)
                    line+=1
                elif y[1]=="linePoly" and zero==0 :
                    s=int(y[5])*(2*math.sin(math.pi/int(y[4])))
                    a=(180*(int(y[4])-2))/int(y[4])
                    turtle.penup()
                    turtle.goto(int(y[2])-88,int(y[3])-88)
                    turtle.setheading(int(y[6])%360)
                    turtle.forward(int(y[5]))
                    turtle.pendown()
                    turtle.left(180-(a/2))
                    for I in range(int(y[4])):
                        turtle.forward(s)
                        turtle.left(180-a)
                    line+=1
                elif y[1]=="triangle" :
                    turtle.penup()
                    turtle.goto(int(y[2])-88,int(y[3])-88)
                    turtle.pendown()
                    turtle.pensize(0)
                    turtle.begin_fill()
                    turtle.goto(int(y[4])-88,int(y[5])-88)
                    turtle.goto(int(y[6])-88,int(y[7])-88)
                    turtle.end_fill()
                    turtle.pensize(size)
                    line+=1
                    
input("작업 완료! 엔터로 종료")
