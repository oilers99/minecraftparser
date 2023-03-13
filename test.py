import visual
def test_entry(start_test, finish_test, port_test):
    """4"""
    """проверяет аргументы входа из visual click_btn
    1. Формат ввода
    2. Соответствие диапозону
    3. Ввод порта == цыфры
    Контрольное значение 11"""
    count = 0
    list_star = list(start_test.split("."))
    try:
        if start_test == (f"{(list_star[0]) }.{list_star[1]}.{list_star[2]}.{list_star[3]}"):
            count += 1
            for item in list_star:
                if int(item) in range(0, 256):
                    count += 1
        finish_list = list(finish_test.split("."))
        if finish_test == (f"{(finish_list[0]) }.{finish_list[1]}.{finish_list[2]}.{finish_list[3]}"):
            count += 1
            for item in finish_list:
                if int(item) in range(0, 256):
                    count += 1
            if port_test.isdigit() == True:
                count += 1
    except Exception:
        count = 1
    visual.check_test(check=count, start_ip_ch=start_test, finish_ip_ch=finish_test, port_ch=port_test)

