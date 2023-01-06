import webbrowser
import tkinter
from tkinter import *

window = Tk()

firefoxbrowser = webbrowser.Mozilla("C:\\Program Files\
\Mozilla Firefox\\firefox.exe")

window.title("Firefox open links")

def getlink():
    url = text.get("1.0", END)
    links = url.split()
    for i in links :
        try :
            firefoxbrowser.open_new_tab(i) 
        except :
            firefoxbrowser.open(i)

text = Text(window)
text.pack()
linkbutton = Button(window, text="Run on Firefox", command=getlink)
linkbutton.pack()
window.mainloop()
