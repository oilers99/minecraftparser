def range_ip (start, finish):
    """Принимает старт диапозона и финиш. Генерирует  все IP в диапозоне. Создает и Записывает
    их в Файл.тхт (про запись в фаил временное решение"""
    from netaddr import iter_iprange
    generator = iter_iprange(start, finish, step=1)
    my_file = open('output.txt', 'w')
    for ipa in generator:
        my_file.write(str(ipa))
        my_file.write("\n")
    my_file.close()




def port_open():
    """Считывает построчно из файла IP проверяет на открытый порт. Возврат файл с IP
    адресами открытых портов"""



def parser(ip_port):
    """Принимет IP с открытым портом проверяет на наличие сервера """
    pass

def withe_lest(server_ip):
    """Принимает сервера с IP и портами проверяет конфиг на ВайтЛист, записывает
    в файл с указанием версии"""
    pass
range_ip('5.8.62.0', '5.8.62.255')
