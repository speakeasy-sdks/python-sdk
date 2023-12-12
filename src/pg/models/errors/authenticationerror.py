"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from pg import utils
from typing import Optional

class SchemasType(str, Enum):
    r"""authentication_error"""
    AUTHENTICATION_ERROR = 'authentication_error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AuthenticationError(Exception):
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    type: Optional[SchemasType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""authentication_error"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))
