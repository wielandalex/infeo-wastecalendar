from __future__ import annotations

import datetime as dt
from typing import Any


class Calendar:
    """A calendar of the Infeo Wastecalendar API."""

    def __init__(self, raw_data: dict[str, Any]) -> None:
        self._raw_data = raw_data

    @property
    def from_(self) -> dt.datetime:
        return dt.datetime.strptime(self._raw_data["from"], "%Y-%m-%dT%H:%M:%S%z")

    @property
    def until(self) -> dt.datetime:
        return dt.datetime.strptime(self._raw_data["until"], "%Y-%m-%dT%H:%M:%S%z")

    @property
    def created(self) -> dt.datetime:
        return dt.datetime.strptime(self._raw_data["created"], "%Y-%m-%dT%H:%M:%S%z")

    @property
    def availableFrom(self) -> dt.datetime:
        return dt.datetime.strptime(
            self._raw_data["availableFrom"], "%Y-%m-%dT%H:%M:%S%z"
        )

    @property
    def availableUntil(self) -> dt.datetime:
        return dt.datetime.strptime(
            self._raw_data["availableUntil"], "%Y-%m-%dT%H:%M:%S%z"
        )

    @property
    def isDefault(self) -> bool:
        return self._raw_data["isDefault"]

    @property
    def externalSystems(self) -> int:
        return self._raw_data["externalSystems"]

    @property
    def renameAction(self) -> str | None:
        return self._raw_data["renameAction"]

    @property
    def name(self) -> str:
        return self._raw_data["name"]

    @property
    def id(self) -> int:
        return self._raw_data["id"]

    @property
    def lastChange(self) -> dt.datetime:
        return dt.datetime.strptime(self._raw_data["lastChange"], "%Y-%m-%dT%H:%M:%S%z")
