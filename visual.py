from tkinter import *
def windows():
    """Создает окно с 3мя полями ввода, кнопкой старт"""
    top = Tk()
    top.resizable(False, False)
    top.title("ПарсерМаинкрафт")
    top.geometry("300x200")
    start = Label(top, text="Старт").place(x=30, y=30)
    finish = Label(top, text="Финиш").place(x=30, y=70)
    port = Label(top, text="Порт").place(x=30, y=110)
    strrt_e1 = Entry(top).place(x=100, y=30)
    finish_e2 = Entry(top).place(x=100, y=70)
    port_e3 = Entry(top).place(x=100, y=110)
    top.mainloop()

windows()