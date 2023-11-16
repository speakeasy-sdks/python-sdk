<!-- Start SDK Example Usage -->
```python
import pg
from pg.models import callbacks, operations, shared

s = pg.Pg()

req = operations.CreateOrderRequest(
    create_order_backend_request=shared.CreateOrderBackendRequest(
        customer_details=shared.CustomerDetails(
            customer_id='string',
            customer_phone='string',
        ),
        order_amount=10.15,
        order_currency='INR',
        order_expiry_time='2021-07-29T00:00:00Z',
        order_meta=shared.OrderMeta(),
        order_note='Test order',
        order_splits=[
            shared.VendorSplit(),
        ],
        order_tags={
            "key": 'string',
        },
        terminal=shared.TerminalDetails(
            terminal_id='string',
            terminal_phone_no='string',
            terminal_type='string',
        ),
    ),
    x_client_id='string',
    x_client_secret='string',
)

res = s.orders.create_order(req)

if res.orders_entity is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->