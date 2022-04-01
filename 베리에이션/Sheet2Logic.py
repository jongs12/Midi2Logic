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
        textlocate=name+"/"+input("파일 확장자를 제외한 악보의 이름을 입력하세요. ")+".txt"
        with open(textlocate,"r",encoding="UTF-8") as file:
            file.read()
    except FileNotFoundError:
        print("그런 파일은 안 보이는데요, 다시 확인해 주시겠어요?")
        print()
    else:
        break
logiclocate=name+"/로직.txt"
print()

block1=['C0', 'C#0', 'D0', 'D#0', 'E0', 'F0', 'F#0', 'G0', 'G#0', 'A0', 'A#0', 'B0', 'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1', 'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5', 'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6', 'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7', 'A7', 'A#7', 'B7', 'C8', 'C#8', 'D8', 'D#8', 'E8', 'F8', 'F#8', 'G8', 'G#8', 'A8', 'A#8', 'B8', 'C9', 'C#9', 'D9', 'D#9', 'E9', 'F9', 'F#9', 'G9', 'G#9', 'A9', 'A#9', 'B9', 'C10', 'C#10', 'D10', 'D#10', 'E10', 'F10', 'F#10', 'G10']
block2=['C0', 'Db0', 'D0', 'Eb0', 'E0', 'F0', 'Gb0', 'G0', 'Ab0', 'A0', 'Bb0', 'B0', 'C1', 'Db1', 'D1', 'Eb1', 'E1', 'F1', 'Gb1', 'G1', 'Ab1', 'A1', 'Bb1', 'B1', 'C2', 'Db2', 'D2', 'Eb2', 'E2', 'F2', 'Gb2', 'G2', 'Ab2', 'A2', 'Bb2', 'B2', 'C3', 'Db3', 'D3', 'Eb3', 'E3', 'F3', 'Gb3', 'G3', 'Ab3', 'A3', 'Bb3', 'B3', 'C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4', 'C5', 'Db5', 'D5', 'Eb5', 'E5', 'F5', 'Gb5', 'G5', 'Ab5', 'A5', 'Bb5', 'B5', 'C6', 'Db6', 'D6', 'Eb6', 'E6', 'F6', 'Gb6', 'G6', 'Ab6', 'A6', 'Bb6', 'B6', 'C7', 'Db7', 'D7', 'Eb7', 'E7', 'F7', 'Gb7', 'G7', 'Ab7', 'A7', 'Bb7', 'B7', 'C8', 'Db8', 'D8', 'Eb8', 'E8', 'F8', 'Gb8', 'G8', 'Ab8', 'A8', 'Bb8', 'B8', 'C9', 'Db9', 'D9', 'Eb9', 'E9', 'F9', 'Gb9', 'G9', 'Ab9', 'A9', 'Bb9', 'B9', 'C10', 'Db10', 'D10', 'Eb10', 'E10', 'F10', 'Gb10', 'G10']
block3=['c0', 'c#0', 'd0', 'd#0', 'e0', 'f0', 'f#0', 'g0', 'g#0', 'a0', 'a#0', 'b0', 'c1', 'c#1', 'd1', 'd#1', 'e1', 'f1', 'f#1', 'g1', 'g#1', 'a1', 'a#1', 'b1', 'c2', 'c#2', 'd2', 'd#2', 'e2', 'f2', 'f#2', 'g2', 'g#2', 'a2', 'a#2', 'b2', 'c3', 'c#3', 'd3', 'd#3', 'e3', 'f3', 'f#3', 'g3', 'g#3', 'a3', 'a#3', 'b3', 'c4', 'c#4', 'd4', 'd#4', 'e4', 'f4', 'f#4', 'g4', 'g#4', 'a4', 'a#4', 'b4', 'c5', 'c#5', 'd5', 'd#5', 'e5', 'f5', 'f#5', 'g5', 'g#5', 'a5', 'a#5', 'b5', 'c6', 'c#6', 'd6', 'd#6', 'e6', 'f6', 'f#6', 'g6', 'g#6', 'a6', 'a#6', 'b6', 'c7', 'c#7', 'd7', 'd#7', 'e7', 'f7', 'f#7', 'g7', 'g#7', 'a7', 'a#7', 'b7', 'c8', 'c#8', 'd8', 'd#8', 'e8', 'f8', 'f#8', 'g8', 'g#8', 'a8', 'a#8', 'b8', 'c9', 'c#9', 'd9', 'd#9', 'e9', 'f9', 'f#9', 'g9', 'g#9', 'a9', 'a#9', 'b9', 'c10', 'c#10', 'd10', 'd#10', 'e10', 'f10', 'f#10', 'g10']
block4=['c0', 'db0', 'd0', 'eb0', 'e0', 'f0', 'gb0', 'g0', 'ab0', 'a0', 'bb0', 'b0', 'c1', 'db1', 'd1', 'eb1', 'e1', 'f1', 'gb1', 'g1', 'ab1', 'a1', 'bb1', 'b1', 'c2', 'db2', 'd2', 'eb2', 'e2', 'f2', 'gb2', 'g2', 'ab2', 'a2', 'bb2', 'b2', 'c3', 'db3', 'd3', 'eb3', 'e3', 'f3', 'gb3', 'g3', 'ab3', 'a3', 'bb3', 'b3', 'c4', 'db4', 'd4', 'eb4', 'e4', 'f4', 'gb4', 'g4', 'ab4', 'a4', 'bb4', 'b4', 'c5', 'db5', 'd5', 'eb5', 'e5', 'f5', 'gb5', 'g5', 'ab5', 'a5', 'bb5', 'b5', 'c6', 'db6', 'd6', 'eb6', 'e6', 'f6', 'gb6', 'g6', 'ab6', 'a6', 'bb6', 'b6', 'c7', 'db7', 'd7', 'eb7', 'e7', 'f7', 'gb7', 'g7', 'ab7', 'a7', 'bb7', 'b7', 'c8', 'db8', 'd8', 'eb8', 'e8', 'f8', 'gb8', 'g8', 'ab8', 'a8', 'bb8', 'b8', 'c9', 'db9', 'd9', 'eb9', 'e9', 'f9', 'gb9', 'g9', 'ab9', 'a9', 'bb9', 'b9', 'c10', 'db10', 'd10', 'eb10', 'e10', 'f10', 'gb10', 'g10']
block5=['도0', '도#0', '레0', '레#0', '미0', '파0', '파#0', '솔0', '솔#0', '라0', '라#0', '시0', '도1', '도#1', '레1', '레#1', '미1', '파1', '파#1', '솔1', '솔#1', '라1', '라#1', '시1', '도2', '도#2', '레2', '레#2', '미2', '파2', '파#2', ' 솔2', '솔#2', '라2', '라#2', '시2', '도3', '도#3', '레3', '레#3', '미3', '파3', '파#3', '솔3', '솔#3', '라3', '라#3', ' 시3', '도4', '도#4', '레4', '레#4', '미4', '파4', '파#4', '솔4', '솔#4', '라4', '라#4', '시4', '도5', '도#5', '레5', '레#5', '미5', '파5', '파#5', '솔5', '솔#5', '라5', '라#5', '시5', '도6', '도#6', '레6', '레#6', '미6', '파6', '파#6', '솔6', '솔#6', '라6', '라#6', '시6', '도7', '도#7', '레7', '레#7', '미7', '파7', '파#7', '솔7', '솔#7', '라7', '라#7', '시7', '도8', '도#8', '레8', '레#8', '미8', '파8', '파#8', '솔8', '솔#8', '라8', '라#8', '시8', '도9', '도#9', '레9', '레#9', '미9', '파9', '파#9', '솔9', '솔#9', '라9', '라#9', '시9', '도10', '도#10', '레10', '레#10', '미10', '파10', '파#10', '솔10']
block6=['도0', '레b0', '레0', '미b0', '미0', '파0', '솔b0', '솔0', '라b0', '라0', '시b0', '시0', '도1', '레b1', '레1', '미b1', '미1', '파1', '솔b1', '솔1', '라b1', '라1', '시b1', '시1', '도2', '레b2', '레2', '미b2', '미2', '파2', '솔b2', ' 솔2', '라b2', '라2', '시b2', '시2', '도3', '레b3', '레3', '미b3', '미3', '파3', '솔b3', '솔3', '라b3', '라3', '시b3', ' 시3', '도4', '레b4', '레4', '미b4', '미4', '파4', '솔b4', '솔4', '라b4', '라4', '시b4', '시4', '도5', '레b5', '레5', '미b5', '미5', '파5', '솔b5', '솔5', '라b5', '라5', '시b5', '시5', '도6', '레b6', '레6', '미b6', '미6', '파6', '솔b6', '솔6', '라b6', '라6', '시b6', '시6', '도7', '레b7', '레7', '미b7', '미7', '파7', '솔b7', '솔7', '라b7', '라7', '시b7', '시7', '도8', '레b8', '레8', '미b8', '미8', '파8', '솔b8', '솔8', '라b8', '라8', '시b8', '시8', '도9', '레b9', '레9', '미b9', '미9', '파9', '솔b9', '솔9', '라b9', '라9', '시b9', '시9', '도10', '레b10', '레10', '미b10', '미10', '파10', '솔b10', '솔10']
block7=['도0', '디0', '레0', '리0', '미0', '파0', '피0', '솔0', '실0', '라0', '릴0', '시0', '도1', '디1', '레1', '리1', '미1', '파1', '피1', '솔1', '실1', '라1', '릴1', '시1', '도2', '디2', '레2', '리2', '미2', '파2', '피2', '솔2', '실2', '라2', '릴2', '시2', '도3', '디3', '레3', '리3', '미3', '파3', '피3', '솔3', '실3', '라3', '릴3', '시3', '도4', '디4', ' 레4', '리4', '미4', '파4', '피4', '솔4', '실4', '라4', '릴4', '시4', '도5', '디5', '레5', '리5', '미5', '파5', '피5', ' 솔5', '실5', '라5', '릴5', '시5', '도6', '디6', '레6', '리6', '미6', '파6', '피6', '솔6', '실6', '라6', '릴6', '시6', ' 도7', '디7', '레7', '리7', '미7', '파7', '피7', '솔7', '실7', '라7', '릴7', '시7', '도8', '디8', '레8', '리8', '미8', ' 파8', '피8', '솔8', '실8', '라8', '릴8', '시8', '도9', '디9', '레9', '리9', '미9', '파9', '피9', '솔9', '실9', '라9', ' 릴9', '시9', '도10', '디10', '레10', '리10', '미10', '파10', '피10', '솔10']
block8=['도0', '렐0', '레0', '메0', '미0', '파0', '셀0', '솔0', '랄0', '라0', '세0', '시0', '도1', '렐1', '레1', '메1', '미1', '파1', '셀1', '솔1', '랄1', '라1', '세1', '시1', '도2', '렐2', '레2', '메2', '미2', '파2', '셀2', '솔2', '랄2', '라2', '세2', '시2', '도3', '렐3', '레3', '메3', '미3', '파3', '셀3', '솔3', '랄3', '라3', '세3', '시3', '도4', '렐4', ' 레4', '메4', '미4', '파4', '셀4', '솔4', '랄4', '라4', '세4', '시4', '도5', '렐5', '레5', '메5', '미5', '파5', '셀5', ' 솔5', '랄5', '라5', '세5', '시5', '도6', '렐6', '레6', '메6', '미6', '파6', '셀6', '솔6', '랄6', '라6', '세6', '시6', ' 도7', '렐7', '레7', '메7', '미7', '파7', '셀7', '솔7', '랄7', '라7', '세7', '시7', '도8', '렐8', '레8', '메8', '미8', ' 파8', '셀8', '솔8', '랄8', '라8', '세8', '시8', '도9', '렐9', '레9', '메9', '미9', '파9', '셀9', '솔9', '랄9', '라9', ' 세9', '시9', '도10', '렐10', '레10', '메10', '미10', '파10', '셀10', '솔10']

note=['0.00', '0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08', '0.09', '0.10', '0.11', '1.00', '1.01', '1.02', '1.03', '1.04', '1.05', '1.06', '1.07', '1.08', '1.09', '1.10', '1.11', '2.00', '2.01', '2.02', '2.03', '2.04', '2.05', '2.06', '2.07', '2.08', '2.09', '2.10', '2.11', '3.00', '3.01', '3.02', '3.03', '3.04', '3.05', '3.06', '3.07', '3.08', '3.09', '3.10', '3.11', '4.00', '4.01', '4.02', '4.03', '4.04', '4.05', '4.06', '4.07', '4.08', '4.09', '4.10', '4.11', '5.00', '5.01', '5.02', '5.03', '5.04', '5.05', '5.06', '5.07', '5.08', '5.09', '5.10', '5.11', '6.00', '6.01', '6.02', '6.03', '6.04', '6.05', '6.06', '6.07', '6.08', '6.09', '6.10', '6.11']
midi=[]
drum=[]
tempdrum=[]
track=-1
num=1
play=0
drumplay=0
tempo=0
loops=0
verse=[]
bsegno=0
print("음정 조정값을 입력하세요. 잘못된 입력은 0으로 처리됩니다. 너무 높거나 낮은 소리는 나지 않습니다.")
key=input("1음은 0.5이고, 1옥타브는 6입니다. 음수도 입력 가능합니다. ")
try:
    key=float(key)
except:
    key=-12
else:
    if key*2!=int(key*2) :
        key=-12
    else:
        key=int(key*2)-12
print()

print("연주 속도(배속)를 입력하세요. 잘못된 입력은 1로 처리됩니다.")
speed=input("배속은 속도만 변화시키며, 음높이에는 영향을 주지 않습니다. ")
try:
    speed=float(speed)
except:
    speed=1
else:
    if speed==0 :
        speed=1
        
print()

print("건반 모드를 켜시겠습니까?")
many=input("1은 '예', 그 외는 '아니요' ")
print()

#읽기
with open(textlocate,"r",encoding="UTF-8") as file:
    while True:
        x=file.readline().strip()
        if x=="start" or x=="시작" :
            break
    while True:
        velo=""
        temp2=-1
        x=file.readline().strip()
        if x=="" :
            continue
        y=x.split(" ")
        if y[0]=="*" :
            continue
        if x=="end" or x=="종료" :
            if play==0 :
                num-=1
                if drumplay==1 :
                    for I in range(len(drum)-1):
                        tempdrum.append(drum[I])
                    drum=tempdrum
                    tempdrum=[]
            if loops>0 :
                for J in range(len(loop1)):
                    verse.append(loop1[J]+[])
                for J in range(len(loop1)):
                    loop1[J][1]+=temp
                for J in range(len(loop2)):
                    verse.append(loop2[J]+[])
                for J in range(len(loop2)):
                    loop2[J][1]+=(temp-bsegno)
                for J in range(len(loop3)):
                    verse.append(loop3[J]+[])
                for J in range(len(loop3)):
                    loop3[J][1]+=(temp-bsegno)
                if segno==0 :
                    loop2=loop1
                for I in range(loops-2):
                    for J in range(len(loop2)):
                        verse.append(loop2[J]+[])
                    for J in range(len(loop2)):
                        loop2[J][1]+=(temp-bsegno)
                    for J in range(len(loop3)):
                        verse.append(loop3[J]+[])
                    for J in range(len(loop3)):
                        loop3[J][1]+=(temp-bsegno)
                if loops>1 :
                    for I in range(len(loop2)):
                        verse.append(loop2[I]+[])
                for I in range(len(verse)):
                    midi[track].append(verse[I])
            break
        else :
            if y[0]=="track" or y[0]=="drum" or y[0]=="트랙" or y[0]=="드럼" :
                if loops>0 :
                    for J in range(len(loop1)):
                        verse.append(loop1[J]+[])
                    for J in range(len(loop1)):
                        loop1[J][1]+=temp
                    for J in range(len(loop2)):
                        verse.append(loop2[J]+[])
                    for J in range(len(loop2)):
                        loop2[J][1]+=(temp-bsegno)
                    for J in range(len(loop3)):
                        verse.append(loop3[J]+[])
                    for J in range(len(loop3)):
                        loop3[J][1]+=(temp-bsegno)
                    if segno==0 :
                        loop2=loop1
                    for I in range(loops-2):
                        for J in range(len(loop2)):
                            verse.append(loop2[J]+[])
                        for J in range(len(loop2)):
                            loop2[J][1]+=(temp-bsegno)
                        for J in range(len(loop3)):
                            verse.append(loop3[J]+[])
                        for J in range(len(loop3)):
                            loop3[J][1]+=(temp-bsegno)
                    if loops>1 :
                        for I in range(len(loop2)):
                            verse.append(loop2[I]+[])
                    for I in range(len(verse)):
                        midi[track].append(verse[I])
                verse=[]
                loop1=[]
                loop2=[]
                loop3=[]
                try:
                    loops=int(y[1])
                except:
                    loops=1
                track+=1
                midi.append([1])
                temp=0
                fine=0
                segno=0
                if drumplay==1 and play==0 :
                    for I in range(len(drum)-1):
                        tempdrum.append(drum[I])
                    drum=tempdrum
                    tempdrum=[]
                if play==1 :
                    num+=1
                    play=0
                drumplay=0
                if y[0]=="drum" or y[0]=="드럼" :
                    drumplay=1
                    drum.append(num)
            elif y[0]=="fine" or y[0]=="피네" :
                fine=1
                continue
            elif y[0]=="segno" or y[0]=="세뇨" :
                if fine==0 :
                    segno=1
                    bsegno=temp
                continue
            else :
                try:
                    y[1]=float(y[1])
                except:
                    y=[y[0],0]
                finally:
                    try:
                        y[0]=float(y[0])
                    except:
                        for I in range(128):
                            if block1[I]==y[0] or block2[I]==y[0] or block3[I]==y[0] or block4[I]==y[0] or block5[I]==y[0] or block6[I]==y[0] or block7[I]==y[0] or block8[I]==y[0] :
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
                                        temp2="control config block"+str(num)+" "+str(note[I-12])
                                        if many=="1" :
                                            velo="control color block"+str(I+73)+" 10 "+str(I-12)+" "+str(city)
                                            temp2="control config block"+str(I+73)+" "+str(note[I-12])
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
                            if fine==1 :
                                if many=="1" and velo!="" :
                                    velo=[velo,temp]
                                    loop3.append(velo)
                                temp2=[temp2,temp]
                                loop3.append(temp2)
                            else:
                                if segno==0 :
                                    if many=="1" and velo!="" :
                                        velo=[velo,temp]
                                        loop1.append(velo)
                                    temp2=[temp2,temp]
                                    loop1.append(temp2)
                                else :
                                    if many=="1" and velo!="" :
                                        velo=[velo,temp]
                                        loop2.append(velo)
                                    temp2=[temp2,temp]
                                    loop2.append(temp2)
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
                    if time>midi[I][midi[I][0]][1] :
                        time=midi[I][midi[I][0]][1]
                        temp=midi[I][midi[I][0]][0]
                        temp2=I
                    if time>=midi[I][midi[I][0]][1] and tline==0 :
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
        if time-total>0 :
            code[pro].append("wait "+str((time-total)/(tempo/60))+"\n")
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
