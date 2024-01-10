import pygame
from tkinter import *
#เพลงในเกม
pygame.mixer.init()
pygame.mixer.music.load('remixpa.wav')
pygame.mixer.music.play(-1)

def start_main_page(): #การเชื่อมต่อในโหมดต่างๆ
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from Options import Colour
            Colour.main()
        elif args == 2:
            from Options import Fruit
            Fruit.main()
        elif args == 3:
            from Options import Thaifood
            Thaifood.main()
        elif args == 4:
            from Options import Vehicles
            Vehicles.main()
            
    def option():

        lab_img1 = Button(
            main_window,
            text="Select",
            bg='#FFFDD0',
            border=0,
            justify='center',
            font=("Arial", 12)   
        )

        sel_btn1 = Button(
            text="สี",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#FFFDD0",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="ผลไม้",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#FFFDD0",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="อาหารไทย",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#FFFDD0",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="ชื่อคนในสภา",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#FFFDD0",
            cursor="hand2",
            command=lambda: start_game(4),
        )
        lab_img1.grid(row=0, column=0, padx=20)#ขนาดปุ่มและแถว
        sel_btn1.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=5, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()
    
    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("เกมทายคำศัพท์สุดแปลก")
    main_window.configure(background="#FCF4A3")

    img1 = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        text="เกมทายคำศัพท์สุดแปลก",
        bg='#FFFDD0',
        font=("Courier", 28)
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#FFFDD0",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50, 20))

    
    main_window.mainloop()
start_main_page()
