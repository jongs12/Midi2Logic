print("악보? -> 로직 변환 프로그램 Sheet2Logic")
print("설명을 전부 읽으셨길 바랍니다.")
print()

#확인
this=__file__.split("\\")
name=""
name+=this[0]
for I in range(1,len(this)-1):
    name+="/"
    name+=this[I]
while True:
    try:
        textlocate=name+"/"+input("파일 확장자를 제외한 악보의 이름을 입력하세요.")+".txt"
        with open(textlocate,"r",encoding="UTF-8") as file:
            file.read()
    except FileNotFoundError:
        print("그런 파일은 안 보이는데요, 다시 확인해 주시겠어요?")
        print()
    else:
        break
logiclocate=name+"/로직.txt"
print()

block=['C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1', 'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5', 'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6', 'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7', 'A7', 'A#7', 'B7']
block2=['도1', '도#1', '레1', '레#1', '미1', '파1', '파#1', '솔1', '솔#1', '라1', '라#1', '시1', '도2', '도#2', '레2', '레#2', '미2', '파2', '파#2', '솔2', '솔#2', '라2', '라#2', '시2', '도3', '도#3', '레3', '레#3', '미3', '파3', '파#3', '솔3', '솔#3', '라3', '라#3', '시3', '도4', '도#4', '레4', '레#4', '미4', '파4', '파#4', '솔4', '솔#4', '라4', '라#4', '시4', '도5', '도#5', '레5', '레#5', '미5', '파5', '파#5', '솔5', '솔#5', '라5', '라#5', '시5', '도6', '도#6', '레6', '레#6', '미6', '파6', '파#6', '솔6', '솔#6', '라6', '라#6', '시6', '도7', '도#7', '레7', '레#7', '미7', '파7', '파#7', '솔7', '솔#7', '라7', '라#7', '시7']
note=['0.00', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09', '0.10', '0.11', '1.00', '1.01', '1.02', '1.03', '1.04', '1.05', '1.06', '1.07', '1.08', '1.09', '1.10', '1.11', '2.00', '2.01', '2.02', '2.03', '2.04', '2.05', '2.06', '2.07', '2.08', '2.09', '2.10', '2.11', '3.00', '3.01', '3.02', '3.03', '3.04', '3.05', '3.06', '3.07', '3.08', '3.09', '3.10', '3.11', '4.00', '4.01', '4.02', '4.03', '4.04', '4.05', '4.06', '4.07', '4.08', '4.09', '4.10', '4.11', '5.00', '5.01', '5.02', '5.03', '5.04', '5.05', '5.06', '5.07', '5.08', '5.09', '5.10', '5.11', '6.00', '6.01', '6.02', '6.03', '6.04', '6.05', '6.06', '6.07', '6.08', '6.09', '6.10', '6.11']
midi=[]
drum=[]
track=-1
num=1
play=0
tempo=0
loops=0
verse=[]
print("음정 조정값을 입력하세요. 잘못된 입력은 0으로 처리됩니다. 너무 높거나 낮은 소리는 나지 않습니다.")
key=input("1음은 0.5이고, 1옥타브는 6입니다. 음수도 입력 가능합니다. ")
try:
    key=float(key)
except:
    key=0
else:
    if key*2!=int(key*2) :
        key=0
    else:
        key=int(key*2)
print()

print("연주 속도(배속)를 입력하세요. 잘못된 입력은 1로 처리됩니다.")
speed=input("배속은 속도만 변화시키며, 음높이에는 영향을 주지 않습니다. ")
re=0
try:
    speed=float(speed)
except:
    speed=1
else:
    if speed==0 :
        speed=1
    if speed<0 :
        re=1
        
print()

print("건반 모드를 켜시겠습니까?")
many=input("1은 '예', 그 외는 '아니요' ")
print()

#읽기
with open(textlocate,"r",encoding="UTF-8") as file:
    while True:
        x=file.readline().strip()
        if x=="start" :
            break
    while True:
        velo=""
        temp2=-1
        x=file.readline().strip()
        y=x.split(" ")
        if x=="end" :
            if loops>0 :
                for I in range(loops-1):
                    for J in range(len(loop1)):
                        verse.append(loop1[J]+[])
                    for J in range(len(loop1)):
                        loop1[J][1]+=temp
                    for J in range(len(loop2)):
                        verse.append(loop2[J]+[])
                    for J in range(len(loop2)):
                        loop2[J][1]+=temp
                for I in range(len(loop1)):
                    verse.append(loop1[I]+[])
                if re==1 :
                    verse.reverse()
                for I in range(len(verse)):
                    midi[track].append(verse[I])
            break
        else :
            if y[0]=="track" or y[0]=="drum" :
                if loops>0 :
                    for I in range(loops-1):
                        for J in range(len(loop1)):
                            verse.append(loop1[J]+[])
                        for J in range(len(loop1)):
                            loop1[J][1]+=temp
                        for J in range(len(loop2)):
                            verse.append(loop2[J]+[])
                        for J in range(len(loop2)):
                            loop2[J][1]+=temp
                    for I in range(len(loop1)):
                        verse.append(loop1[I]+[])
                    if re==1 :
                        verse.reverse()
                    for I in range(len(verse)):
                        midi[track].append(verse[I])
                verse=[]
                loop1=[]
                loop2=[]
                try:
                    loops=int(y[1])
                except:
                    loops=1
                track+=1
                midi.append([1])
                temp=0
                fine=0
                if play==1 :
                    num+=1
                    play=0
                    if y[0]=="drum" :
                        drum.append(num)
            elif y[0]=="fine" :
                fine=1
                continue
            else :
                try:
                    y[1]=float(y[1])
                except:
                    continue
                else:
                    try:
                        y[0]=float(y[0])
                    except:
                        for I in range(84):
                            if block[I]==y[0] or block2[I]==y[0]:
                                try:
                                    city=float(y[2])
                                except:
                                    city=1
                                try:
                                    non=0
                                    for J in range(len(drum)):
                                        if drum[J]==num :
                                            non=1
                                    if non==0 :
                                        temp2="control config block"+str(num)+" "+str(note[I+key])
                                        if many=="1" :
                                            velo="control color block"+str(I+1+key)+" inst "+str(I+key)+" "+str(city)
                                            temp2="control config block"+str(I+1+key)+" "+str(note[I+key])
                                    else :
                                        temp2="control config block"+str(num)+" "+str(note[I])
                                        if many=="1" :
                                            velo="control color block"+str(I+85)+" 10 "+str(I)+" "+str(city)
                                            temp2="control config block"+str(I+85)+" "+str(note[I])
                                except:
                                    temp2=-1
                                else:
                                    if I+key<0 and non==0:
                                        temp2=-1
                                    else :
                                        play=1
                    else:
                        temp2=y[0]
                        if re==1 :
                            tempo=abs(speed*y[0])
                    finally:
                        if temp2!=-1 :
                            if fine==1 :
                                if many=="1" and velo!="" :
                                    velo=[velo,temp]
                                    loop2.append(velo)
                                temp2=[temp2,temp]
                                loop2.append(temp2)
                            else:
                                if many=="1" and velo!="" :
                                    velo=[velo,temp]
                                    loop1.append(velo)
                                temp2=[temp2,temp]
                                loop1.append(temp2)
                        temp+=float(y[1])

#쓰기
    code=[[]]
    pro=0
    line=0
    tline=0
    total=0
    over=0
    code[pro].append("read inst cell1 0\n")
    code[pro].append("read start cell1 1\n")
    code[pro].append("jump 4 equal start 0\n")
    code[pro].append("end\n")
    if many=="1" :
        num=0
    else :
        for I in range(1,num+1):
            non=0
            for J in range(len(drum)):
                if drum[J]==I :
                    non=1
            if non==0 :
                code[pro].append("control color block"+str(I)+" inst 0 0 0\n")
            else :
                code[pro].append("control color block"+str(I)+" 10 0 0 0\n")
    code[pro].append("sensor on switch1 @enabled\n")
    code[pro].append("jump "+str(7+num)+" equal on 1\n")
    code[pro].append("end\n")
    while True:
        done=0
        for I in range(len(midi)):
            if midi[I][0]==len(midi[I]) :
                done+=1
            else :
                if I==done :
                    time=midi[I][midi[I][0]][1]
                    temp=midi[I][midi[I][0]][0]
                    temp2=I
                else :
                    if re==0 :
                        if time>midi[I][midi[I][0]][1] :
                            time=midi[I][midi[I][0]][1]
                            temp=midi[I][midi[I][0]][0]
                            temp2=I
                        if time>=midi[I][midi[I][0]][1] and tline==0 :
                            total=midi[I][midi[I][0]][1]
                    else :
                        if time<midi[I][midi[I][0]][1] :
                            time=midi[I][midi[I][0]][1]
                            temp=midi[I][midi[I][0]][0]
                            temp2=I
                        if time<=midi[I][midi[I][0]][1] and tline==0 :
                            total=midi[I][midi[I][0]][1]
        if done==len(midi) :
            break
        if line>=900 :
            over+=1
            code[pro].append("write inst cell1 0\n")
            code[pro].append("write "+str(over)+" cell1 1\n")
            code.append([])
            pro+=1
            code[pro].append("read inst cell1 0\n")
            code[pro].append("read start cell1 1\n")
            code[pro].append("jump 4 equal start "+str(over)+"\n")
            code[pro].append("end\n")
            line=0
        if re==0 :
            if time-total>0 :
                code[pro].append("wait "+str((time-total)/(tempo/60))+"\n")
                total=time
                line+=1
                tline+=1
        else :
            if total-time>0 :
                code[pro].append("wait "+str((total-time)/(tempo/60))+"\n")
                total=time
                line+=1
                tline+=1
        if type(temp)==float :
            tempo=abs(speed*temp)
        else :
            code[pro].append(temp+"\n")
            line+=1
            tline+=1
        midi[temp2][0]+=1
code[pro].append("set time1 @time\n")
if many!="1" :
    for I in range(1,num+1):
        non=0
        for J in range(len(drum)):
            if drum[J]==I :
                non=1
        if non==0 :
            code[pro].append("control color block"+str(I)+" inst 0 0 0\n")
        else :
            code[pro].append("control color block"+str(I)+" 10 0 0 0\n")
code[pro].append("control enabled switch1 0 0 0 0\n")
code[pro].append("set time2 @time\n")
code[pro].append("op sub time time2 time1\n")
last=line+5
if over==0 :
    last+=(num+3)
code[pro].append("jump "+str(last)+" lessThan time 1000\n")
code[pro].append("write 0 cell1 1\n")

#출력
over+=1
print("Success!\n(",end="")
if many=="1" :
    num=84
print(num,"block",end="")
if num>=2 :
    print("s",end="")
print(",",tline,"line",end="")
if tline>=2 :
    print("s",end="")
print(")\n")

print("출력 위치:",logiclocate)
temp=0
while True:
    if temp==-1 :
        break
    else :
        print()
        print("페이지",str(temp+1)+"/"+str(over))
        with open(logiclocate,"w") as file:
            for I in range(len(code[temp])):
                file.write(code[temp][I])
    print("출력할 페이지 번호를 입력하세요. 0을 입력하면 출력을 중단합니다.")
    temp2=input("아무것도 입력하지 않으면 자동으로 다음 페이지를 출력합니다. ")
    try:
        temp2=int(temp2)
    except:
        if temp+1==over :
            temp=0
        else :
            temp+=1
    else:
        if 0<=temp2<=over :
            temp=temp2-1
        else :
            if temp+1==over :
                temp=0
            else :
                temp+=1
exit(0)
