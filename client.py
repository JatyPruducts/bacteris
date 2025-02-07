import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # настройка сокета
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # отключение пакетирования
sock.connect(("localhost", 10000))  # IP и привязка к порту

while True:
    sock.send("Привет".encode())

