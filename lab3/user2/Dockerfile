FROM python:buster
COPY server.py /server.py
COPY proxy.py /proxy.py
RUN python3 proxy.py --port 7777 --server-host localhost --server-port 8888 --message "Hid this, check out!" &
ENTRYPOINT ["python3", "server.py", "--port", "8888"]
