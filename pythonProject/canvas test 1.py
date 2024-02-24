from tkinter import *
import random

tk = Tk()
tk.title("EVOLUTION")
# tk.state("zoomed")
tk.attributes('-fullscreen', True)
canvas = Canvas(tk, width=tk.winfo_width(), height=tk.winfo_height())
canvas.pack()

world = []


def add_obj():
    x = tk.winfo_width() * random.random()
    y = tk.winfo_height() * random.random()
    r = 20 * random.random() + 2
    world.append(canvas.create_oval(x, y, x+r, y+r, fill="yellow"))


running = True
btn = canvas.create_window((100, 40), window=Button(tk, text='button', command=add_obj))
txt = canvas.create_text(100, 100, text='文字')
for i in range(9000):
    add_obj()
while running:
    for obj in world:
        canvas.move(obj, (random.random()-0.5)*5, (random.random()-0.5)*5)
    tk.update()

tk.mainloop()
