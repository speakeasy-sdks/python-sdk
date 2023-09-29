# App


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `channel`                                                              | *Optional[str]*                                                        | :heavy_check_mark:                                                     | Specify the channel through which the payment must be processed.       |
| `phone`                                                                | *Optional[str]*                                                        | :heavy_check_mark:                                                     | Customer phone number associated with a wallet for payment.            |
| `provider`                                                             | [Optional[shared.AppProvider]](undefined/models/shared/appprovider.md) | :heavy_check_mark:                                                     | Specify the provider through which the payment must be processed.      |