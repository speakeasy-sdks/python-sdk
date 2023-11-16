# PG

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/python-sdk.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
### Example

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



<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.AuthenticationError | 401                        | application/json           |
| errors.RateLimitError      | 429                        | application/json           |
| errors.APIError            | 500                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

### Example

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

res = None
try:
    res = s.orders.create_order(req)
except (errors.AuthenticationError) as e:
    print(e) # handle exception
except (errors.RateLimitError) as e:
    print(e) # handle exception

except (errors.APIError) as e:
    print(e) # handle exception
except (errors.SDKError) as e:
    print(e) # handle exception


if res.orders_entity is not None:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://sandbox.cashfree.com/pg` | None |
| 1 | `https://api.cashfree.com/pg` | None |

#### Example

```python
import pg
from pg.models import callbacks, operations, shared

s = pg.Pg(
    server_idx=1,
)

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


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import pg
from pg.models import callbacks, operations, shared

s = pg.Pg(
    server_url="https://sandbox.cashfree.com/pg",
)

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
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import pg
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = pg.Pg(client: http_client)
```
<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
