from tkinter import *


def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from files_extra import animals
            animals.main()
        elif args == 2:
            from file1 import colours
            colours.main()
        elif args == 3:
            from file1 import shapes
            shapes.main()
    def option():

        lab_img1 = Button(main_window,text="Select",bg='#e6fff5',border=0,justify='center',font=("Arial", 12))
        sel_btn1 = Button(text="Animals",width=18,borderwidth=8,font=("", 18),fg="#000000",bg="#99ffd6",cursor="hand2",command=lambda: start_game(1))
        sel_btn2 = Button(text="Colour",width=18,borderwidth=8,font=("", 18),fg="#000000",bg="#99ffd6",cursor="hand2",command=lambda: start_game(2))
        sel_btn3 = Button(text="Shapes",width=18,borderwidth=8,font=("", 18),fg="#000000",bg="#99ffd6",cursor="hand2",command=lambda: start_game(3))
        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("Guess the Word")
    main_window.configure(background="#e6fff5")
    

    img1 = PhotoImage(file="")

    lab_img = Label(
        main_window,
        text="Guess the Word Game",
        bg='#e6fff5',
        font=("Courier", 28)
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(main_window,text="Start",width=18,borderwidth=8,fg="#000000",bg="#99ffd6",font=("", 13),cursor="hand2",command=show_option)
    start_btn.pack(pady=(50, 20))
    main_window.mainloop()


start_main_page()
