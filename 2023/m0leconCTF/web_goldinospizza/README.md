# goldinospizza

In this challenge we need to focus on 
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

Buy the first item (flag) and modify `item["quantity"]` to `-1`.
```py
current_user.balance -= product.price * quantity 
=> current_user.balance -= product.price * (-1)
=> current_user.balance += product.price
```

Then we have enough amount of money to buy the flag.