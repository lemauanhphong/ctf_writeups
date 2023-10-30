import os
import json
import hashlib
import sys
import hmac
import base64
import string
import requests
from Crypto.Cipher import AES
from phpserialize import loads, dumps

#https://gist.github.com/bluetechy/5580fab27510906711a2775f3c4f5ce3

def mcrypt_decrypt(value, iv):
    global key
    AES.key_size = [len(key)]
    crypt_object = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
    return crypt_object.decrypt(value)


def mcrypt_encrypt(value, iv):
    global key
    AES.key_size = [len(key)]
    crypt_object = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
    return crypt_object.encrypt(value)


def decrypt(bstring):
    global key
    dic = json.loads(base64.b64decode(bstring).decode())
    mac = dic['mac']
    value = bytes(dic['value'], 'utf-8')
    iv = bytes(dic['iv'], 'utf-8')
    if mac == hmac.new(key, iv+value, hashlib.sha256).hexdigest():
        return mcrypt_decrypt(base64.b64decode(value), base64.b64decode(iv))
        #return loads(mcrypt_decrypt(base64.b64decode(value), base64.b64decode(iv))).decode()
    return ''


def encrypt(string):
    global key
    iv = os.urandom(16)
    #string = dumps(string)
    padding = 16 - len(string) % 16
    string += bytes(chr(padding) * padding, 'utf-8')
    value = base64.b64encode(mcrypt_encrypt(string, iv))
    iv = base64.b64encode(iv)
    mac = hmac.new(key, iv+value, hashlib.sha256).hexdigest()
    dic = {'iv': iv.decode(), 'value': value.decode(), 'mac': mac}
    return base64.b64encode(bytes(json.dumps(dic), 'utf-8'))

app_key ='xgH4wSfmT4d7pzQ+OcWRjRGUeIwKtSrk2BmpXXzLKd0='
key = base64.b64decode(app_key)
print(decrypt('eyJpdiI6IjRPbzV5eFhqTi9FdU5WbDQrN1FYbHc9PSIsInZhbHVlIjoiTlcxVHZMb2RKRlFPWElxNVU5Mk5NRVpxcExxaFhZcHdZVXd1cVFxaGRoY1kyMktDRzd0WFg2Y01VNUN2Z2R1Y0I4amtHbVJaelNERjJZbjJ3a1BtL2IwVjR3R2J2Z2xjVGF5TndVNUtoWVFaSjBRNkoxRjMrTVpSbmkwd2hxUFAiLCJtYWMiOiI5NjllNjI3NGEyYTY2OGMyNTdjMDYwYWE3Mzk2ZDg2NGU2YTMwYjMwNDE2ZThkMTM0ZGU4M2Y0YmY5MDgwMjlmIiwidGFnIjoiIn0='))
#b'{"data":"a:6:{s:6:\\"_token\\";s:40:\\"vYzY0IdalD2ZC7v9yopWlnnYnCB2NkCXPbzfQ3MV\\";s:8:\\"username\\";s:8:\\"guestc32\\";s:5:\\"order\\";s:2:\\"id\\";s:9:\\"direction\\";s:4:\\"desc\\";s:6:\\"_flash\\";a:2:{s:3:\\"old\\";a:0:{}s:3:\\"new\\";a:0:{}}s:9:\\"_previous\\";a:1:{s:3:\\"url\\";s:38:\\"http:\\/\\/206.189.25.23:31031\\/api\\/configs\\";}}","expires":9605140631}\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'
# print(encrypt(b'|hehe'))