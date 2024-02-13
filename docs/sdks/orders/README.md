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
from pg.models import operations

s = pg.Pg()

req = operations.CreateOrderRequest(
    x_client_id='string',
    x_client_secret='string',
)

res = s.orders.create_order(req)

if res.orders_entity is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateOrderRequest](../../models/operations/createorderrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateOrderResponse](../../models/operations/createorderresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.AuthenticationError | 401                        | application/json           |
| errors.RateLimitError      | 429                        | application/json           |
| errors.APIError            | 500                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## order_pay

Use this API when you have already created the orders and want Cashfree to process the payment. To use this API S2S flag needs to be enabled from the backend. In case you want to use the cards payment option the PCI DSS flag is required, for more information send an email to "care@cashfree.com".

### Example Usage

```python
import pg
from pg.models import operations

s = pg.Pg()

req = operations.OrderPayRequest(
    x_api_version='string',
)

res = s.orders.order_pay(req)

if res.order_pay_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.OrderPayRequest](../../models/operations/orderpayrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.OrderPayResponse](../../models/operations/orderpayresponse.md)**
### Errors

| Error Object          | Status Code           | Content Type          |
| --------------------- | --------------------- | --------------------- |
| errors.RateLimitError | 429                   | application/json      |
| errors.APIError       | 500                   | application/json      |
| errors.SDKError       | 4x-5xx                | */*                   |
