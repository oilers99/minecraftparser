import visual

def range_ip(start, finish, port):
    """6"""
    """Принимает старт диапозона и финиш. Генерирует  все IP в диапозоне
    добавляет порт"""
    import ipaddress
    range_ipa = []
    start_ip = ipaddress.IPv4Address(start)
    end_ip = ipaddress.IPv4Address(finish)
    for ip_int in range(int(start_ip), int(end_ip)):
        range_ipa.append(str(ipaddress.IPv4Address(ip_int)))
    ip_port = []
    for ip in range_ipa:
        ip_port.append(ip + ":" + port)
    withe_lest(ip_port)

def withe_lest(server_work):
    """7"""
    """Принимает переменную со списком IP и портами перебирает их
    записывает в файл с указанием версии"""
    from mcstatus import JavaServer
    my_file = open("output.txt", "a")
    finale = []
    for i in server_work:
        try:
            server = JavaServer.lookup(i)
            status = server.status()
            if server.ping() > 1:
                # print(i, status.version.name)
                finale.append(i + " " + status.version.name)
                my_file.writelines(finale)
                my_file.writelines("\n")
        except Exception:
            None
            # print("no")
    my_file.close()

"""запуск визула !!!! както криво"""
"""1"""
visual


