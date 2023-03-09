import tkinter
from tkinter import *
import main
"""Создает окно с 3мя полями ввода, кнопкой старт"""
def windows():
    """Создает окно с 3мя полями ввода, кнопкой старт"""
    def click_btn():
        """Записывает переменные старт диапозон, финиш, порт, передает в
        range_ip(start, finish, port):"""
        start_entry = start_e1.get()
        finish_entry = finish_e2.get()
        port_entry = port_e3.get()
        main.withe_lest(main.range_ip(start_entry, finish_entry, port_entry))

    top = Tk()
    top.resizable(False, False)
    top.title("ПарсерМаинкрафт_v1.0")
    photo = tkinter.PhotoImage(file="minecraft-logo-clipart-tnt-6.png")
    top.iconphoto(False, photo)
    top.geometry("300x200+800+200")
    st = Label(top, text="Старт")
    st.grid(row=1, column=0)
    fin = Label(top, text="Финиш")
    fin.grid(row=2, column=0)
    po = Label(top, text="Порт")
    po.grid(row=3, column=0)
    start_e1 = tkinter.Entry(top)
    start_e1.grid(row=1, column=1)
    finish_e2 = tkinter.Entry(top)
    finish_e2.grid(row=2, column=1)
    port_e3 = tkinter.Entry(top)
    port_e3.grid(row=3, column=1)
    btn1 = tkinter.Button(top, text="Start", command=click_btn)
    btn1.grid(row=4, column=1)
    top.grid_columnconfigure(0, minsize=100)
    top.mainloop()

"""запуск окна !!! КАКто криво"""
windows()


