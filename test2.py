# https://www.pynote.net/archives/1713
import time
import tkinter as tk

def test():
    # time.sleep(1)
    print("hello")

def __writeText():
    text.insert(tk.END, str(time.time())+'\n')
    root.after(1000, __writeText)  # again forever
    test()

root = tk.Tk()
root.geometry("+660+240")
text = tk.Text(root)
text.pack()
root.after(1000, __writeText)

root.mainloop()