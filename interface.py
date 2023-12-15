from tkinter import *
from PIL import ImageTk, Image

def choose_sport():
    print("Sport domain selected")

def choose_math():
    print("Math domain selected")

def choose_culture():
    print("Culture marocaine domain selected")

def choose_programming():
    print("Programming domain selected")

game = Tk()
game.title('QUIZ GAME')
game.iconbitmap('icon.ico')
game.geometry("800x600")

domin = Frame(game)
domin.pack()
sport_label = Label(domin, text="Sport", bg="gray",fg="white", font=('Helvetica', 15))
sport_label.pack()
domin.place(x=20, y=0)



sport = ImageTk.PhotoImage(Image.open("OIP.jpeg"))
n1_label = Label(domin, image=sport)
n1_label.pack()
sp = Button(domin, text="Choisir le domaine de sport",   command=choose_sport, bg="lightblue", fg="black")
sp.pack()

domin2 = Frame(game )
domin2.pack()
math_label = Label(domin2, text="math",bg="gray",fg="white", font=('Helvetica', 15))
math_label.pack()
domin2.place(x=40, y=300)


math = ImageTk.PhotoImage(Image.open("math.jpeg"))
n2_label = Label(domin2, image=math)
n2_label.pack()
mat = Button(domin2, text="Choisir le domaine de math",   command=choose_math, bg="lightgreen", fg="black")
mat.pack()

domin3 = Frame(game )
domin3.pack()
mar_label = Label(domin3, text="culture marocaine",bg="gray",fg="white", font=('Helvetica', 15))
mar_label.pack()
math_label.pack()
domin3.place(x=500, y=40)



mar = ImageTk.PhotoImage(Image.open("MAR.jpeg"))
n3_label = Label(domin3, image=mar)
n3_label.pack()
MARO = Button(domin3, text="Choisir le domaine de culture marocan",  command=choose_culture, bg="lightcoral", fg="black")
MARO.pack()

domin4 = Frame(game  )
domin4.pack()
Pro_label = Label(domin4, text="Programmation",bg="gray",fg="white", font=('Helvetica', 15))
Pro_label.pack()
math_label.pack()
domin4.place(x=500, y=300)



prog = ImageTk.PhotoImage(Image.open("PRO.jpeg"))
n4_label = Label(domin4, image=prog)
n4_label.pack()
pro = Button(domin4, text="Choisir le domaine de programmation",  command=choose_programming, bg="lightyellow", fg="black")
pro.pack()

game.mainloop()
