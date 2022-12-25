# YouTube Downloader
from pytube import YouTube
from tkinter import*
from tkinter import messagebox, filedialog
import youtube_dl


def widgets():
    root = Frame(window, bg='#181818')
    root.pack()
    link_label = Label(root,
                       text="YouTube link :",
                       fg='#aaaaaa',
                       bg="#3d3d3d",
                       pady=5,
                       padx=5)
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)

    window.link_text = Entry(root,
                             width=47,
                             fg="#aaaaaa",
                             bg="#212121",
                             textvariable=video_Link,
                             font="Arial 11")
    window.link_text.grid(row=1,
                          column=1,
                          pady=5,
                          padx=5,
                          columnspan=2)

    destination_label = Label(root,
                              text="Destination :",
                              fg="#aaaaaa",
                              bg="#3d3d3d",
                              pady=5,
                              padx=9)
    destination_label.grid(row=2,
                           column=0,
                           pady=5,
                           padx=5)
    destinationText = Entry(root,
                            width=27,
                            textvariable=download_Path,
                            fg="#aaaaaa",
                            bg="#212121",
                            font="Arial 14")
    destinationText.grid(row=2,
                         column=1,
                         pady=5,
                         padx=5)
    browse = Button(root,
                    text="Browse",
                    command=Browse,
                    fg="#aaaaaa",
                    width=10,
                    bg="#3d3d3d",
                    relief=GROOVE)
    browse.grid(row=2,
                column=2,
                pady=1,
                padx=1)

    high_reseltion = Button(root, text="high reseltion video",
                            font=("Arial", 13),
                            fg="#ffffff",
                            bg="#3d3d3d",
                            width=20,
                            activeforeground="#3776ab",
                            activebackground="black",
                            pady=10,
                            padx=15,
                            relief=GROOVE,
                            command=High_reseltion)
    high_reseltion.grid(row=3,
                        column=1,
                        pady=5,
                        padx=20)

    low_reseltion = Button(root,
                           text="low reseltion mp4",
                           font=("Arial", 13),
                           fg="#ffffff",
                           bg="#3d3d3d",
                           width=20,
                           activeforeground="#3776ab",
                           activebackground="black",
                           pady=10,
                           padx=15,
                           relief=GROOVE,
                           command=Low_reseltion)
    low_reseltion.grid(row=4,
                       column=1,
                       pady=5,
                       padx=20)

    audio = Button(root, text="MP3", font=("Arial", 13),
                   fg="#ffffff",
                   bg="#3d3d3d",
                   width=20,
                   activeforeground="#3776ab",
                   activebackground="black",
                   pady=10,
                   padx=15,
                   relief=GROOVE,
                   command=Audio)
    audio.grid(row=5,
               column=1,
               pady=5,
               padx=20)


def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_Directory)


def High_reseltion():
    yt = video_Link.get()
    download_Folder = download_Path.get()
    yd = YouTube(yt)
    print("Title: ", yd.title)
    window.title(f"Downloading..{yd.title}")
    videoStream = yd.streams.get_highest_resolution()
    videoStream.download(download_Folder)

    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)


def Low_reseltion():
    yt = video_Link.get()
    download_Folder = download_Path.get()
    yd = YouTube(yt)
    print("Title: ", yd.title)
    window.title(f"Downloading..{yd.title}")
    videoStream = yd.streams.get_lowest_resolution()
    videoStream.download(download_Folder)

    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)


def Audio():
    yt = video_Link.get()
    download_Folder = download_Path.get()
    video_info = youtube_dl.YoutubeDL().extract_info(url=yt, download=False)
    filename = f"{video_info['title']}.mp3"
    window.title(f"Downloading..{video_info.get('title',None)}")
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': download_Folder + filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    window.title(f"{video_info.get('title',None)} Downloaded")
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)


window = Tk()
icon = PhotoImage(file='YT icon.png')
window.title("YouTube Downloader")
window.iconphoto(True, icon)
window.resizable(False, False)
window.config(background='#181818')

window_width = 520
window_height = 280

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))


video_Link = StringVar()
download_Path = StringVar()

widgets()

window.mainloop()
