from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random

def choose_sport():
    setup_quiz("Sport", "sports.png", 0)
    game.withdraw()


def choose_math():
    setup_quiz("Math", "mathXX.png", 1)

def choose_culture():
    setup_quiz("Culture marocaine", "moroco.png", 2)

def choose_programming():
    setup_quiz("Programming", "programation.png", 3)

def setup_quiz(domain, image_path, correct_choice):
    game = Toplevel()
    game.title('QUIZ GAME')
    game.iconbitmap('icon.ico')
    game.geometry("700x600")

    bg = PhotoImage(file="fgh.jpeg.png")
    label1 = Label(game, image=bg, width=700, height=700)
    label1.place(x=0, y=0)

    timer_label = Label(game, text="Timer: 0 ", bg="red", fg="black", font=('Helvetica', 20))
    timer_label.pack(pady=15)
    timer_label.place(x=10, y=10)

    coins = 0
    coins_label = Label(game, text=f"Coins: {coins}", font=('Helvetica', 12))
    coins_label.pack(pady=10)
    coins_label.place(x=600, y=50)

    score = 0
    score_label = Label(game, text=f"Score: {score}", bg="black", fg="white", font=('Helvetica', 20))
    score_label.pack(padx=10)
    score_label.place(x=570, y=10)

    question_label = Label(game, text=f"{domain} Question", font=('Helvetica', 30))
    question_label.pack(pady=10)

    choice_button_1 = Button(game, text="Choice 1", font=('Helvetica', 20), bg="lightblue", fg="black", command=check_answer_1)
    choice_button_1.pack()
    choice_button_1.place(x=150, y=160)

    choice_button_2 = Button(game, text="Choice 2", font=('Helvetica', 20), bg="lightblue", fg="black", command=check_answer_2)
    choice_button_2.pack()
    choice_button_2.place(x=150, y=300)

    choice_button_3 = Button(game, text="Choice 3", font=('Helvetica', 20), bg="lightblue", fg="black", command=check_answer_3)
    choice_button_3.pack()
    choice_button_3.place(x=420, y=160)

    choice_button_4 = Button(game, text="Choice 4", font=('Helvetica', 20), bg="lightblue", fg="black", command=check_answer_4)
    choice_button_4.pack()
    choice_button_4.place(x=420, y=300)

    choice_buttons = [choice_button_1, choice_button_2, choice_button_3, choice_button_4]

    help_button = Button(game, text="Request Help", font=('Helvetica', 22), bg="lightgreen", fg="black", command=request_help)
    help_button.pack(pady=10)
    help_button.place(x=270, y=430)

    time_left = 10

    def update_timer():
        nonlocal time_left
        timer_label.config(text=f"Timer: {time_left}")
        if time_left > 0:
            time_left -= 1
            game.after(1000, update_timer)
        else:
            messagebox.showinfo("Time's Up!", "Sorry, you ran out of time.")
            reset_timer()

    def reset_timer():
        nonlocal time_left
        time_left = 10
        update_timer()

    def check_answer_1():
        check_answer(0)

    def check_answer_2():
        check_answer(1)

    def check_answer_3():
        check_answer(2)

    def check_answer_4():
        check_answer(3)

    def check_answer(choice):
        nonlocal score, coins
        for i, button in enumerate(choice_buttons):
            if i == correct_choice:
                button.config(bg="green")
                if i == choice:
                    score += 10
                    coins += 1
                    coins_label.config(text=f"Coins: {coins}")
                    score_label.config(text=f"Score: {score}")
            elif i != choice:
                button.config(bg="red")

        for button in choice_buttons:
            button.config(state=DISABLED)

    def request_help():
        nonlocal coins
        messagebox.showinfo("Help", "You requested help!")
        wrong_choices = [i for i in range(len(choice_buttons)) if i != correct_choice]
        if wrong_choices:
            choice_to_remove = random.choice(wrong_choices)
            choice_buttons[choice_to_remove].destroy()

        coins -= 1
        coins_label.config(text=f"Coins: {coins}")

    reset_timer()
    update_timer()

    game.mainloop()


game = Tk()
game.title('QUIZ GAME')
game.iconbitmap('icon.ico')
game.geometry("800x600")

domin = Frame(game)
domin.pack()
sport_label = Label(domin, text="Sport", bg="gray", fg="white", font=('Helvetica', 15))
sport_label.pack()
domin.place(x=20, y=0)

sport = ImageTk.PhotoImage(Image.open("OIP.jpeg"))
n1_label = Label(domin, image=sport)
n1_label.pack()
sp = Button(domin, text="Choisir le domaine de sport", command=lambda:choose_sport, bg="lightblue", fg="black")
sp.pack()

domin2 = Frame(game)
domin2.pack()
math_label = Label(domin2, text="math", bg="gray", fg="white", font=('Helvetica', 15))
math_label.pack()
domin2.place(x=40, y=300)

math = ImageTk.PhotoImage(Image.open("math.jpeg"))
n2_label = Label(domin2, image=math)
n2_label.pack()
mat = Button(domin2, text="Choisir le domaine de math", command=choose_math, bg="lightgreen", fg="black")
mat.pack()

domin3 = Frame(game)
domin3.pack()
mar_label = Label(domin3, text="culture marocaine", bg="gray", fg="white", font=('Helvetica', 15))
mar_label.pack()
math_label.pack()
domin3.place(x=500, y=40)

mar = ImageTk.PhotoImage(Image.open("MAR.jpeg"))
n3_label = Label(domin3, image=mar)
n3_label.pack()
MARO = Button(domin3, text="Choisir le domaine de culture marocan", command=choose_culture, bg="lightcoral", fg="black")
MARO.pack()

domin4 = Frame(game)
domin4.pack()
Pro_label = Label(domin4, text="Programmation", bg="gray", fg="white", font=('Helvetica', 15))
Pro_label.pack()
math_label.pack()
domin4.place(x=500, y=300)

prog = ImageTk.PhotoImage(Image.open("PRO.jpeg"))
n4_label = Label(domin4, image=prog)
n4_label.pack()
pro = Button(domin4, text="Choisir le domaine de programmation", command=choose_programming, bg="lightyellow", fg="black")
pro.pack()

game.mainloop()