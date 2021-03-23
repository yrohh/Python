from pynput import mouse
import tkinter as tk

window=tk.Tk()
window.title("마우스 좌표 확인")
window.geometry("300x100+650+300")

Button = tk.Button(window, width=10, height=2, text="Start", command=lambda:gp())
Button.pack(expand=True, fill="both")
X_Entry = tk.Entry(window, width=10)
X_Entry.pack(expand=True, fill="both")
Y_Entry = tk.Entry(window, width=10)
Y_Entry.pack(expand=True, fill="both")

def gp():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    dp()

def on_click(x, y, button, pressed):
    global X, Y

    if pressed:
        X=x
        Y=y
    
    else:
        return False

def dp():
    X_Entry.delete(0, 'end')
    Y_Entry.delete(0, 'end')
    X_Entry.insert(0, X)
    Y_Entry.insert(0, Y)

window.mainloop()