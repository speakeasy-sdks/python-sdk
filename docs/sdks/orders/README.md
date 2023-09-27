# Orders
(*orders*)

### Available Operations

* [create_order](#create_order) - Create Order
* [order_pay](#order_pay) - Order Pay

## create_order

Use this API to create orders with Cashfree from your backend and get the payment link. To use this API S2S flag needs to be enabled from the backend. In case you want to use the cards payment option the PCI DSS flag is required, for more information email us at "care@cashfree.com".

### Example Usage

```python
import pg
from pg.models import callbacks, operations, shared

s = pg.Pg()

req = operations.CreateOrderRequest(
    create_order_backend_request=shared.CreateOrderBackendRequest(
        customer_details=shared.CustomerDetails(
            customer_bank_account_number='quod',
            customer_bank_code='quod',
            customer_bank_ifsc='esse',
            customer_email='totam',
            customer_id='porro',
            customer_phone='dolorum',
        ),
        order_amount=10.15,
        order_currency='INR',
        order_expiry_time='2021-07-29T00:00:00Z',
        order_id='dicta',
        order_meta=shared.OrderMeta(
            notify_url='nam',
            payment_methods='officia',
            return_url='occaecati',
        ),
        order_note='Test order',
        order_splits=[
            shared.VendorSplit(
                amount=1433.53,
                percentage=5373.73,
                vendor_id='hic',
            ),
        ],
        order_tags={
            "optio": 'totam',
        },
        terminal=shared.TerminalDetails(
            terminal_id='beatae',
            terminal_phone_no='commodi',
            terminal_type='molestiae',
        ),
    ),
    x_api_version='modi',
    x_client_id='qui',
    x_client_secret='impedit',
)

res = s.orders.create_order(req)

if res.orders_entity is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateOrderRequest](../../models/operations/createorderrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**


## order_pay

Use this API when you have already created the orders and want Cashfree to process the payment. To use this API S2S flag needs to be enabled from the backend. In case you want to use the cards payment option the PCI DSS flag is required, for more information send an email to "care@cashfree.com".

### Example Usage

```python
import pg
from pg.models import operations, shared

s = pg.Pg()

req = operations.OrderPayRequest(
    order_pay_request=shared.OrderPayRequest(
        offer_id='faa6cc05-d1e2-401c-b0cf-0c9db3ff0f0b',
        payment_method=[],
        payment_session_id='session__CvcEmNKDkmERQrxnx39ibhJ3Ii034pjc8ZVxf3qcgEXCWlgDDlHRgz2XYZCqpajDQSXMMtCusPgOIxYP2LZx0-05p39gC2Vgmq1RAj--gcn',
        save_instrument=False,
    ),
    x_api_version='cum',
)

res = s.orders.order_pay(req)

if res.order_pay_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.OrderPayRequest](../../models/operations/orderpayrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.OrderPayResponse](../../models/operations/orderpayresponse.md)**

