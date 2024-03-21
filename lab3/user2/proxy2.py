import socket

from logging import error
import argparse

from time import sleep, time
from random import random, randint
from os import urandom

from queue import Queue
from threading import Thread

from termcolor import colored

# from concurrent.futures import ThreadPoolExecutor

M = 1.0


def start_proxy(port: int, server_host: str, server_port: int, mode: bool):
    q = Queue()

    def listen_and_buffer(port):
        error(colored(f"PROXY::binding to localhost:{port}", "red"))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("localhost", port))
        sock.listen(1)

        client, addr = sock.accept()
        error(colored(f"PROXY::Connection from {addr}", "red"))

        start = None
        while True:
            data = client.recv(1024)
            end = time()
            if start is None:
                data = (data, 0.0)
            else:
                data = (data, end - start)
                end = start

            error(colored(f"PROXY::Received data {data}", "red"))
            q.put(data)
            if not data[0]:
                break
        client.close()

    receive = Thread(target=listen_and_buffer, args=(port,))
    receive.start()

    if mode:
        while True:
            if not q.empty():
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                error(colored(f"PROXY::trying {server_host}:{server_port}", "blue"))
                server.connect((server_host, server_port))

                while True:
                    if q.empty():
                        continue

                    data, delay = q.get()
                    if data == b"":
                        break

                    sleep(M - delay)
                    error(colored(f"PROXY::sending data {data}", "green"))
                    server.send(data)

                server.close()
    else:
        while True:
            if not q.empty():
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                error(colored(f"PROXY::trying {server_host}:{port}", "blue"))
                server.connect((server_host, server_port))

                while True:
                    if q.empty():
                        continue
                    data, _ = q.get()

                    if data == b"":
                        break

                    error(colored(f"PROXY::sending data {data}", "green"))
                    server.send(data)
                    if random() < 0.2:
                        data = urandom(randint(1, 10))
                        data = len(data).to_bytes(4, "big") + data

                        sleep(random())
                        error(colored(f"PROXY::sending data {data}", "white"))
                        server.send(data)

                server.close()


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
    parser.add_argument("-m", "--mode", help="mode", type=int, required=True)
    args = parser.parse_args()

    start_proxy(args.port, args.server_host, args.server_port, args.mode)
