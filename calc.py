from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title("Калькулятор")
tk.geometry("800x600")
tk.minsize(width = 800, height = 600)
tk.maxsize(width = 800, height = 600)

resText = ""

def calculating():
    global resText
    if resText == "":
        return 0
    try:
        resText = str(eval(resText))
        res.configure(state="normal")
        res.delete("1.0","end")
        res.insert(1.0, resText)
        res.configure(state="disabled")
    except ZeroDivisionError:
        messagebox.showerror("Помилка", "На 0 діліти не можна.")
    except SyntaxError:
        messagebox.showerror("Помилка", "Щось пішло не так :(")
    except OverflowError:
        messagebox.showerror("Помилка", "Помилка")
    except TypeError:
        messagebox.showerror("Помилка", "Щось пішло не так. Недопустимі значення.")
     
def entering(d):
   global resText
   if resText != "":
       if d in "+-*/" and resText[-1] in "+-*/":
           erase()
           entering(d)
   elif resText == "" and d in "+-*/":
       return 0
   res.configure(state="normal")
   if len(resText) <= 25:
       resText += d
       res.delete("1.0","end")
       res.insert(1.0, resText)
       res.configure(state="disabled")
   else:
        messagebox.showerror("Увага!", "На жаль, ви не можете ввести більше 25 символів!")
   
def clean():
    global resText
    resText = ""
    res.configure(state="normal")
    res.delete("1.0","end")
    res.configure(state="disabled")
    
def erase():
    global resText
    resText = resText[:-1]
    print(resText)
    res.configure(state="normal")
    res.delete("1.0","end")
    res.insert(1.0, resText)
    res.configure(state="disabled")

res = Text(tk, height=2, width=14, exportselection=0, font=("Century Gothic", 28))
res.place(relx=.35, rely = .13)
res.configure(state="disabled")
b = []
i = 0
for c in "789/456*123+C0.-()":
    if c == "C":
        x = Button(tk, text=c, command=clean, font=("Times New Roman", 14), width=5, height=2)
    else:
        x = Button(tk, text=c, command=lambda j=c: entering(j), font=("Times New Roman", 14), width=5, height=2)
    x.place(relx=(.35 + .1 * (i%4)), rely = (.3 + .12 * (i//4)))
    b.append(x)
    i += 1
butErase = Button(tk, text = "<--", font=("Century Gothic", 13), width=5, height=2, command = erase)
butErase.place(relx=.55, rely = .78) 
butRes = Button(tk, text="=", font=("Times New Roman", 14), width=5, height=2, command = calculating)
butRes.place(relx=.65, rely = .78)

tk.mainloop()