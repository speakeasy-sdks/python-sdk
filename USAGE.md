<!-- Start SDK Example Usage -->


```python
import pg
from pg.models import callbacks, operations, shared

s = pg.Pg()

req = operations.CreateOrderRequest(
    create_order_backend_request=shared.CreateOrderBackendRequest(
        customer_details=shared.CustomerDetails(
            customer_bank_account_number='North double',
            customer_bank_code='spherical woman burdensome',
            customer_bank_ifsc='interfaces Smart',
            customer_email='Doyle brown toast',
            customer_id='Bedfordshire',
            customer_phone='Mohr North',
        ),
        order_amount=10.15,
        order_currency='INR',
        order_expiry_time='2021-07-29T00:00:00Z',
        order_id='deploy South',
        order_meta=shared.OrderMeta(
            notify_url='Road male Berkshire',
            payment_methods='parsing female middleware',
            return_url='Bedfordshire navigating',
        ),
        order_note='Test order',
        order_splits=[
            shared.VendorSplit(
                amount=5942.72,
                percentage=3302.96,
                vendor_id='dearly remount',
            ),
        ],
        order_tags={
            "expedita": 'South',
        },
        terminal=shared.TerminalDetails(
            terminal_id='Southwest',
            terminal_phone_no='violet Chips Porsche',
            terminal_type='mobile',
        ),
    ),
    x_api_version='ROI bypassing vero',
    x_client_id='Solutions Ferrari Accountability',
    x_client_secret='Folk ampere',
)

res = s.orders.create_order(req)

if res.orders_entity is not None:
    # handle response
```
<!-- End SDK Example Usage -->