# ARK RepoLens Demo Transcript

## Demo Command

```bash
localengine index examples/demo_project
localengine report
localengine doctor
localengine ask "Where is checkout_total implemented?"
```

## Index Result

```text
Project: examples/demo_project
Files indexed: 3
Chunks indexed: 3
Possible secrets redacted: 0
Top paths: README.md, policy.md, service.py
```

## Readiness Check

```text
[OK] Model config: Loaded default config path.
[OK] License policy: Loaded default config path.
[OK] Retrieval index: 3 chunks from 3 files; 0 possible secrets redacted.
```

## Assistant Answer

```text
Retrieved local project context for the prompt:
Where is checkout_total implemented?

[service.py:1-17]
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

[README.md:1-12]
# Demo Project

Tiny project for checking ARK RepoLens retrieval before indexing a real
customer repository.

Try:

localengine index examples/demo_project
localengine report
localengine ask "Where is checkout_total implemented?"

Next step: connect this grounded context to the approved local model runtime or
adapter training path for customer-specific generation.
```

## Citations

- service.py:1-17
- README.md:1-12

## Review Policy

Generated or retrieved coding output requires human review before production
use.

## Demo Status

PASS
