# Midi2Logic


[KO]
---
미디 파일을 읽어서 게임 '[Mindustry](https://github.com/Anuken/Mindustry)'의 모드 중 하나인 '[Betamindy](https://github.com/sk7725/BetaMindy)'의 노트블럭을 연주하는 로직 코드를 짜주는 프로그램입니다.
사용할 때는 '[Infinite Processor](https://github.com/FreezeMandu/infinite-processor)' 모드를 함께 사용하는 것을 권장합니다.
[민더스트리](https://github.com/Anuken/Mindustry)와 [파이썬](https://github.com/python)에 대해 어느 정도 기초적인 지식이 있으면 사용하는 데 도움이 될 겁니다.

이 프로그램을 사용하려면 [파이썬](https://github.com/python)과 [mido 모듈](https://github.com/mido/mido)(현재 1.2.10)이 필요합니다. 또한, IDLE로 실행하는 것이 좋습니다.
IDLE로 실행한다는 것은 한 줄씩 실행한다는 것이 아니라, 셸 창에서 'File -> Open'으로 파일을 연 다음 F5로 한번에 실행한다는 의미입니다.
(현재는 업데이트로 IDLE 없이 그냥 파이썬 파일을 바로 실행해도 문제없습니다. 근데 그냥 실행하면 Squeezed text 없이 다 출력돼서...)
mido 모듈을 설치하려면 명령 프롬프트에 따옴표 없이 'pip install mido'라고 입력하세요.
(아, 참고로 저는 파이썬 3 씁니다. 컴퓨터에 파이썬 2도 있는데 mido 설치하려니까 거기에 깔려서 수동으로 옮겼습니다.)

이 프로그램에서는 이 프로그램과 같은 폴더에 들어 있는 파일로 읽기 및 쓰기를 합니다.
해당하는 파일은 다음과 같습니다. 혹시나 기존 파일이 삭제되는 불상사를 막기 위해 확인해 주세요:
미디.txt(쓰기 후 읽기), 로직.txt(쓰기만), (미디 이름).mid(프로그램 내에서 입력받음, 읽기만)

가끔씩 인코딩 에러가 나는지 자동으로 미디 파일을 읽지 못할 때가 있습니다. 그럴 때는 Squeezed text라 쓰인 부분을 복사해서
미디 파일이 저장되는 곳(프로그램과 같은 폴더의 미디.txt)에 직접 붙여넣어 저장해주면 됩니다.
만약 붙여넣기를 하지 않고 강제로 진행하려 하면 파일이 비어 있기 때문에 에러가 납니다.

변환 완료 시 셸 창에 blocks와 lines가 표시되는데 blocks는 미디를 온전히 연주하는 데 필요한 노트 블록의 수이고
lines는 연주'에만' 필요한 코드 줄 수입니다. (스위치 상태 감지, 메모리 셀 입출력 등은 제외)
84개의 노트 블록이 각각 한 가지 음만 연주하는 건반 모드가 켜져 있으면 blocks는 84로 고정됩니다.

변환할 때 연주 코드가 900줄이 넘으면 여러 페이지로 나뉘어 출력되는데,
한 프로세서에 최대 999줄까지 들어갈 수 있기 때문에 그런 것으로
페이지 수만큼의 프로세서를 준비해서 각 페이지 내용 전체를 복붙해주시면 됩니다.

노트 블록을 연주하는 모든 프로세서는 모든 노트 블록(block1, block2...)과 메모리 셀(cell1)에 연결되어 있어야 하며,
특히 첫 번째와 마지막 프로세서는 스위치(switch1)에도 연결되어 있어야 합니다.
메모리 셀의 0번 칸은 연주할 악기(0~9까지 가능)를 결정하며, 1번 칸은 연주할 파트(0부터 시작, 자동으로 관리됨)를 결정합니다.

깃헙은 처음이라 많이 난잡해도 양해 부탁드려요.

비록 나중에 더 좋은 프로그램이 나온다고 해도, 제가 이런 것을 시도했다는 것을 기억해 주세요...

[EN]
---
(Translator is used)

This is a program that reads a midi file and creates a logic code to play the note block of '[Betamindy](https://github.com/sk7725/BetaMindy),' one of the mods of the game '[Mindustry](https://github.com/Anuken/Mindustry).'
Recommend '[Infinite Processor](https://github.com/FreezeMandu/infinite-processor)' mod when using.
If you have some basic knowledge of [Mindustry](https://github.com/Anuken/Mindustry) and [Python](https://github.com/python), it will help you use it.

[Python](https://github.com/python) and [mido module](https://github.com/mido/mido)(currently 1.2.10) are required to use this program. Also, it is recommended to run with IDLE. Running with IDLE does not mean running one line at a time, but opens the file with 'File -> Open' in the shell window and then runs it at once with F5.
To install the mido module, type 'pip install mido' without quotes at the command prompt.

This program reads and writes to files in the same folder as this program.
The corresponding file is as follows. Just in case, please check to prevent accidents in which existing files are deleted:
미디.txt(read/write), 로직.txt(write only), (midi name).mid(receives input in program, read only)

Sometimes it can't read the midi file automatically(i think there is an encoding error). In that case, copy the part that says Squeezed text and paste it to 미디.txt(in the same folder as the program) and save.
If you try to force the process without pasting it, an error occurs because the file is empty.

When the conversion is completed, blocks and lines are displayed in the shell window.
'blocks' is the number of note blocks required to fully play the midi.
'lines' is the number of code lines required only for 'play'(except switch state detection, memory cell input/output, etc.).
If keyboard mode, in which 84 note blocks each play only one note, is turned on, the blocks are fixed at 84.

When converting, if the playing code exceeds 900 lines, it is divided into several pages and output. Because it can fit up to 999 lines in one processor.
You need to prepare as many processors as the number of pages and copy and paste the entire contents of each page.

All processors playing the note block must be connected to all note blocks(block1, block2...) and a memory cell (cell1).
In particular, the first and last processors must also be connected to the switch(switch1).
The 0th column of the memory cell determines the instrument to play(available from 0 to 9), and the 1st column determines the part to play(starting from 0, automatically managed).

It's my first time using Github, so I ask for your understanding even if it's very chaotic.

Even if a better program comes out later, please remember that I tried this...
