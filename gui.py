from tkinter import *

window = Tk()  #makes a fucking window
window.geometry("400x400")
window.title("This is my window.")

icon = PhotoImage(file='Lexi button.png')
window.iconphoto(True,icon)
window.config(background="pink")
window.mainloop() #displays window, listen for events
