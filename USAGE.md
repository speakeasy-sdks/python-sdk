<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->