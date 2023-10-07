<!-- Start SDK Example Usage -->


```python
import pg
from pg.models import callbacks, operations, shared

s = pg.Pg()

req = operations.CreateOrderRequest(
    create_order_backend_request=shared.CreateOrderBackendRequest(
        customer_details=shared.CustomerDetails(
            customer_id='North double',
            customer_phone='spherical woman burdensome',
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
            "temporibus": 'SUV',
        },
        terminal=shared.TerminalDetails(
            terminal_id='overriding',
            terminal_phone_no='Southeast Southwest but',
            terminal_type='Recycled',
        ),
    ),
    x_client_id='Orchestrator',
    x_client_secret='implement',
)

res = s.orders.create_order(req)

if res.orders_entity is not None:
    # handle response
```
<!-- End SDK Example Usage -->