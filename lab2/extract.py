import pyshark
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

def hist1(data, xl, yl, title):
    plt.clf()
    n, _, _ plt.hist(data, bins=30, color="skyblue", alpha=0.7, edgecolor="black")

    return n


def hist(data, xl, yl, title):
    plt.clf()
    sns.histplot(data, bins=30, kde=True, color="skyblue", alpha=0.7, edgecolor="black")

    plt.grid(axis="y", alpha=0.75)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(title)

    maxfreq = n.max()
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.xlim(xmax=max(data) + 0.5)
    plt.savefig(title)


def extract_packets(fname, start=0):
    cap = pyshark.FileCapture(fname)
    prev_time = None
    delays = []
    i = 0
    for packet in cap:
        if prev_time is None:
            prev_time = packet.sniff_time.timestamp()
            continue

        time_delay = packet.sniff_time.timestamp() - prev_time
        prev_time = packet.sniff_time.timestamp()
        if i >= start:
            delays.append(time_delay)
        i += 1
    cap.close()
    return delays


#print("1")
#for i in range(1, 13):
#    delays = extract_packets(f"{i}.pcapng")
#    n, ints = np.histogram(delays, bins=30)
#    avg = sum(delays) / len(delays)
#
#    max_delay = max(delays)
#    avg_C = (
#        sum(n[i] * (ints[i + 1] - ints[i]) for i in range(len(ints) - 1)) / max_delay
#    )
#
#    hist(delays, "delay", "freq", f"task1/{i}")
#    max_C = max(n)
#    print(f"{avg_C, max_C = }")
#    print(f"P_{i} = {1 - avg_C / max_C}")
#print()
print("2")
for i in range(1, 13):
    delays = extract_packets(f"{i}.pcapng", 99)
    n, ints = np.histogram(delays[99:], bins=30)
    print(n)
    exit()
    avg = sum(delays) / len(delays)

    max_delay = max(delays)
    #avg_C = (
    #    sum(n[i] * (ints[i + 1] - ints[i]) for i in range(len(ints) - 1)) / max_delay
    #)
    avg_C = avg

    hist(delays, "delay", "freq", f"task2/{i}")
    max_C = max(n)
    print(f"{avg_C, max_C = }")
    print(f"P_{i} = {1 - avg_C / max_C}")
print()
