from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="#2E1B47")  # Adjusted the background color slightly
root.resizable(False, False)

dark_mode = True

# Custom theme colors
themes = {
    "dark": {"bg": "#2E1B47", "fg": "white", "button_bg": "#800080", "msg_color": "#DDA0DD"},  # Purple tones
    "light": {"bg": "#A3C9FF", "fg": "#000080", "button_bg": "#87CEEB", "msg_color": "#4682B4"},  # Light blue tones
}

# Toggle theme function
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    theme = "dark" if dark_mode else "light"
    root.configure(background=themes[theme]["bg"])
    comp_label.configure(bg=themes[theme]["bg"])
    user_label.configure(bg=themes[theme]["bg"])
    playerScore.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    computerScore.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    user_indicator.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    comp_indicator.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    msg.configure(bg=themes[theme]["bg"], fg=themes[theme]["msg_color"])
    toggle_button.configure(bg=themes[theme]["button_bg"], fg=themes[theme]["fg"])

# Load images
rock_img = ImageTk.PhotoImage(Image.open("Images/rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("Images/paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("Images/scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("Images/rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("Images/paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("Images/scissors.png"))

# Create label for user and computer images
user_label = Label(root, image=scissor_img, bg="#2E1B47")
comp_label = Label(root, image=scissor_img_comp, bg="#2E1B47")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Score labels
playerScore = Label(root, text=0, font=100, bg="#2E1B47", fg="white")
computerScore = Label(root, text=0, font=100, bg="#2E1B47", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# Indicators for user and computer
user_indicator = Label(root, font=50, text="USER", bg="#2E1B47", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#2E1B47", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Message label
msg = Label(root, font=50, bg="#2E1B47", fg="white")
msg.grid(row=3, column=2)

# Reset game function
def reset_game():
    playerScore["text"] = "0"
    computerScore["text"] = "0"
    msg["text"] = ""
    user_label.configure(image=scissor_img)
    comp_label.configure(image=scissor_img_comp)

reset_button = Button(root, text="Restart Game", bg="#FF6347", fg="white", command=reset_game)
reset_button.grid(row=0, column=2, padx=10, pady=10)

# Update message label
def updateMessage(x):
    msg['text'] = x

# Update player score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# Update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# Check for winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose!")
            updateCompScore()
        else:
            updateMessage("You win!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lose!")
            updateCompScore()
        else:
            updateMessage("You win!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lose!")
            updateCompScore()
        else:
            updateMessage("You win!")
            updateUserScore()

# Update choices and display images
choices = ["rock", "paper", "scissor"]

def updateChoice(x):
    compChoice = choices[randint(0, 2)]
    
    # Update computer image based on choice
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # Update user image based on their choice
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)

# Buttons for user to make a choice
rock_button = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper_button = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor_button = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

# Theme toggle button
toggle_button = Button(root, text="Toggle Theme", bg=themes["dark"]["button_bg"], fg=themes["dark"]["fg"], command=toggle_theme)
toggle_button.grid(row=0, column=4, padx=10, pady=10)

root.mainloop()
