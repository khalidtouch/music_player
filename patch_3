                              # imported files

from tkinter import *
from pygame import mixer
from tkinter import filedialog
from tkinter import messagebox
mixer.init()


                                            # window background
window = Tk()
window.title('Cosmic Music')
window.iconbitmap('C:/Users/USER/Pictures/microphone__1__HHa_icon.ico')
window.geometry('300x300')
text = Label(window, text="Let the Universe speak.")
text.pack()

                                            # defining control functions

def browse_file():
    global filename
    filename = filedialog.askopenfile()
    loadThenPlay(filename)
    

def about_us():
    messagebox.showinfo('Cosmic Music', 'This Music Player was designed by Xigma Interns 2019.')

def notLoaded(any_file):
    if any_file is None:
        return True


def printFilename(event):
    print(filename)

        # MenuBar
menubar = Menu(window)
window.config(menu = menubar)





        # sub-menubar
submenu = Menu(menubar, tearoff = 0 )
menubar.add_cascade(label = 'Music File', menu = submenu)
submenu.add_command(label = 'open files', command = browse_file)

submenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Profile', menu = submenu)
submenu.add_command(label = 'Isah Khalid')

submenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'History', menu = submenu)
submenu.add_command(label = 'This music app was developed....')

submenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'About', menu = submenu)
submenu.add_command(label = 'who we are', command = about_us)

submenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Exit', command = window.destroy)


    # control functions
pause = False

def loadThenPlay(any_file):
    mixer.music.load(any_file)
    mixer.music.play()
    statusbar['text'] = 'Music Now Playing'

def resume_music():
    global pause_state
    mixer.music.unpause()
    pause_state = False

def pause_music(event):
    mixer.music.pause()
    pause_state = True

def music_stopped():
    if statusbar['text'] == 'Music Stopped':
        return True

def play_button(event):
    statusbar['text'] = 'Now Playing... '
    try:
        resume_music()
        if music_stopped():
            loadThenPlay(filename)
    
    except: 
        messagebox.showerror('Cosmic Music','File not selected')



    # stop button
def stop_button(event):
    #print('stop')
    mixer.music.stop()
    statusbar['text'] = 'Music Stopped'
    statusbar['anchor'] = E

    # volume control
def volume_control(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)










                                            # play button
play_photo = PhotoImage(file = ("C:/Users/USER/Pictures/play-button.png"))
stop_photo = PhotoImage(file = ('C:/Users/USER/Pictures/stop.png'))
pause_photo = PhotoImage(file = ('C:/Users/USER/Pictures/pause.png'))

#adding a widget to make it clickable
play_Button = Button(window, image = play_photo)
play_Button.bind('<Button-1>', play_button)
play_Button.bind('<Button-2>', resume_music)
play_Button.bind('<Button-3>', resume_music)
play_Button.pack()

pause_Button = Button(window, image = pause_photo)
pause_Button.bind('<Button-1>', pause_music)
pause_Button.bind('<Button-2>', pause_music)
pause_Button.bind('<Button-3>', pause_music)
pause_Button.pack()

stop_Button = Button(window, image = stop_photo)
stop_Button.bind('<Button-1>', stop_button)
stop_Button.bind('<Button-2>', stop_button)
stop_Button.bind('<Button-3>', printFilename)
stop_Button.pack()


volume_control = Scale(window, from_ = 0, to = 100, command = volume_control, orient = HORIZONTAL)
volume_control.pack()
volume_control.set(15)
mixer.music.set_volume(15)



statusbar = Label(window, text = 'Cosmic Music App. Copyright 2019', relief = SUNKEN, anchor = CENTER)
statusbar.pack(side = BOTTOM, fill = X)








window.mainloop()
#window = (str(input('Enter to Close')))


