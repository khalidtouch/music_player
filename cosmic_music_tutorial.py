# imported files
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter import messagebox
import os
mixer.init()
background_color = '#697382'
textColor = 'white'
muted = False

# window background
window = Tk()
window.title("Music Player")
window.iconbitmap('C:/Users/USER/Pictures/microphone__1__HHa_icon.ico')
#window.geometry("650x350")

text = Label(window, text="To infinity and beyond")
text.pack()
text.config(background=background_color)
text.config(fg='white')

# Menu Bar
menuBar = Menu(window)
window.config(menu=menuBar)
window.config(background=background_color)


# MenuBar Functions
def browse():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)


def about_us():
    messagebox.showinfo("Music Player", "Don't Dare Miss The Experience")


# SubMenu Bar
MusicFile = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Music File", menu=MusicFile)
MusicFile.add_command(label="Open Files", command=browse)
MusicFile.config(background=background_color)

Profile = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Profile", menu=Profile)
Profile.add_command(label="Name")
Profile.config(background=background_color)

History = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="History", menu=History)
History.add_command(label="Founded")
History.config(background=background_color)

About = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="About", menu=About)
About.add_command(label="About us", command=about_us)
About.config(background=background_color)



Exit = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Exit", command=window.destroy)
Exit.config(background=background_color)

'''To create images
widgetPhoto = Label(window, image = photo)
widgetPhoto.pack()'''

def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusBar["text"] = "PAUSED"
    statusBar['anchor'] = CENTER


def play_button():
    try:
        paused
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusBar["text"] = "Now Playing" + " - " + os.path.basename(filename)
            #statusBar['anchor'] = W
        except:
            messagebox.showerror("Error", "Please select a file")
    else:
        mixer.music.unpause()
        statusBar["text"] = "Now Playing"

def stop_music():
    mixer.music.stop()
    statusBar["text"] = "Stopped"
    statusBar['anchor'] = E


def volume_control(val):
    global vol
    vol = int(val)/100
    mixer.music.set_volume(vol)

def Rewind_button():
    play_button()
    statusBar['text'] = 'Music Restarted'

def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(30)
        volume_button.config(image = volume_photo)
        volume.set(30)
        muted = False
    else:
        mixer.music.set_volume(0)
        volume_button.config(image = mute_photo)
        volume.set(0)
        muted = True





# Frame
InnerFrame = Frame(window)
InnerFrame.pack(padx=10)
InnerFrame.config(background=background_color)

downframe = Frame(window)
downframe.pack()
downframe.config(background=background_color)

# rewind button
rewind_photo = PhotoImage(file='C:/Users/USER/Pictures/skip-back-button.png')
rewind_button = Button(InnerFrame, image = rewind_photo)
rewind_button.pack(side=LEFT)

# Pause Buttonn
pause_photo = PhotoImage(file='C:/Users/USER/Pictures/pause_new.png')
Pause_button= Button(InnerFrame, image=pause_photo, command=pause_music)
Pause_button.pack(side=LEFT, padx=5)
Pause_button.config(background=background_color)
Pause_button.config(highlightcolor=background_color)
# Play Button
play_photo = PhotoImage(file='C:/Users/USER/Pictures/play_new.png')
Play_button = Button(InnerFrame, image=play_photo, command=play_button)
Play_button.pack(side=LEFT, padx=5)
Play_button.config(background=background_color)
# Stop Button
stop_photo = PhotoImage(file='C:/Users/USER/Pictures/stop_new.png')
Stop_button = Button(InnerFrame, image=stop_photo, command=stop_music)
Stop_button.pack(side=LEFT, padx=5)
Stop_button.config(background=background_color)



mute_photo = PhotoImage(file='C:/Users/USER/Pictures/muted.png')
volume_photo = PhotoImage(file='C:/Users/USER/Pictures/speaker.png')
volume_button = Button(downframe, image = volume_photo, command= mute_music)
volume_button.pack(side=LEFT)
volume_button.config(width=20)
volume_button.config(height=20)
# Volume Control
volume = Scale(downframe, from_=0, to=100, command=volume_control, orient=HORIZONTAL)
volume.pack(side=LEFT)
volume.set(30)
mixer.music.set_volume(30)
volume.config(background=background_color)



statusBar = Label(window, text="Music Player copyright 2019", relief=FLAT, anchor=CENTER)
statusBar.pack(side=BOTTOM, fill=X)

window.mainloop()

'window = input("Enter to exit ")'
