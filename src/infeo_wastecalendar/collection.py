import datetime as dt
from typing import Any


class CollectionFraction:
    """A fraction of a collectionn of the Infeo Wastecalendar API."""

    def __init__(self, raw_data: dict[str, Any]) -> None:
        self._raw_data = raw_data

    @property
    def fractionName(self) -> str:
        return self._raw_data["fractionName"]

    @property
    def fractionShortname(self) -> str:
        return self._raw_data["fractionShortname"]

    @property
    def color(self) -> int:
        return self._raw_data["color"]

    @property
    def colorHex(self) -> str:
        return self._raw_data["colorHex"]

    @property
    def colorText(self) -> str:
        return self._raw_data["colorText"]


class Collection:
    """A collection of the Infeo Wastecalendar API."""

    def __init__(self, raw_data: dict[str, Any]) -> None:
        self._raw_data = raw_data

    @property
    def plannedCollection(self) -> dt.datetime:
        return dt.datetime.strptime(
            self._raw_data["plannedCollection"], "%Y-%m-%dT%H:%M:%S%z"
        )

    @property
    def fractions(self) -> list[CollectionFraction]:
        return [CollectionFraction(obj) for obj in self._raw_data["fractions"]]
