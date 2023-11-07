"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg import utils
from typing import Optional

class SchemasRateLimitErrorType(str, Enum):
    r"""rate_limit_error"""
    RATE_LIMIT_ERROR = 'rate_limit_error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RateLimitError(Exception):
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    type: Optional[SchemasRateLimitErrorType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""rate_limit_error"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)