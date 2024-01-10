from tkinter import *
from random import *
from tkinter import messagebox
import time
from csv import *

สี_WORD = ['สดีแง', 'หลีอืงเส', 'สีง้ำเนิน', 'ขียวเส', 'ม้สีส', 'ส่งมีว', 'ต้ำสาลตี', 'พีชูสม', 'ทีอสง',
           'งีเสิน','สำดี', 'ขสาวี', ]

สี_ANSWER = ['สีแดง', 'สีเหลือง', 'สีน้ำเงิน', 'สีเขียว', 'สีส้ม', 'สีม่วง', 'สีน้ำตาล', 'สีชมพู', 'สีทอง',
             'สีเงิน', 'สีดำ', 'สีขาว', ]

ran_num = randrange(0, (len(สี_WORD)))
jumbled_rand_word = สี_WORD[ran_num]
try:
    score=[]
    with open("score.csv",'r')as f:
        for i in f:
            score.append(int(i))
    points = score[0]
except:
    points = 0


def main():
    def back():
        my_window.destroy()
        import index
        index.start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(สี_WORD)))
        word.configure(text=สี_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")
    def save():
        with open("score.csv","w")as f:
                f.write(str(points) +'\n')
    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == สี_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(สี_WORD)))
            word.configure(text=สี_WORD[ran_num])
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
            ans_lab.configure(text=สี_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("เกมทายคำศัพท์สุดแปลก")
    my_window.configure(background="#e6fff5")
    img1 = PhotoImage(file="back.png")

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
        text="Score: ",
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  30 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="ตกลง",
        width=15,
        borderwidth=5,
        font=("", 12),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="ข้าม",
        width=15,
        borderwidth=5,
        fg="#000000",
        bg="#99ffd6",
        font=("", 12),
        command=change,
    )
    change.pack()

    ans = Button(
        text="เฉลย",
        width=15,
        borderwidth=5,
        fg="#000000",
        bg="#99ffd6",
        font=("", 12),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))
    ans = Button(
        text="บันทึก",
        width=15,
        borderwidth=5,
        fg="#000000",
        bg="#99ffd6",
        font=("", 12),
        command=save,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#e6fff5",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()
    my_window.mainloop()
