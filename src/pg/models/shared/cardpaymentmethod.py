"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import card as shared_card
from dataclasses_json import Undefined, dataclass_json
from pg import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CardPaymentMethod:
    r"""The card payment object is used to make payment using either plain card number, saved card instrument id or using cryptogram"""
    card: shared_card.Card = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('card') }})
    

