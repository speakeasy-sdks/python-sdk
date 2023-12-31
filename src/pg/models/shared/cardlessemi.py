"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg import utils
from typing import Optional

class CardlessEMIProvider(str, Enum):
    r"""One of [`flexmoney`, `zestmoney`, `hdfc`, `icici`, `cashe`, `idfc`, `kotak`]"""
    FLEXMONEY = 'flexmoney'
    ZESTMONEY = 'zestmoney'
    HDFC = 'hdfc'
    ICICI = 'icici'
    CASHE = 'cashe'
    IDFC = 'idfc'
    KOTAK = 'kotak'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CardlessEMI:
    channel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel'), 'exclude': lambda f: f is None }})
    r"""The channel for cardless EMI is always `link`"""
    emi_tenure: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emi_tenure'), 'exclude': lambda f: f is None }})
    r"""EMI tenure for the selected provider. This is mandatory when provider is one of [`hdfc`, `icici`, `cashe`, `idfc`, `kotak`]"""
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""Customers phone number for this payment instrument. If the customer is not eligible you will receive a 400 error with type as 'invalid_request_error' and code as 'invalid_request_error'"""
    provider: Optional[CardlessEMIProvider] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider'), 'exclude': lambda f: f is None }})
    r"""One of [`flexmoney`, `zestmoney`, `hdfc`, `icici`, `cashe`, `idfc`, `kotak`]"""
    

