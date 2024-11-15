# coding: utf-8

"""
    Authoring API

    Experimental API to edit xblocks and course content.       Danger: Do not use on running courses!        - How to gain access: Please email the owners of this openedx service.       - How to use: This API uses oauth2 authentication with the     access token endpoint: `http://localhost:18000/oauth2/access_token`.     Please see separately provided documentation.       - How to test: You must be logged in as course author for whatever course you want to test with.     You can use the [Swagger UI](https://localhost:18000/authoring-api/ui/) to \"Try out\" the API with your test course. To do this, you must select the \"Local\" server.       - Public vs. Local servers: The \"Public\" server is where you can reach the API externally. The \"Local\" server is     for development with a local edx-platform version,  and for use via the [Swagger UI](https://localhost:18010/authoring-api/ui/).       - Swaggerfile: [Download link](https://localhost:18000/authoring-api/schema/)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UserInfo(BaseModel):
    """
    UserInfo
    """ # noqa: E501
    username: Annotated[str, Field(strict=True, max_length=100)]
    email: StrictStr
    data: StrictStr
    __properties: ClassVar[List[str]] = ["username", "email", "data"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            # "email",
            # "data",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = (
            # cls.model_validate(
            {
            "username": obj.get("username"),
            "email": obj.get("email"),
            "data": obj.get("data")
        }
        )
        # )
        return _obj
