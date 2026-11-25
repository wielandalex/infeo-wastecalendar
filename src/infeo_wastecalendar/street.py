import datetime as dt
from typing import Any


class Street:
    """A street of the Infeo Wastecalendar API."""

    def __init__(self, raw_data: dict[str, Any]) -> None:
        self._raw_data = raw_data

    @property
    def id(self) -> int:
        return self._raw_data["id"]

    @property
    def lastChange(self) -> dt.datetime:
        return dt.datetime.strptime(self._raw_data["lastChange"], "%Y-%m-%dT%H:%M:%S%z")

    @property
    def name(self) -> str:
        return self._raw_data["name"]

    @property
    def cityId(self) -> int:
        return self._raw_data["cityId"]

    @property
    def calendarId(self) -> int:
        return self._raw_data["calendarId"]
