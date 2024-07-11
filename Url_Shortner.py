#URLShortner

from tkinter import *
import pyshorteners
import pyshorteners.shorteners

win = Tk()
win.geometry("400x270")
win.configure(bg="Grey")

#ButtonFunction
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)

#Label for entering user url
Label(win,text="Enter Your URL",font="impack 20 bold",bg="black",fg="white").pack(fill="x")

#EntryBox
entry1 = Entry(win,font="10",bd=3,width=40)
entry1.pack(pady=30)

#Button
Button(win,text="Click Me",font="impack 15 bold",bg="black",fg="white",command=short).pack()

#Entry
entry2 = Entry(win,font="impack 15 bold",bg="grey",width=24,bd=0)
entry2.pack(pady=30)

mainloop()
