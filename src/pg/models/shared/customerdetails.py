"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pg import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomerDetails:
    r"""The customer details that are necessary. Note that you can pass dummy details if your use case does not require the customer details."""
    customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_id') }})
    r"""A unique identifier for the customer. Use alphanumeric values only."""
    customer_phone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_phone') }})
    r"""Customer phone number."""
    customer_bank_account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_bank_account_number'), 'exclude': lambda f: f is None }})
    r"""Customer bank account. Required if you want to do a bank account check (TPV)"""
    customer_bank_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_bank_code'), 'exclude': lambda f: f is None }})
    r"""Customer bank code. Required for net banking payments, if you want to do a bank account check (TPV)"""
    customer_bank_ifsc: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_bank_ifsc'), 'exclude': lambda f: f is None }})
    r"""Customer bank IFSC. Required if you want to do a bank account check (TPV)"""
    customer_email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_email'), 'exclude': lambda f: f is None }})
    r"""Customer email address."""
    

