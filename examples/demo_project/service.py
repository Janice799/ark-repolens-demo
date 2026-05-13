from dataclasses import dataclass


@dataclass(frozen=True)
class CartItem:
    name: str
    price: float
    quantity: int = 1


def checkout_total(items: list[CartItem], tax_rate: float = 0.0) -> float:
    subtotal = sum(item.price * item.quantity for item in items)
    return round(subtotal * (1 + tax_rate), 2)


def refund_label(order_id: str) -> str:
    return f"refund-request:{order_id}"
