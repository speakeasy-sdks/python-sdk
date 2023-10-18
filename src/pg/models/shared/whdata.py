"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import whcustomer_details as shared_whcustomer_details
from ..shared import whorder as shared_whorder
from ..shared import whpayment as shared_whpayment
from dataclasses_json import Undefined, dataclass_json
from pg import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WHdata:
    customer_details: Optional[shared_whcustomer_details.WHcustomerDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_details'), 'exclude': lambda f: f is None }})
    order: Optional[shared_whorder.WHorder] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order'), 'exclude': lambda f: f is None }})
    payment: Optional[shared_whpayment.WHpayment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment'), 'exclude': lambda f: f is None }})
    

