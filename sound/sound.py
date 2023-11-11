# importing required module
from playsound import playsound
from tkinter import*

root = Tk() 
root.title('GeeksforGeeks sound player') #giving the title for our window
root.geometry("500x400")

# making function 
def play():
	playsound('1.mp3')
 
def validation():
    playsound()
    
def error():
    playsound()

title=Label(root,text="GeeksforGeeks",bd=9,relief=GROOVE,
			font=("times new roman",50,"bold"),bg="white",fg="green") 
title.pack(side=TOP,fill=X) 


play_button = Button(root, text="Play Song", font=("Helvetica", 32),
					relief=GROOVE, command=play)
play_button.pack(pady=20)

info=Label(root,text="Click on the button above to play song ",
		font=("times new roman",10,"bold")).pack(pady=20)
root.mainloop()
