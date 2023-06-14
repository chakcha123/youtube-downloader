from tkinter import *
from PIL import ImageTk
from pytube import YouTube
from tkinter.filedialog import askdirectory



def downloader():
    video_url = url_ent.get()
    try:
        yt = YouTube(video_url)
    except:
        progress_lbl.config(text="Invalid video URL!")
        return
    stream = yt.streams.get_highest_resolution()
    download_dir = askdirectory()
    if download_dir:
        stream.download(download_dir)
        progress_lbl.config(text="Download complete!")



root = Tk()                             
root.title('Video Downloader')                      
root.iconbitmap('1.ico')               
root.geometry('800x500')                
root.resizable(0,0)

bgimg = ImageTk.PhotoImage(file='bg.png')         
bgLabel = Label(root,image=bgimg)          
bgLabel.place(x=0,y=0)

url_ent = Entry(root,font=('bold',18),width=15,bg='black',fg='white')
url_ent.place(x=480,y=200)

D_btn = Button(root,text='Download',font=('bold',16),width=15,bg='black',fg='white',command=downloader)
D_btn.place(x=485,y=270)

quit_btn = Button(root,text='Quit',font=('bold',12),width=10,bg='black',fg='white',height=1,command=root.quit)
quit_btn.place(x=525,y=360)

progress_lbl = Label(root,font=('bold',18),width=15,fg='green',bg='white')
progress_lbl.place(x=80, y=70)




root.mainloop()
