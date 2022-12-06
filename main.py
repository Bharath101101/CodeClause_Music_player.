import tkinter as tk
import fnmatch
import os
from pygame import mixer
from tkinter.filedialog import askdirectory

canvas =tk.Tk()
canvas.title("Music player")
canvas.geometry("400x600")
canvas.config(bg='black')

prev_image=tk.PhotoImage(file="prev_img.png")
stop_image=tk.PhotoImage(file="stop_img.png")
play_image=tk.PhotoImage(file="play_img.png")
pause_image=tk.PhotoImage(file="pause_img.png")
next_image=tk.PhotoImage(file="next_img.png")


directory=askdirectory()
os.chdir(directory)
song_list=os.listdir()

mixer.init()

def play():
    mixer.music.load(listBox.get(tk.ACTIVE))
    label.config(text=listBox.get(tk.ACTIVE))
    mixer.music.play()
    
def prev():
    next_song=listBox.curselection()
    next_song=next_song[0]-1
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(listBox.get(next_song))
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def pause():
    if pauseButton["text"]=="pause":
        mixer.music.pause()
        pauseButton["text"]="play"
    else:
        mixer.music.unpause()
        pauseButton["text"]="pause" 

def next():
    next_song=listBox.curselection()
    next_song=next_song[0]+1
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(listBox.get(next_song))
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

listBox=tk.Listbox(canvas,fg="cyan",bg="black",width="100", font=('ds-digital',14))
listBox.pack(padx=15,pady=15)

label=tk.Label(canvas,text='',bg='black',fg='yellow',font=('ds-digital',18))
label.pack(pady=15)

top=tk.Frame(canvas,bg='black')
top.pack(padx=10,pady=5,anchor='center')

prevButton=tk.Button(canvas,text='prev',command=prev,image=prev_image,bg='black',borderwidth=0)
prevButton.pack(pady=15,in_=top,side='left')

stopButton=tk.Button(canvas,text='stop',command=stop,image=stop_image,bg='black',borderwidth=0)
stopButton.pack(pady=15,in_=top,side='left')

playButton=tk.Button(canvas,text='play',command=play,image=play_image,bg='black',borderwidth=0)
playButton.pack(pady=15,in_=top,side='left')

pauseButton=tk.Button(canvas,text='pause',command=pause,image=pause_image,bg='black',borderwidth=0)
pauseButton.pack(pady=15,in_=top,side='left')

nextButton=tk.Button(canvas,text='next',command=next,image=next_image,bg='black',borderwidth=0)
nextButton.pack(pady=15,in_=top,side='left')

x=0
for i in song_list:
    listBox.insert(x,i)
    x+=1

canvas.mainloop()
