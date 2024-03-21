import socket
from logging import error
import argparse
from time import time

from termcolor import colored


def start_server(port: int, M: float):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("localhost", port))
    sock.listen(1)

    while True:
        client, addr = sock.accept()
        error(f"SERVER::Connection from {addr}")
        times = []
        start = time()
        while True:
            data = client.recv(1024)
            error(f"SERVER::recieved data {data}")
            end = time()
            times.append(end - start)
            start = end
            if not data:
                break
        print(f"{times=}")

        timelen = len(times)
        M = int("".join(str(int(x > M)) for x in times)[::-1], 2)
        msg = M.to_bytes((timelen + 7) // 8, "big")
        error(colored(f"Recovered message: {msg}", "green"))


M = 0.48871803283691406

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", help="server running port", type=int, required=True
    )
    args = parser.parse_args()

    start_server(args.port, M)
