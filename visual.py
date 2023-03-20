import tkinter
from tkinter import *
import main
import test

def windows():
    """2"""
    """Создает окно с 3мя полями ввода, кнопкой старт"""
    def click_btn():
        """3"""
        """Записывает переменные старт диапозон, финиш, порт, передает в
        test test_entry"""
        start_entry = start_e1.get()
        finish_entry = finish_e2.get()
        port_entry = port_e3.get()
        test.test_entry(start_test=start_entry, finish_test=finish_entry, port_test=port_entry)

    """Основное окно"""
    top = Tk()
    top.resizable(False, False)
    top.title("ПарсерМаинкрафт_v1.3")
    photo = tkinter.PhotoImage(file="minecraft-logo-clipart-tnt-6.png")
    top.iconphoto(False, photo)
    top.geometry("400x200+800+200")
    """отображение Lebel при запуске"""
    st = Label(top, text="Старт")
    st.grid(row=1, column=0)
    fin = Label(top, text="Финиш")
    fin.grid(row=2, column=0)
    po = Label(top, text="Порт")
    po.grid(row=3, column=0)
    """Поле ввода"""
    start_e1 = tkinter.Entry(top)
    start_e1.grid(row=1, column=1)
    finish_e2 = tkinter.Entry(top)
    finish_e2.grid(row=2, column=1)
    port_e3 = tkinter.Entry(top)
    port_e3.grid(row=3, column=1)
    """отображение Label помошь"""
    leb1 = tkinter.Label(top, text="123.123.123.123")
    leb1.grid(row=1, column=3)
    leb2 = tkinter.Label(top, text="222.222.222.222")
    leb2.grid(row=2, column=3)
    leb3 = tkinter.Label(top, text="DEFAULT 25565")
    leb3.grid(row=3, column=3)
    """Кнопка"""
    btn1 = tkinter.Button(top, text="Start", command=click_btn)
    btn1.grid(row=4, column=1)
    """Размеры колонок"""
    top.grid_columnconfigure(0, minsize=100)
    top.grid_columnconfigure(1, minsize=150)
    top.grid_columnconfigure(3, minsize=140)
    """Отображение"""
    top.mainloop()
def check_test(start_ip_ch, finish_ip_ch, port_ch, check):
    """5"""
    """Принимает значение из test test_entry, проверяет порамтр check
    if передает в main range_ip
    else сообшение ошибка"""
    if check == 11:
        main.range_ip(start_ip_ch, finish_ip_ch, port_ch)
    else:
        fail = tkinter.Label(text="НЕВЕРНЫЙ ВВОД\nincorrect data entry", foreground="red")
        fail.grid(row=5, column=1)
        pass

