from tkinter import *
def clicker():
    text.config(text='Bye')

def clicked():
    res=txt.get()
    name.config(text=res)

window = Tk()
window.title("my first gui program")
window.geometry('1920x1280') #window size
text = Label(window,
            text = 'Hey',
            font=('Arial Bold',60) #font and text size
            )
name = Label(window,
            text = ' Jack',
            font=('Arial Bold',70)
            )
#we could've just sent it as one text, but i’m just practicing
txt=Entry(window, width=10)
but=Button(window, text="Enter", comman=clicked)
wronger=Label(window,
              text='if name is incorrect, you can change it',
              font=('Arial Bold',40)
              )

but.grid(column=2, row=1)
txt.grid(column=1, row=1)
text.grid(column=0, row=0) #label spawner lol
name.grid(column=1, row=0)
btn = Button(window, text='click me', command=clicker)
btn.grid(column=0, row=1)
wronger.grid(column=0, row=2)
window.mainloop()


