import pyshark
import numpy as np
import matplotlib.pyplot as plt

def extract_packets(fname, dstport):
    cap = pyshark.FileCapture(fname)
    prev_time = None
    delays = []
    for packet in cap:
        if packet["tcp"].dstport != dstport:
            continue

        if prev_time is None:
            prev_time = packet.sniff_time.timestamp()
            continue

        time_delay = packet.sniff_time.timestamp() - prev_time
        prev_time = packet.sniff_time.timestamp()
        delays.append(time_delay)
    return delays

def plot(delays, fname):
    plt.clf()
    x = list(range(len(delays)))    
    y = delays

    plt.title("Delays")
    plt.ylabel("delay, s")
    plt.xlabel("packet num")

    plt.plot(x, y, color="skyblue")
    plt.savefig(fname)

delays8888 = extract_packets("dump1.pcapng", "8888")
delays7777 = extract_packets("dump1.pcapng", "7777")
plot(delays8888[:-1], "8888")
plot(delays7777[:-1], "7777")
