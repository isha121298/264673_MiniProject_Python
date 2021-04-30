from tkinter import *
import random 
from tkinter import messagebox
import time

with open("C://Users/HP/Desktop/Mini Project Python/264673_MiniProject_Python/files_extra//animals_word.txt", "r") as ANIMALS_WORD:
    word=list(ANIMALS_WORD.readline().split(","))

with open("C://Users/HP/Desktop/Mini Project Python/264673_MiniProject_Python/files_extra//animals_answer.txt", "r") as ANIMALS_ANSWER:
    ans=ANIMALS_ANSWER.readline().split(",")



ran_num = random.randrange(0, (len(word)))
jumbled_rand_word = word[ran_num]
points = 0


def main():
    def back():
        my_window.destroy()
        import main1
        main1.start_main_page()

    def change():
        global ran_num
        ran_num = random.randrange(0, (len(word)))
        word1.configure(text=word[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == ans[ran_num]:
            points += 5
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = random.randrange(0, (len(word)))
            word1.configure(text=word[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=ans[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("700x700+500+150")
    my_window.resizable(0, 0)
    my_window.title("Guest the Word Game")
    my_window.configure(background="#e6fff5")
    img1 = PhotoImage(file="C://Users/HP/Desktop/Mini Project Python/264673_MiniProject_Python/backarrow.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#e6fff5',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score:- 0",
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word1 = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  50 bold"
    )
    word1.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=change,
    )
    change.pack()

    ans1 = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=show_answer,
    )
    ans1.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#e6fff5",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
