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

def about_us():
    messagebox.showinfo('Cosmic Music', 'This Music Player was designed by Xigma Interns 2019.')

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
def play_button():

    try:
        mixer.music.load(filename)
        mixer.music.play()
        statusbar['text'] = 'Music Now Playing'
        statusbar['anchor'] = W
    except:
        messagebox.showerror('Cosmic Music','File not selected')



    # stop button
def stop_button():
    #print('stop')
    mixer.music.stop()
    statusbar['text'] = 'Music Stopped'
    statusbar['anchor'] = E

    # volume control
def volume_control(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)









                                            # play button
play_photo = PhotoImage(file = ("C:/Users/USER/Pictures/play-button-2.png"))
stop_photo = PhotoImage(file = ('C:/Users/USER/Pictures/stop-button.png'))

#adding a widget to make it clickable
play_Button = Button(window, image = play_photo, command = play_button)
play_Button.pack()
stop_Button = Button(window, image = stop_photo, command = stop_button)
stop_Button.pack()
volume_control = Scale(window, from_ = 0, to = 100, command = volume_control, orient = HORIZONTAL)
volume_control.pack()
volume_control.set(15)
mixer.music.set_volume(15)


statusbar = Label(window, text = 'Cosmic Music App. Copyright 2019', relief = SUNKEN, anchor = CENTER)
statusbar.pack(side = BOTTOM, fill = X)








window.mainloop()
#window = (str(input('Enter to Close')))


