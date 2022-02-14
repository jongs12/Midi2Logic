print("악보...? -> 로직 변환 프로그램")
print("설명을 전부 읽으셨길 바랍니다.")
print()

#확인
while True:
    print("파일명을 제외한 파일 경로를 입력하세요.")
    name=input("역슬래시(\)를 슬래시(/)로 바꿀 필요는 없습니다. ")
    name=name.split("\\")
    name="/".join(name)+"/악보.txt"
    try:
        with open(name,"r",encoding="UTF-8") as file:
            file.read()
    except:
        print("존재하지 않거나 잘못된 파일입니다.")
    else:
        break
    finally:
        print()

with open(name,"r",encoding="UTF-8") as file:
    warning=file.readline().strip()
    logiclocate=file.readline().strip()
    left=file.read()

if warning=="on" :
    while True:
        try:
            with open(logiclocate,"r") as file:
                temp=file.read()
        except FileNotFoundError:
            logicnotexist=1
        else:
            logicnotexist=0
        if logicnotexist==0 :
            print("다음 파일이 이미 존재합니다:")
            print(logiclocate)
            print("계속하면 기존 파일이 삭제됩니다. 계속할까요?")
            contin=input("1은 '예', 2는 '예, 다시 표시하지 않습니다.', 그 외는 '아니요' ")
            if contin=="1" :
                print()
                break
            if contin=="2" :
                with open(name,"w",encoding="UTF-8") as file:
                    file.write("off\n")
                    file.write(logiclocate+"\n")
                    file.write(left)
                    print()
                    break
            print()
        else :
            print()
            break

block=['C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1', 'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5', 'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6', 'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7', 'A7', 'A#7', 'B7']
note=['0.00', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09', '0.10', '0.11', '1.00', '1.01', '1.02', '1.03', '1.04', '1.05', '1.06', '1.07', '1.08', '1.09', '1.10', '1.11', '2.00', '2.01', '2.02', '2.03', '2.04', '2.05', '2.06', '2.07', '2.08', '2.09', '2.10', '2.11', '3.00', '3.01', '3.02', '3.03', '3.04', '3.05', '3.06', '3.07', '3.08', '3.09', '3.10', '3.11', '4.00', '4.01', '4.02', '4.03', '4.04', '4.05', '4.06', '4.07', '4.08', '4.09', '4.10', '4.11', '5.00', '5.01', '5.02', '5.03', '5.04', '5.05', '5.06', '5.07', '5.08', '5.09', '5.10', '5.11', '6.00', '6.01', '6.02', '6.03', '6.04', '6.05', '6.06', '6.07', '6.08', '6.09', '6.10', '6.11']
midi=[]
drum=[]
track=-1
num=1
play=0
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
try:
    speed=float(speed)
except:
    speed=1
else:
    if speed<=0 :
        speed=1
print()

print("건반 모드를 켜시겠습니까?")
many=input("1은 '예', 그 외는 '아니요' ")
print()

#읽기
with open(name,"r",encoding="UTF-8") as file:
    while True:
        x=file.readline().strip()
        if x=="start" :
            break
    while True:
        temp2=-1
        velo=""
        x=file.readline().strip()
        if x=="" :
            continue
        if x=="end" :
            break
        else :
            if x=="track" or x=="drum" :
                track+=1
                midi.append([1])
                temp=0
                if play==1 :
                    num+=1
                    play=0
                    if x=="drum" :
                        drum.append(num)
            else :
                y=x.split(" ")
                try:
                    y[0]=float(y[0])
                except:
                    for I in range(84):
                        if block[I]==y[0] :
                            try:
                                non=0
                                for J in range(len(drum)):
                                    if drum[J]==num :
                                        non=1
                                if non==0 :
                                    temp2="control config block"+str(num)+" "+str(note[I+key])
                                    if many=="1" :
                                        velo="control color block"+str(I+1+key)+" inst "+str(I+key)+" 1"
                                        temp2="control config block"+str(I+1+key)+" "+str(note[I+key])
                                else :
                                    temp2="control config block"+str(num)+" "+str(note[I])
                                    if many=="1" :
                                        velo="control color block"+str(I+85)+" 10 "+str(I)+" 1"
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
                finally:
                    if temp2!=-1 :
                        if many=="1" and velo!="" :
                            velo=[velo,temp]
                            midi[track].append(velo)
                        temp2=[temp2,temp]
                        midi[track].append(temp2)
                    temp+=float(y[1])

#쓰기
    code=[[]]
    pro=0
    line=0
    tline=0
    tempo=0
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
                    if time>midi[I][midi[I][0]][1] :
                        time=midi[I][midi[I][0]][1]
                        temp=midi[I][midi[I][0]][0]
                        temp2=I
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
        if time-total>0 :
            code[pro].append("wait "+str((time-total)/(tempo/60))+"\n")
            total=time
            line+=1
            tline+=1
        if type(temp)==float :
            tempo=temp*speed
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
