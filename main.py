def range_ip(start, finish, port):
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
    return ip_port


def withe_lest(server_work):
    """Принимает переменную со списком IP и портами перебирает их
    записывает в файл с указанием версии"""
    from mcstatus import JavaServer
    z = []
    for i in server_work:
        try:
            server = JavaServer.lookup(i)
            status = server.status()
            if server.ping() > 1:
                print(i, status.version.name)
                z.append(i + " " + status.version.name)
        except Exception:
            print(i, "No")
    print(z)



withe_lest(range_ip('79.175.1.0', '79.175.3.255', "25565"))
