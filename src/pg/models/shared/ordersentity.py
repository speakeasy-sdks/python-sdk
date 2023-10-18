"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import customerdetails as shared_customerdetails
from ..shared import ordermeta as shared_ordermeta
from ..shared import paymenturlobject as shared_paymenturlobject
from ..shared import refundurlobject as shared_refundurlobject
from ..shared import settlementurlobject as shared_settlementurlobject
from dataclasses_json import Undefined, dataclass_json
from pg import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrdersEntity:
    cf_order_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cf_order_id'), 'exclude': lambda f: f is None }})
    customer_details: Optional[shared_customerdetails.CustomerDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_details'), 'exclude': lambda f: f is None }})
    r"""The customer details that are necessary. Note that you can pass dummy details if your use case does not require the customer details."""
    entity: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity'), 'exclude': lambda f: f is None }})
    order_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_amount'), 'exclude': lambda f: f is None }})
    order_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_currency'), 'exclude': lambda f: f is None }})
    order_expiry_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_expiry_time'), 'exclude': lambda f: f is None }})
    order_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_id'), 'exclude': lambda f: f is None }})
    order_meta: Optional[shared_ordermeta.OrderMeta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_meta'), 'exclude': lambda f: f is None }})
    order_note: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_note'), 'exclude': lambda f: f is None }})
    order_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_status'), 'exclude': lambda f: f is None }})
    payment_session_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_session_id'), 'exclude': lambda f: f is None }})
    payments: Optional[shared_paymenturlobject.PaymentURLObject] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payments'), 'exclude': lambda f: f is None }})
    refunds: Optional[shared_refundurlobject.RefundURLObject] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refunds'), 'exclude': lambda f: f is None }})
    settlements: Optional[shared_settlementurlobject.SettlementURLObject] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settlements'), 'exclude': lambda f: f is None }})
    

