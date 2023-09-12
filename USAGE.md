<!-- Start SDK Example Usage -->


```python
import pg
from pg.models import callbacks, operations, shared

s = pg.Pg()

req = operations.CreateOrderRequest(
    create_order_backend_request=shared.CreateOrderBackendRequest(
        customer_details=shared.CustomerDetails(
            customer_bank_account_number='corrupti',
            customer_bank_code='provident',
            customer_bank_ifsc='distinctio',
            customer_email='quibusdam',
            customer_id='unde',
            customer_phone='nulla',
        ),
        order_amount=10.15,
        order_currency='INR',
        order_expiry_time='2021-07-29T00:00:00Z',
        order_id='corrupti',
        order_meta=shared.OrderMeta(
            notify_url='illum',
            payment_methods='vel',
            return_url='error',
        ),
        order_note='Test order',
        order_splits=[
            shared.VendorSplit(
                amount=6458.94,
                percentage=3843.82,
                vendor_id='iure',
            ),
        ],
        order_tags={
            "magnam": 'debitis',
        },
        terminal=shared.TerminalDetails(
            terminal_id='ipsa',
            terminal_phone_no='delectus',
            terminal_type='tempora',
        ),
    ),
    x_api_version='suscipit',
    x_client_id='molestiae',
    x_client_secret='minus',
)

res = s.orders.create_order(req)

if res.orders_entity is not None:
    # handle response
```
<!-- End SDK Example Usage -->