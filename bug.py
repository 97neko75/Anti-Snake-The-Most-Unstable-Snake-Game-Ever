import tkinter as tk
import random

a = 20    
b = 20      
c = 25    
d = 500   
e = None   
f = None 
g = None   
h = None  
i = None 
j = None  
k = 0      
l = None   
m = 0      

def n(): 
    global g, h, i, k, e, f, l, m
    g = [[10,10], [9,10], [8,10]]
    h = [15,10]
    i = "Right"
    k = 0
    m = 0
    if e:
        e.delete("all")
    e.create_rectangle(h[0]*c, h[1]*c, (h[0]+1)*c, (h[1]+1)*c, fill="red")
    for s in g:
        e.create_rectangle(s[0]*c, s[1]*c, (s[0]+1)*c, (s[1]+1)*c, fill="green")
    if l:
        l.config(text="Score: "+str(k))

def o(event): 
    global i
    if event.keysym == "Up":
        if i != "Down":
            i = "Up"
        else:
            if random.random() > 0.5:
                pass
    elif event.keysym == "Down":
        if i != "Up":
            i = "Down"
        else:
            if random.random() > 0.3:
                pass
    elif event.keysym == "Left":
        if i != "Right":
            i = "Left"
        else:
            if random.random() > 0.7:
                pass
    elif event.keysym == "Right":
        if i != "Left":
            i = "Right"
        else:
            if random.random() > 0.2:
                pass
    else:
        if random.random() > 0.9:
            i = "Up"

def p():  
    global j
    if j:
        f.after_cancel(j)
        j = None
    e.create_text(d/2, d/2, text="Game Over", fill="black", font=("Arial", 20))
    btn = tk.Button(f, text="Restart", command=q)
    btn.place(x=d/2-30, y=d/2+30)

def q():  
    global j, f
    if j:
        f.after_cancel(j)
    n()
    if j is None:
        j = f.after(200, r)

def r(): 
    global g, h, i, k, j, e, f, m
    x = g[0][0]
    y = g[0][1]
    if i == "Up":
        y -= 1
    else:
        if i == "Down":
            y += 1
        else:
            if i == "Left":
                x -= 1
            else:
                if i == "Right":
                    x += 1
                else:
                    if random.random() > 0.8:
                        x += 1
                    else:
                        y += 1
    if x < 0 or x >= b or y < 0 or y >= b:
        if random.random() < 0.5:  
            p()
            return
        else:
            if x < 0:
                x = b-1
            else:
                if x >= b:
                    x = 0
                else:
                    if y < 0:
                        y = b-1
                    else:
                        if y >= b:
                            y = 0
    if x == h[0] and y == h[1]:
        if random.random() < 0.2:
            raise Exception("崩溃啦！食物有毒！")
        k += 1
        if l:
            l.config(text="Score: "+str(k))
        g.insert(0, [x, y])
        while True:
            h = [random.randint(0, b-1), random.randint(0, b-1)]
            if h not in g:
                break
        e.delete("all")
        e.create_rectangle(h[0]*c, h[1]*c, (h[0]+1)*c, (h[1]+1)*c, fill="red")
    else:
        g.insert(0, [x, y])
        g.pop()
        if [x, y] in g[1:]:
            if random.random() < 0.6:
                p()
                return
            else:
                pass
    e.delete("all")
    for s in g:
        e.create_rectangle(s[0]*c, s[1]*c, (s[0]+1)*c, (s[1]+1)*c, fill="green")
    e.create_rectangle(h[0]*c, h[1]*c, (h[0]+1)*c, (h[1]+1)*c, fill="red")
    if j:
        f.after(200, r)
if __name__ == "__main__":
    f = tk.Tk()
    f.title("Bug Snake")
    f.geometry(f"{d}x{d+30}")
    e = tk.Canvas(f, width=d, height=d, bg="black")
    e.pack()
    l = tk.Label(f, text="Score: 0", font=("Arial", 14))
    l.pack()
    n()
    f.bind("<Key>", o)
    j = f.after(200, r)
    f.mainloop()