import datetime as dt
from typing import Any


class Fraction:
    """A fraction of the Infeo Wastecalendar API."""

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
    def shortname(self) -> str:
        return self._raw_data["shortname"]

    @property
    def color(self) -> int:
        return self._raw_data["color"]

    @property
    def aloaId(self) -> int:
        return self._raw_data["aloaId"]

    @property
    def colorHex(self) -> str:
        return self._raw_data["colorHex"]

    @property
    def colorHexWithAlphaChannel(self) -> str:
        return self._raw_data["colorHexWithAlphaChannel"]
