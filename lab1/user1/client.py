import argparse
import socket
from os import urandom
from random import randint, random
from time import sleep


def model_packets(host, port, n_packets=200):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    sent = 0
    while sent < n_packets:
        data = urandom(randint(1, 100))
        data = len(data).to_bytes(4, "big") + data
        client.send(data)

        sent += 1
        sleep(random())
    client.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--port", help="server running port", type=int, required=True
    )
    parser.add_argument("--host", help="server running host", type=str, required=True)
    args = parser.parse_args()

    model_packets(args.host, args.port)
