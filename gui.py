import tkinter as tk
from main import SnakeWaterGun
import winsound   # Windows sound

game = SnakeWaterGun()
round_no = 1

def play_sound(result):
    try:
        if result == "You Win":
            winsound.PlaySound("win.wav", winsound.SND_ASYNC)
        elif result == "You Lose":
            winsound.PlaySound("lose.wav", winsound.SND_ASYNC)
        else:
            winsound.PlaySound("win.wav", winsound.SND_ASYNC)
    except:
        pass

def play(choice):
    global round_no

    data = game.play_round(choice)

    result_label.config(
        text=f"You: {data['user_choice']}\n"
             f"Computer: {data['computer_choice']}\n"
             f"Result: {data['result']}"
    )

    score_label.config(
        text=f"Score → You: {data['user_score']} | Computer: {data['computer_score']}"
    )

    history_box.insert(
        tk.END,
        f"Round {round_no}: You({data['user_choice']}) | "
        f"Computer({data['computer_choice']}) → {data['result']}\n"
    )
    history_box.see(tk.END)

    play_sound(data["result"])
    round_no += 1

def reset_game():
    global round_no
    game.reset_game()
    round_no = 1

    score_label.config(text="Score → You: 0 | Computer: 0")
    result_label.config(text="")
    history_box.delete("1.0", tk.END)

# ---------------- GUI SETUP ---------------- #

root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("500x450")
root.resizable(False, False)

tk.Label(
    root,
    text="🐍 Snake Water Gun 🔫",
    font=("Arial", 16, "bold")
).pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Snake 🐍", width=10, command=lambda: play(1)).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Water 💧", width=10, command=lambda: play(-1)).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Gun 🔫", width=10, command=lambda: play(0)).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(
    root,
    text="Score → You: 0 | Computer: 0",
    font=("Arial", 12, "bold")
)
score_label.pack(pady=5)

# 🔁 Reset Button
tk.Button(
    root,
    text="🔄 Reset Game",
    font=("Arial", 11),
    command=reset_game
).pack(pady=8)

# 📜 Round History
tk.Label(root, text="Round History", font=("Arial", 12, "bold")).pack()

history_box = tk.Text(root, height=8, width=55)
history_box.pack(pady=5)

root.mainloop()
