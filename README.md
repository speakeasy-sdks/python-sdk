# PG

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/python-sdk.git
```
<!-- End SDK Installation -->

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [Orders](docs/sdks/orders/README.md)

* [create_order](docs/sdks/orders/README.md#create_order) - Create Order
* [order_pay](docs/sdks/orders/README.md#order_pay) - Order Pay
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
