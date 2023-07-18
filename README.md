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
                amount=3843.82,
                percentage=4375.87,
                vendor_id='magnam',
            ),
            shared.VendorSplit(
                amount=8917.73,
                percentage=567.13,
                vendor_id='delectus',
            ),
            shared.VendorSplit(
                amount=2726.56,
                percentage=3834.41,
                vendor_id='molestiae',
            ),
        ],
        order_tags={
            "placeat": 'voluptatum',
            "iusto": 'excepturi',
            "nisi": 'recusandae',
            "temporibus": 'ab',
        },
        terminal=shared.TerminalDetails(
            terminal_id='quis',
            terminal_phone_no='veritatis',
            terminal_type='deserunt',
        ),
    ),
    x_api_version='perferendis',
    x_client_id='ipsam',
    x_client_secret='repellendus',
)

res = s.orders.create_order(req)

if res.orders_entity is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [orders](docs/sdks/orders/README.md)

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
