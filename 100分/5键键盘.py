# 题目描述
# 有一个特殊的5键键盘，上面有a，ctrl-c，ctrl-x，ctrl-v，ctrl-a五个键。
# a键在屏幕上输出一个字母a；
# ctrl-c将当前选择的字母复制到剪贴板；
# ctrl-x将当前选择的字母复制到剪贴板，并清空选择的字母；
# ctrl-v将当前剪贴板里的字母输出到屏幕；
# ctrl-a选择当前屏幕上的所有字母。
# 输入描述
# 输入为一行，为简化解析，用数字1 2 3 4 5代表a，ctrl-c，ctrl-x，ctrl-v，ctrl-a五个键的输入，数字用空格分隔。
# 输出描述
# 输出一个数字，为最终屏幕上字母的数量

keyin = list(map(int,input().split()))

def keybroad():
    screen = []
    clip = []
    isSelect = False #默认初始状态没有选择字符
    for item in keyin:
        if item == 1: #a
            if isSelect:
                screen.clear()
            screen.append('a')
        elif item == 2: #cltr c
            if isSelect:
                clip.clear()
                clip.extend(screen) #注意extend和append的区别
        elif item == 3: #ctrl x
            if isSelect:
                clip.clear()
                clip.extend(screen) #cltr x可理解为一个cltr c加一个删除
                screen.clear()
                isSelect = False
        elif item == 4: #ctrl v
            if isSelect:
                screen.clear()
            screen.extend(clip)
            isSelect = False
        elif item == 5: #ctrl a
            if len(screen)!= 0:
                isSelect = True

    return len(screen)

print(keybroad())











