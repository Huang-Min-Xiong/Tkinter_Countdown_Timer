import time
import pyautogui
from tkinter import *
from pygame import mixer

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock) #每秒呼叫該函數
    

def countdown():
    global play_sound
    play_sound = False
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get()) #總秒數
    while times > -1:
        minute,second = (times // 60 , times % 60)
        
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
            
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        
        root.update()
        time.sleep(1)

        if(times == 0):
            play_sound = True
            mixer.init() 
            mixer.music.load('sound.mp3') 
            mixer.music.play() 
            pyautogui.alert("時間到!","提醒")
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1


def close_sound():
    if play_sound:
        mixer.music.stop()
    else:
        pass


if __name__ == '__main__':
    root = Tk()
    sw = root.winfo_screenwidth() #屏幕寬度
    sh = root.winfo_screenheight() #屏幕高度
    ww = 300 #程式寬度
    wh = 200 #程式高度
    
    x = (sw-ww) / 2
    y = (sh-wh) / 2
    root.geometry("%dx%d+%d+%d" %(ww,wh,x,y)) #顯示在正中央
    root.resizable(0,0)
    root.config(bg ='orange') 
    root.title('倒數計時器')
    

    #目前時間
    Label(root, font ='arial 15', text = '目前時間 :', bg = 'orange').place(x = 40 ,y = 30) #papaya whip
    curr_time = Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='orange')
    curr_time.place(x = 140 , y = 30)
    clock()

    #設置倒數時間(時:分:秒)
    hrs= StringVar()
    Entry(root, textvariable = hrs, width =2, font = 'arial 15').place(x=140, y=100)
    hrs.set('00')

    mins= StringVar()
    Entry(root, textvariable = mins, width =2, font = 'arial 15').place(x=170, y=100)
    mins.set('00')

    sec = StringVar()
    Entry(root, textvariable = sec, width = 2, font = 'arial 15').place(x=200, y=100)
    sec.set('00')

    Label(root, font ='arial 15', text = '設置時間 :',   bg ='orange').place(x = 40 ,y = 100)
    Button(root, text='開始', bd ='5', command = countdown, bg = 'orange', font = 'arial 15').place(x=50, y=150)
    Button(root, text='關閉鈴聲', bd ='5', command = close_sound, bg = 'orange', font = 'arial 15').place(x=150, y=150)
    root.mainloop()
