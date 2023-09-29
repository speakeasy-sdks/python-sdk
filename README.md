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

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [orders](docs/sdks/orders/README.md)

* [create_order](docs/sdks/orders/README.md#create_order) - Create Order
* [order_pay](docs/sdks/orders/README.md#order_pay) - Order Pay
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
