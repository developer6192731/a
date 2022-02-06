from tkinter import *

r = Tk()

def cb():
  q = t.get(1.0, "end-1c")
  ans = int(q)**3
  l.config(text=ans)
  


a = Button(r, text="Cube", command=cb)
t = Text(r,height=2, width=20)
l = Label(r)
t.pack()
a.pack()
l.pack()

r.mainloop()
