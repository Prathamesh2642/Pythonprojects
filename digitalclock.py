import time
import tkinter as tk

window=tk.Tk()
window.title("Clock")
window.geometry("200x80")
window.configure(bg="red")
# window.resizable(False,False)

main_clock=tk.Label(window,fg="purple",font=("Times"))
main_clock.place(x=20,y=20)

def updatelabel():
    currentime=time.strftime("%H : %M : %S")
    main_clock.configure(text=currentime)
    main_clock.after(80,updatelabel)

updatelabel()
tk.mainloop()
