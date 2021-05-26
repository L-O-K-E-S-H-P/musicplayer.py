def volumeup():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)
def stopmusic():
    mixer.music.stop()
def pausemusic():
    mixer.music.pause()
def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
def musicurl():
    dd=filedialog.askopenfilename()
    audiotrack.set(dd)
def createwidthes():
    ######################################################################## Labels
    TrackLabel=Label(root,text="Select the Audio Track:",background='LightSkyBlue',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)
    ####################################################################### Entry Box
    TrackLabelEntry=Entry(root,font=('arial',16,'italic bold'),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)
    ########################################################################## Buttons
    BrowseButton=Button(root,text='Search',bg='yellow',font=('arial',12,'italic bold'),width=15,bd=5,activebackground='lightgreen',command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)
    PlayButton = Button(root, text='Play', bg='green2', font=('arial', 12, 'italic bold'), width=15, bd=5,
                          activebackground='deeppink',command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)
    PauseButton = Button(root, text='Pause', bg='deeppink', font=('arial', 12, 'italic bold'), width=15, bd=5,
                        activebackground='yellow',command=pausemusic)
    PauseButton.grid(row=1, column=1, padx=20, pady=20)
    VolumeUpButton = Button(root, text='VolumeUp', bg='blue', font=('arial', 12, 'italic bold'), width=15, bd=5,
                        activebackground='deeppink',command=volumeup)
    VolumeUpButton.grid(row=1, column=2, padx=20, pady=20)
    VolumeDownButton = Button(root, text='VolumeDown', bg='darkorange', font=('arial', 12, 'italic bold'), width=15, bd=5,
                            activebackground='deeppink',command=volumedown)
    VolumeDownButton.grid(row=2, column=2, padx=20, pady=20)
    StopButton = Button(root, text='Stop', bg='red', font=('arial', 12, 'italic bold'), width=15, bd=5,
                            activebackground='deeppink',command=stopmusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)




#######################################################################################
from tkinter import*
from tkinter import filedialog
from pygame import mixer
root = Tk()
root.geometry('1100x500+200+50')
root.title('Simple Music Player..')
root.iconbitmap('audio.ico')
root.resizable(False,False)
root.configure(bg='lightskyblue')
####################################################################Global variables
audiotrack=StringVar()
######################################################################################### Create Slider
ss="Developed By Lokesh.P"
count=0
text=' '
SliderLabel=Label(root,text=ss,bg='lightskyblue',font=('arial', 40, 'italic bold'))
SliderLabel.grid(row=3,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTrick():
    global count,text
    if(count>=len(ss)):
        count=-1
        text=''
        SliderLabel.configure(text=text)
    else:
        text=text+ss[count]
        SliderLabel.configure(text=text)
    count+=1
    SliderLabel.after(200,IntroLabelTrick)
IntroLabelTrick()
mixer.init()
createwidthes()
root.mainloop()


