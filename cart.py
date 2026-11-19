def cart_total(prices, discount=0):
    """Повертає вартість кошика з урахуванням знижки у відсотках.

    prices -- список цін товарів (числа >= 0)
    discount -- знижка у відсотках, 0..100
    """
    if not 0 <= discount <= 100:
        raise ValueError("Знижка має бути в межах від 0 до 100")
    total = 0
    for price in prices:
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise ValueError("Ціна має бути числом")
        if price < 0:
            raise ValueError("Ціна не може бути від’ємною")
        total += price
    return round(total * (100 - discount) / 100, 2)
