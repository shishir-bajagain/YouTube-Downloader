from tkinter import *
from pytube import YouTube

root = Tk()
root.title("YouTube Downloader")
root.geometry("650x600")


txt1 = Label(root,text = "Youtube Videos/Audio Download",font=("New Romania Times",25,"bold","underline"),fg="black")
txt1.place(x=70,y=20)

link = None #To have link as a Global Variable

def link_entry(text):
    global link  # Declare link as a global variable
    link = Entry(root, font=("New Romania Times", 20, "bold"), fg="black", border=5, width=30)
    link.place(x=100, y=110)
    link.insert(0, text)

#ClearInput function deletes the text written previously i.e Enter the Youtube link and Error!!! when pressing on Entry
def clearInput(event):
    global link  # Access the global link variable
    if link is not None:
        if link.get() == "Enter the YouTube Link..." or link.get() == "ERROR!!!":
            link.delete(0, END)

# Call link_entry to initialize the link variable
link_entry("Enter the YouTube Link...")

# Bind the clearInput function to the <FocusIn> event

if link is not None:
    link.bind("<FocusIn>", clearInput)


def display(yt_link):
    global link
    llink = YouTube(yt_link)
    tt = Label(root, text= llink.title,font=("New Romania Times",20,"bold","underline"),fg="black",relief= RAISED,bg="white")
    tt.place(x=60, y =400)



def download(vid,s_res):
    download_vid = vid.filter(only_video = True, res= s_res)
    download_vid[0].download()
    print("Download Successful!!")

def button(vid):
    z = 60
    button_lst = [f"button{i}" for i,k in enumerate(vid)]
    res_lst = [k.resolution for i,k in enumerate(vid)]
    for i in range(4):
        txt = button_lst[i]
        key = res_lst[i]
        txt = Button(root, text = key,border= 1, font=("New Romania Times",20,"bold","underline"),fg="white",relief= RAISED,bg="black",command=lambda val = key: download(vid,val))      
        txt.place(x=z,y=300)
        z += 150

def video():
    global link
    if link is not None:
        url = link.get()
        try:
            llink =  YouTube(url) #type: ignore
            vid = llink.streams.filter(only_video = True, mime_type="video/mp4") 
            button(vid)
        except Exception as e:
            print(e)
    else:
        pass
    

def audio():
    global link
    if link is not None:
        url = link.get()
        try:
            llink =  YouTube(url) #type: ignore
            vid = llink.streams.filter(only_audio = True, mime_type="audio/mp4") 
            vid[0].download()
        except Exception as e:
            print(e)
    else:
        pass

button1 = Button(root, text="Download Video",font=("New Romania Times",20,"bold"),fg="white",bg="red",border=3,relief= RAISED,command=video, state = DISABLED)
button1.place(x=70,y=210)

button2 = Button(root, text="Download Audio",font=("New Romania Times",20,"bold"),fg="white",bg="red",border=3,relief= RAISED,command=audio, state = DISABLED)
button2.place(x=340,y=210)

def checker():
    global link
    try:
        yt_link = YouTube(link.get()) #type: ignore
        button1.config(state= NORMAL)
        button2.config(state= NORMAL)
        display(link.get()) #type: ignore
    except Exception as e:
        button1.config(state= DISABLED)
        button2.config(state= DISABLED)
        link_entry("ERROR!!!")
        if link is not None:
            link.bind("<FocusIn>", clearInput)
        print(e)

buttoncheck = Button(root, text="Go",font=("New Romania Times",15,"bold"),fg="white",bg="grey",border=3,relief= RAISED,command=checker)
buttoncheck.place(x=570,y=110)


root.mainloop()
