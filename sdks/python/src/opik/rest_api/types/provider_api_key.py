# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider_api_key_provider import ProviderApiKeyProvider


class ProviderApiKey(UniversalBaseModel):
    id: typing.Optional[str] = None
    provider: ProviderApiKeyProvider
    api_key: typing.Optional[str] = None
    name: typing.Optional[str] = None
    headers: typing.Optional[typing.Dict[str, str]] = None
    configuration: typing.Optional[typing.Dict[str, str]] = None
    base_url: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    created_by: typing.Optional[str] = None
    last_updated_at: typing.Optional[dt.datetime] = None
    last_updated_by: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
