# IMPORT REQUIRED MODULES

from tkinter import *
import random
from tkinter import messagebox
import pygame
from pygame import mixer
from playsound import playsound

# FIRST WINDOW INTERFACE
window1 = Tk()
window1.title("MEMGE")
window1.geometry("1284x707")

# DEFINE IMAGE
bg = PhotoImage(file="title.png")

# BACKGROUND MUSIC
pygame.init()

pygame.mixer.init()
mixer.music.load("title-_AudioTrimmer.com_-_1_.wav")
mixer.music.play(-1)

# CREATE CANVAS
my_canvas = Canvas(window1, width=1284, height=707)
my_canvas.pack(fill="both", expand=True)

# SET IMAGE IN CANVAS
my_canvas.create_image(0, 0, image=bg, anchor="nw")

# ADD A LABEL
my_canvas.create_text(770, 200, text="WELCOME", font=("Jokerman", 40), fill="white")
my_canvas.create_text(770, 70, text="JAWAHAR NAVODAYA VIDYALAYA", font=("Jokerman", 40), fill="white")
my_canvas.create_text(770, 300, text="MemGE", font=("Jokerman", 70), fill="grey")
my_canvas.create_text(770, 400, text="Memory Game for everyone", font=("Jokerman", 20), fill="grey")

# FUNCTION TO EXIT GAME
def quit(event=None):
    mixer.music.stop()
    window1.destroy()

# DEFINE SOME VARIABLES
count = 0
answer_list = []
answer_dict = {}
moves = 0

# FUNCTION TO START GAME
def game(event=None):
    mixer.music.stop()
    window = Tk()
    window.title("MEMGE")
    window.geometry("1284x707")
    window1.destroy()

    global winner
    winner = 0 

    # CREATE MATCHES
    global matches
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    random.shuffle(matches)

    # CREATE BUTTON FRAME
    my_frame = Frame(window)
    my_frame.pack(pady=10)

    # CREATING A LABEL
    my_label = Label(window, text="")
    moves_label = Label(window, text="")
    reset_label = Label(window, text="PRESS BACKSPACE TO RESET GAME")
    reset_label.pack(pady=20)
    my_label.pack(pady=20)
    moves_label.pack(pady=100)

    # CREATE RESET DEFINITION
    def reset(event):
        global matches, winner
        winner = 0
        # CREATE MATCHES
        matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
        random.shuffle(matches)

        # RESET LABEL
        my_label.config(text="")

        # RESET COLOURS
        colortile = open("colorsmemge.txt")
        allcolors = colortile.read()
        liscolors = allcolors.split("\n")
        color1 = random.randint(0, 996)
        rc = liscolors[color1]

        # RESET OUR TILES
        button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
        for button in button_list:
            button.config(text="", bg=rc, state="normal")

    # CREATE WINNER DEFINITION
    def win():
        global moves
        my_label.config(text="CONGRATULATIONS! YOU WON")
        mixer.music.load("gaming-sound-effect-hd.mp3")
        mixer.music.play(2)
        moves_label.config(text=moves)
        button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
        for button in button_list:
            button.config(bg="yellow")

    # FUNCTION FOR CLICKING BUTTONS
    def button_click(eff,b,number):
        global count, answer_list, answer_dict, winner, moves
        if b["text"] == "" and count < 2:
            b["text"] = matches[number]
            moves += 1
            if matches[number] == 1:
                playsound("8d82b5_The_Number_1_Sound_Effect.mp3")

            if matches[number] == 2:
                playsound("8d82b5_The_Number_2_Sound_Effect.mp3")

            if matches[number] == 3:
                playsound("8d82b5_The_Number_3_Sound_Effect.mp3")

            if matches[number] == 4:
                playsound("8d82b5_The_Number_4_Sound_Effect.mp3")

            if matches[number] == 5:
                playsound("8d82b5_The_Number_5_Sound_Effect.mp3")

            if matches[number] == 6:
                playsound("8d82b5_The_Number_6_Sound_Effect.mp3")

            print(matches[number])
            answer_list.append(number)
            answer_dict[b] = matches[number]
            count += 1

        # CHECK CORRECT OR NOT
        if len(answer_list) == 2:
            if matches[answer_list[0]] == matches[answer_list[1]]:
                my_label.config(text="MATCH")
                playsound("win-applause-game-sound-fx.mp3")

                for key in answer_dict:
                    key["state"] = "disabled"
                count = 0
                answer_list = []
                answer_dict = {}

                winner += 1
                if winner == 6:
                    win()

            else:
                my_label.config(text="NOT MATCHED")
                count = 0
                answer_list = []
                playsound("error-notification-banjo-45430.mp3")

                messagebox.showinfo("Incorrect!", "Incorrect")
                for key in answer_dict:
                    key["text"] = ""
                answer_dict = {}

    # GIVING COLOURS TO TILES
    colortile = open("colorsmemge.txt")
    allcolors = colortile.read()
    liscolors = allcolors.split("\n")
    color1 = random.randint(0, 996)
    rc = liscolors[color1]

    # DEFINE OUR BUTTONS
    b0 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b0, 0),
                relief="groove")
    b1 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b1, 1),
                relief="groove")
    b2 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b2, 2),
                relief="groove")
    b3 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b3, 3),
                relief="groove")
    b4 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b4, 4),
                relief="groove")
    b5 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b5, 5),
                relief="groove")
    b6 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b6, 6),
                relief="groove")
    b7 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b7, 7),
                relief="groove")
    b8 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b8, 8),
                relief="groove")
    b9 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b9, 9),
                relief="groove")
    b10 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b10, 10),
                 relief="groove")
    b11 = Button(my_frame, text="", bg=rc, font=("Arial", 20), height=3, width=6, command=lambda: button_click(b11, 11),
                 relief="groove")

    window.bind("<q>", lambda eff: button_click(eff,b0,0))
    window.bind("<w>", lambda eff: button_click(eff,b1,1))
    window.bind("<e>", lambda eff: button_click(eff,b2,2))
    window.bind("<r>", lambda eff: button_click(eff,b3,3))
    window.bind("<a>", lambda eff: button_click(eff,b4,4))
    window.bind("<s>", lambda eff: button_click(eff,b5,5))
    window.bind("<d>", lambda eff: button_click(eff,b6,6))
    window.bind("<f>", lambda eff: button_click(eff,b7,7))
    window.bind("<z>", lambda eff: button_click(eff,b8,8))
    window.bind("<x>", lambda eff: button_click(eff,b9,9))
    window.bind("<c>", lambda eff: button_click(eff,b10,10))
    window.bind("<v>", lambda eff: button_click(eff,b11,11))

    # GRID OUR BUTTONS

    b0.grid(row=2, column=0)
    b1.grid(row=2, column=1)
    b2.grid(row=2, column=2)
    b3.grid(row=2, column=3)

    b4.grid(row=3, column=0)
    b5.grid(row=3, column=1)
    b6.grid(row=3, column=2)
    b7.grid(row=3, column=3)

    b8.grid(row=4, column=0)
    b9.grid(row=4, column=1)
    b10.grid(row=4, column=2)
    b11.grid(row=4, column=3)

    # FUNCTION TO EXIT FROM GAME
    def exit_game(event):
        window.destroy()
    
    window.bind("<BackSpace>",reset)
    window.bind("<Escape>",exit_game)

    window.mainloop()

window1.bind("<Return>",game)
window1.bind("<Escape>",quit)

# DEFINING BUTTONS
button1 = Button(window1, text="PRESS ENTER TO START GAME", width=24, height=2, command=game)
button2 = Button(window1, text="PRESS ESC TO EXIT GAME", width=24, height=2, command=quit)

# DEFINING BUTTON CANVAS
button1_canvas = my_canvas.create_window(560, 500, anchor="nw", window=button1)
button2_canvas = my_canvas.create_window(790, 500, anchor="nw", window=button2)

window1.mainloop()
