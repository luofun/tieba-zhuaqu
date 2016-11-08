from tkinter import *           # 导入 Tkinter 库
import wordstimeliner
root = Tk()                     # 创建窗口对象的背景色
root.resizable(False,False)
root.title("时间频率图")

def btnclick():
    root.update()
    #下面这种方法不知道为什么会不行有些时候
    #word = data.get()
    #SCALE = scale.get()
    word = wordentry.get()
    SCALE = daysentry.get()
    print("word=",word,"\tSCALE=",SCALE)
    wordstimeliner.showLastDays(word,int(SCALE))

def centerWindow(rt):
    rt.update() # update window ,must do
    curWidth = rt.winfo_reqwidth() # get current width
    curHeight = rt.winfo_height() # get current height
    scnWidth,scnHeight = rt.maxsize() # get screen width and height
    # now generate configuration information
    tmpcnf = '%dx%d+%d+%d'%(curWidth,curHeight,
    (scnWidth-curWidth)/2,(scnHeight-curHeight)/2)
    rt.geometry(tmpcnf)
    return rt

data = StringVar(root)
scale = IntVar(root)
Label(root,text="KCC数据分析模块 - 基本分析套件\n该模块用于显示指定词语的时间频率关系图",width=35,height=5).pack()
Label(root,text="请输入要分析的词语（仅一个）:",width=25,height=2).pack()
wordentry = Entry(root,text="请输入内容",width=25,textvariable=data)
wordentry.pack(ipadx=4,ipady=4)
Label(root,text="请输入显示最近多少天的统计图:",width=25,height=2).pack()
daysentry = Entry(root,text="请输显示多少天的",width=25,relief=GROOVE,textvariable=scale)
daysentry.pack(ipadx=4,ipady=4)
Button(root, text="获取edit内容", width=15,relief=GROOVE,command=btnclick).pack(pady=16,ipadx=8,ipady=8)

root = centerWindow(root)
root.mainloop()                 # 进入消息循环
