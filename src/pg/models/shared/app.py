"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg import utils

class Provider(str, Enum):
    r"""Specify the provider through which the payment must be processed."""
    GPAY = 'gpay'
    PHONEPE = 'phonepe'
    OLA = 'ola'
    PAYTM = 'paytm'
    AMAZON = 'amazon'
    AIRTEL = 'airtel'
    FREECHARGE = 'freecharge'
    MOBIKWIK = 'mobikwik'
    JIO = 'jio'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class App:
    channel: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel') }})
    r"""Specify the channel through which the payment must be processed."""
    phone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone') }})
    r"""Customer phone number associated with a wallet for payment."""
    provider: Provider = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    r"""Specify the provider through which the payment must be processed."""
    

