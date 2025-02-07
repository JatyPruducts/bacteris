import socket
import time

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # настройка сокета
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # отключение пакетирования
main_socket.bind(("localhost", 10000))  # IP и привязка к порту
main_socket.setblocking(False)  # Непрерывность, не ждём ответа
main_socket.listen(5)  # Включение прослушивания, 5 - максимальное количество соединений
print("Сокет создался")

players = []
while True:
    try:
        new_socket, address = main_socket.accept()
        print(f"Соединение установлено с {address}")
        new_socket.setblocking(False)
        players.append(new_socket)

    except BlockingIOError:
        pass

    for sock in players:
        try:
            data = sock.recv(1024).decode()
            print(f"Получено сообщение: {data}")
        except:
            pass

    time.sleep(1)
