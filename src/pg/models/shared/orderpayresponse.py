"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import orderpaydata as shared_orderpaydata
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg import utils
from typing import Optional

class OrderPayResponseAction(str, Enum):
    r"""One of [\\"link\\", \\"custom\\", \\"form\\"]"""
    LINK = 'link'
    CUSTOM = 'custom'
    FORM = 'form'

class OrderPayResponseChannel(str, Enum):
    r"""One of [\\"link\\", \\"collect\\", \\"qrcode\\"]. In an older version we used to support different channels like 'gpay', 'phonepe' etc. However, we now support only the following channels - link, collect and qrcode. To process payments using gpay, you will have to provide channel as 'link' and provider as 'gpay'"""
    LINK = 'link'
    COLLECT = 'collect'
    QRCODE = 'qrcode'

class OrderPayResponsePaymentMethod(str, Enum):
    r"""One of [\\"upi\\", \\"netbanking\\", \\"card\\", \\"app\\", \\"cardless_emi\\", \\"paylater\\"]"""
    NETBANKING = 'netbanking'
    CARD = 'card'
    UPI = 'upi'
    APP = 'app'
    CARDLESS_EMI = 'cardless_emi'
    PAYLATER = 'paylater'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrderPayResponse:
    action: Optional[OrderPayResponseAction] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})
    r"""One of [\\"link\\", \\"custom\\", \\"form\\"]"""
    cf_payment_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cf_payment_id'), 'exclude': lambda f: f is None }})
    r"""Payment identifier created by Cashfree"""
    channel: Optional[OrderPayResponseChannel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel'), 'exclude': lambda f: f is None }})
    r"""One of [\\"link\\", \\"collect\\", \\"qrcode\\"]. In an older version we used to support different channels like 'gpay', 'phonepe' etc. However, we now support only the following channels - link, collect and qrcode. To process payments using gpay, you will have to provide channel as 'link' and provider as 'gpay'"""
    data: Optional[shared_orderpaydata.OrderPayData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    payment_method: Optional[OrderPayResponsePaymentMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_method'), 'exclude': lambda f: f is None }})
    r"""One of [\\"upi\\", \\"netbanking\\", \\"card\\", \\"app\\", \\"cardless_emi\\", \\"paylater\\"]"""
    

