import socket

from logging import error
import argparse

from time import sleep
from random import random, randint
from os import urandom

from queue import Queue
from threading import Thread

from termcolor import colored

# from concurrent.futures import ThreadPoolExecutor

M = 0.48871803283691406


def start_proxy(port: int, server_host: str, server_port: int, message: str):
    q = Queue()
    msg = int.from_bytes(message.encode(), "big")
    finished = False

    def listen_and_buffer(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("localhost", port))
        sock.listen(1)

        client, addr = sock.accept()
        error(colored(f"PROXY::Connection from {addr}", "red"))

        while True:
            data = client.recv(1024)
            error(colored(f"PROXY::Received data {data}", "red"))
            q.put(data)
            if not data:
                break
        client.close()

    def be_proxy_and_send_message(host: str, port: port, msg):
        data = b""
        delay = 0.0
        started = False
        server = None
        finished = False
        while msg or not finished:
            delay = 0.0
            if msg and started:
                if msg & 1:
                    delay = 0.1 * random() + 0.2 + M
                else:
                    delay = random() * 0.9 * M
                msg >>= 1

                if q.empty():
                    data = urandom(randint(1, 10))
                    data = len(data).to_bytes(4, "big") + data
                    error(colored(f"PROXY::sending data {data}", "green"))
                else:
                    data = q.get()
                    if data == b'':
                        finished = True
                    error(colored(f"PROXY::sending data {data}", "yellow"))

                sleep(delay)
                server.send(data)
            elif not q.empty():
                if started:
                    data = q.get()
                    error(colored(f"PROXY::sending data {data}", "yellow"))
                    if data == b'':
                        finished = True
 
                    server.send(data)
                else:
                    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    error(colored(f"PROXY::trying {host}:{port}", "blue"))
                    server.connect((host, port))

                    started = True

        server.close()

    finished = False
    receive = Thread(target=listen_and_buffer, args=(port,))
    receive.start()
    send = Thread(
        target=be_proxy_and_send_message, args=(server_host, server_port, msg)
    )
    send.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", help="proxy running port", type=int, required=True
    )
    parser.add_argument(
        "--server-port", help="server running port", type=int, required=True
    )
    parser.add_argument(
        "--server-host", help="server running host", type=str, required=True
    )
    parser.add_argument(
        "-m", "--message", help="secret message", type=str, required=True
    )
    args = parser.parse_args()

    start_proxy(args.port, args.server_host, args.server_port, args.message)
