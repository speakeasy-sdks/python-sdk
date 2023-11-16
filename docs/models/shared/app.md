# App


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `channel`                                                         | *str*                                                             | :heavy_check_mark:                                                | Specify the channel through which the payment must be processed.  |
| `phone`                                                           | *str*                                                             | :heavy_check_mark:                                                | Customer phone number associated with a wallet for payment.       |
| `provider`                                                        | [shared.Provider](../../models/shared/provider.md)                | :heavy_check_mark:                                                | Specify the provider through which the payment must be processed. |