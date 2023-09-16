# Orders

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
            customer_bank_account_number='placeat',
            customer_bank_code='voluptatum',
            customer_bank_ifsc='iusto',
            customer_email='excepturi',
            customer_id='nisi',
            customer_phone='recusandae',
        ),
        order_amount=10.15,
        order_currency='INR',
        order_expiry_time='2021-07-29T00:00:00Z',
        order_id='temporibus',
        order_meta=shared.OrderMeta(
            notify_url='ab',
            payment_methods='quis',
            return_url='veritatis',
        ),
        order_note='Test order',
        order_splits=[
            shared.VendorSplit(
                amount=6481.72,
                percentage=202.18,
                vendor_id='ipsam',
            ),
        ],
        order_tags={
            "repellendus": 'sapiente',
        },
        terminal=shared.TerminalDetails(
            terminal_id='quo',
            terminal_phone_no='odit',
            terminal_type='at',
        ),
    ),
    x_api_version='at',
    x_client_id='maiores',
    x_client_secret='molestiae',
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
        payment_method=shared.CardlessEMIPaymentMethod(
            cardless_emi=shared.CardlessEMI(
                channel='quod',
                emi_tenure=461479,
                phone='861-765-1597 x5144',
                provider=shared.CardlessEMIProvider.ZESTMONEY,
            ),
        ),
        payment_session_id='session__CvcEmNKDkmERQrxnx39ibhJ3Ii034pjc8ZVxf3qcgEXCWlgDDlHRgz2XYZCqpajDQSXMMtCusPgOIxYP2LZx0-05p39gC2Vgmq1RAj--gcn',
        save_instrument=False,
    ),
    x_api_version='qui',
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

