import pyshark

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

bs = [1.5, 0.75, 1.25, 1.5, 0.8, 1, 1.15, 0.75, 0.75, 1.25, 1.25, 0.75]
for i in range(1, 13):
    delays = extract_packets(f"{i}.pcapng", 99)
    res = ""
    for d in delays:
        if d < bs[i-1]:
            res += "0"
        else:
            res += "1"

    try:
        t = int(res, 2).to_bytes((len(res) + 7) // 8, 'big')
        print(t.decode("utf-8"))
    except:
        pass

    try:
        t = int(res[::-1], 2).to_bytes((len(res) + 7) // 8, 'big')
        print(t.decode("utf-8"))
    except:
        pass
