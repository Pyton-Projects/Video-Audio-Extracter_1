
from tkinter import * # Importing Are tkinter module for our gui
r=Tk()

saved_file_path = Label(r, fg='purple3')
saved_file_path.place(x=1  , y=50)
convert_button = Button(r, text='Convert To Audio', bg='lightblue', activebackground='lightblue',state=DISABLED)
convert_button.place(x=175 + 10 + 2, y=110 + 50)
open_file_path=Label(r,fg='purple1')
open_file_path.place(x=1,y=75)
from tkinter import filedialog
from tkinter import messagebox 
def  mp4_to_mp3():
    import os
    import pathlib
    import moviepy.editor
    global asking_file_to_save 
    global star__
    messagebox.showwarning('Warning!',' Remember Put File Extension (In Small Letters) At The End Of The File Name') # image converter,insertation of a mp3 to a mp4 # advance sppech recognization
    asking_file_to_save=filedialog.asksaveasfile('wb',title='Save As',filetypes=(('mp3','*.mp3',),("mp3","*.mp3"),('wav','*.wav'),('ogg','*.ogg')))
    star__=asking_file_to_save.name 
    sre=str(os.path.basename(star__))    
    user_video=moviepy.editor.VideoFileClip(star_a)# write audio file ! using open function
    audio=user_video.audio.write_audiofile(sre)
    messagebox.showinfo('Message','''Correct File Extenstion.(mp3,wav,ogg) Can Be Converted''')
    global s
    s=asking_file_to_save.name
    path = f'{s}'
    global extesntion
    extesntion = (pathlib.Path(path)).suffix    
def dialog_mp4():# write audio file in that location...
    from tkinter import filedialog
    global filename_
    global extesntion_
    global star_a
    global path_opend_file_
    filename_=filedialog.askopenfile('rb',filetype=(("mp4","*.mp4"),('mp4','*.mp4')),title='Open Mp4 File')
    try:
        path_opend_file_=(filename_.name)
        star_a=str(path_opend_file_)
        check=(star_a.endswith('.mp4'))
        if check==True:
            convert_button.config(command=mp4_to_mp3)
            convert_button.config(state=NORMAL)
            open_file_path.config(text=f'Opened File Path:-{path_opend_file_}')
            length_of_opend_file=(len(path_opend_file_))
        if length_of_opend_file>=70:
            open_file_path.config(text=f'''Opend File Path:--{path_opend_file_}''')
            open_file_path.place(x=1,y=60)
    except Exception :
        convert_button.config(state=DISABLED)
r.minsize(500,200)
r.maxsize(500,200)
r.title('Mp4 To Mp3')
r.geometry('500x300')
heading=Label(r,text='Video (Mp4) File to Audio File ',fg='cyan4')
heading.place(x=100+25+5+5+15,y=1)
browse_mp4=Button(r,text='Browse A Mp4 File',bg='pink',activebackground='pink',command=dialog_mp4)
browse_mp4.place(x=175,y=100+10)
browse_mp4.bind('<Button-1>')
r.mainloop()
# mp3  to acc or acc to mp3
# filedialog speech recognition,os  and how to sava a audio file and get the path of that file.
# song lyrics game.
# how to know the file extension of a file.
# how  to change border colour in a entry widget/.
# main comments:
# HOW TO KNOW THE TKINTER APPLICATION IS NOT RESPONDING!
# go and create an codecheif account!
# lets goto five star coding!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# create image converter.
# lets go to five star at code_chef
# how to get file path when file saved...
# how to save a audio file
# how to stop tkinter to not responding!,
# wav best sound quality!
# fix lenthgh bug!!!
# diffrent file video extenstion.
# what is the extenstion of a FLODER.
# MP3 FILE INSERTION IN A MP4 FILE!
# my 9 projects: