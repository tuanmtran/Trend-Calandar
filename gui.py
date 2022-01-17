import tkinter as tk
import cal_setup
import list_calendars
import create_event

window = tk.Tk()

def redCallBack():
    create_event.main(11)

def greenCallBack():
    create_event.main(2)

def orangeCallBack():
    create_event.main(6)

def purpleCallBack():
    create_event.main(3)

R = tk.Button(window, text = "Red", command = redCallBack, bg="red")
G = tk.Button(window, text = "Green", command = greenCallBack, bg="green")
O = tk.Button(window, text = "Orange", command = orangeCallBack, bg="orange")
P = tk.Button(window, text = "Purple", command = purpleCallBack, bg="purple")

R.pack()
G.pack()
O.pack()
P.pack()
window.mainloop()