from tkinter import *
import os
import urllib.request
import re
import webbrowser
from PIL import ImageTk, Image

root =  Tk()
root.title("DevApp")
root.iconbitmap("D:/Coding/Azure/DevApp/TestDauVao/AzureLogo.ico")

root.geometry("1920x1080")

bg = PhotoImage(file = "D:/Coding/Azure/DevApp/TestDauVao/bg.png")

my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

def shutdown():
    os.system("shutdown /p")

def playmusic():
    myLabel = Label(root, text= "Nhập tên bài hát (không có dấu)", font=("Arial", 14), bg= "#ffffff").place(x= 585, y= 510)
    e = Entry(root, width = 32, font=("Arial", 14), bg= "#ffffff")
    e.place(x= 535, y= 555)

    def open(seach):
        seach = ('+').join(seach.split())
        # lay url video do tren ytb
        open = "https://www.youtube.com/results?search_query=" + seach
        html = urllib.request.urlopen(open)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        url_link = "https://www.youtube.com/watch?v=" + video_ids[0]
        # mo video
        webbrowser.open(url_link)

    def Click():
        seach = e.get()
        open(seach)


    myButton = Button(root, text = "PLAY", command=Click, font=("Arial", 14), bg= "#ffffff")
    myButton.place(x= 670, y= 600)



def exit():
    a = 1
    while(True):
        if (a != 1):
            root.quit()


myLabel = Label(root, text= "Bạn muốn làm gì?!", justify='center')
button_playmusic = Button(root, text= "Bật nhạc", padx=8, pady=15, borderwidth=5, font=("Arial", 14), bg= "#ffffff", command= playmusic).place(x= 350, y= 380)
button_shutdown = Button(root, text = "Tắt máy", padx=10, pady=15, borderwidth=5, font=("Arial", 14), bg= "#ffffff", command=shutdown).place(x= 650, y= 380)
button_exit = Button(root, text= "Thoát", padx=16, pady=15, borderwidth=5, font=("Arial", 14), bg= "#ffffff", command= exit).place(x= 950, y= 380)



root.mainloop()

