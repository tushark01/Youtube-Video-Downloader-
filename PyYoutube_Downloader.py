from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('600x400')
root.resizable(0,0)

root.title("Youtube video downloader pro")

Label(root,text = 'Youtube Video Downloader', font ='arial 22 bold').pack()    

link = StringVar()
Label(root, text = 'Paste Video Link Here:', font = 'arial 17 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 17').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 17 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()