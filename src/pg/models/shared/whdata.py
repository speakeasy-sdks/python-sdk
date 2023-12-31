"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .whcustomer_details import WHcustomerDetails
from .whorder import WHorder
from .whpayment import WHpayment
from dataclasses_json import Undefined, dataclass_json
from pg import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WHdata:
    customer_details: Optional[WHcustomerDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_details'), 'exclude': lambda f: f is None }})
    order: Optional[WHorder] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order'), 'exclude': lambda f: f is None }})
    payment: Optional[WHpayment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment'), 'exclude': lambda f: f is None }})
    

