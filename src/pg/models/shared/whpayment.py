"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import whpayment_method as shared_whpayment_method
from dataclasses_json import Undefined, dataclass_json
from pg import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WHpayment:
    auth_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_id'), 'exclude': lambda f: f is None }})
    bank_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_reference'), 'exclude': lambda f: f is None }})
    cf_payment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cf_payment_id'), 'exclude': lambda f: f is None }})
    payment_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_amount'), 'exclude': lambda f: f is None }})
    payment_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_currency'), 'exclude': lambda f: f is None }})
    payment_group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_group'), 'exclude': lambda f: f is None }})
    payment_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_message'), 'exclude': lambda f: f is None }})
    payment_method: Optional[shared_whpayment_method.WHpaymentMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_method'), 'exclude': lambda f: f is None }})
    payment_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_status'), 'exclude': lambda f: f is None }})
    payment_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_time'), 'exclude': lambda f: f is None }})
    

