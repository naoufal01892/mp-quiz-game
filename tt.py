from tkinter import *
from tkinter import messagebox
import random

def quiz_game():
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

    def reset_buttons():
        for button in choice_buttons:
            button.config(bg="SystemButtonFace", state=NORMAL)

    game = Tk()
    game.title('QUIZ GAME')
    game.iconbitmap('icon.ico')
    game.geometry('700x600')

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
    question_label = Label(game, text="Sample Question", font=('Helvetica', 30))
    question_label.pack(pady=10)

    choice_button_1 = Button(game, text="Choice 1", font=('Helvetica', 20), bg="lightblue", fg="black",
                             command=lambda: check_answer(0))
    choice_button_1.pack()
    choice_button_1.place(x=150, y=160)

    choice_button_2 = Button(game, text="Choice 2", font=('Helvetica', 20), bg="lightblue", fg="black",
                             command=lambda: check_answer(1))
    choice_button_2.pack()
    choice_button_2.place(x=150, y=300)

    choice_button_3 = Button(game, text="Choice 3", font=('Helvetica', 20), bg="lightblue", fg="black",
                             command=lambda: check_answer(2))
    choice_button_3.pack()
    choice_button_3.place(x=420, y=160)

    choice_button_4 = Button(game, text="Choice 4", font=('Helvetica', 20), bg="lightblue", fg="black",
                             command=lambda: check_answer(3))
    choice_button_4.pack()
    choice_button_4.place(x=420, y=300)

    choice_buttons = [choice_button_1, choice_button_2, choice_button_3, choice_button_4]

    help_button = Button(game, text="Request Help", font=('Helvetica', 22), bg="lightgreen", fg="black",
                         command=request_help)
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

    correct_choice = 0

    update_timer()

    game.mainloop()

# Run the quiz game
quiz_game()
