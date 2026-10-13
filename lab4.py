class Product:
    """Товар з назвою та ціною."""

    def __init__(self, name, price):
        """Створює товар."""
        self.name = name
        self.price = price


class OrderItem:
    """Позиція замовлення: товар і його кількість."""

    def __init__(self, product, qty):
        """Створює позицію замовлення."""
        self.product = product
        self.qty = qty


class Order:
    """Замовлення, що містить товари та знижку."""

    def __init__(self, customer):
        """Створює порожнє замовлення."""
        self.customer = customer
        self._items = []
        self._discount = 0

    def add(self, product, qty=1) -> "Order":
        """Додає товар або збільшує його кількість, повертає замовлення."""
        for item in self._items:
            if item.product is product:
                item.qty += qty
                return self

        self._items.append(OrderItem(product, qty))
        return self

    def apply_discount(self, percent):
        """Встановлює знижку від 0 до 50 відсотків."""
        if not 0 <= percent <= 50:
            raise ValueError("знижка має бути від 0 до 50 %")
        self._discount = percent

    @property
    def total(self):
        """Повертає повну вартість із урахуванням знижки."""
        amount = sum(item.product.price * item.qty for item in self._items)
        return amount * (1 - self._discount / 100)

    def __len__(self):
        """Повертає загальну кількість одиниць товару."""
        return sum(item.qty for item in self._items)

    def __str__(self):
        """Повертає текстовий опис замовлення."""
        return f"Замовлення {self.customer}: {len(self)} од., {self.total:.2f} грн"


if __name__ == "__main__":
    bread = Product("хліб", 30)
    cheese = Product("сир", 120)

    o = (Order("Олена").add(bread, 2)
         .add(cheese).add(bread))

    print((len(o), o.total))
    o.apply_discount(10)
    print(o)

    try:
        o.apply_discount(70)
    except ValueError as error:
        print(type(error).__name__)
