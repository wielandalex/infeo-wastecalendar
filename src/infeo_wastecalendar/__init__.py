from enum import StrEnum

from aiohttp import ClientResponse, ClientResponseError, ClientSession

from .calendar import Calendar
from .city import City
from .collection import Collection
from .fraction import Fraction
from .street import Street


class WellKnownBaseUrl(StrEnum):
    INNSBRUCK = "https://services.infeo.at/aloa/api/ikb/wastecalendar"
    KLAGENFURT = "https://services.infeo.at/awm/api/klagenfurt/wastecalendar"
    LEOBEN = "https://services.infeo.at/aloa/api/leoben/wastecalendar"
    SALZBURG = "https://services.infeo.at/Awm/api/salzburg/wastecalendar"
    ST_POELTEN = "https://services.infeo.at/awm/api/st.pölten/wastecalendar"

class InfeoWastecalendarError(Exception):
    """Base error of the Infeo Wastecalendar API."""


async def custom_raise_for_status(response: ClientResponse):
    code = response.status
    text = await response.text()
    try:
        response.raise_for_status()
    except ClientResponseError as ex:
        raise InfeoWastecalendarError(
            f"Error in API request. Code: {code} Text: {text}"
        ) from ex


class InfeoWastecalendarAPI:
    """Client to interact with the Infeo Wastecalendar API."""

    def __init__(self, session: ClientSession, base_url: str):
        """Use one of the base URLs listed in `WELL_KNOWN_BASE_URLS`
        or provide a custom one."""
        session._raise_for_status = custom_raise_for_status
        self._session = session

        # Remove trailing slash from base_url
        if base_url[-1] == "/":
            base_url = base_url[:-1]
        self._base_url = base_url

    async def async_get_calendars(self) -> list[Calendar]:
        """Return calendars."""
        res = await self._session.request(
            "GET",
            f"{self._base_url}/calendars/",
            params={"showUnpublishedCalendars": "false"},
        )
        calendars = [Calendar(obj) for obj in await res.json()]
        return calendars

    async def async_get_cities(self, calendar_id: int) -> list[City]:
        """Return cities."""
        res = await self._session.request(
            "GET", f"{self._base_url}/cities/", params={"calendarId": calendar_id}
        )
        cities = [City(obj) for obj in await res.json()]
        return cities

    async def async_get_streets(self, calendar_id: int, city_id: int) -> list[Street]:
        """Return streets."""
        res = await self._session.request(
            "GET",
            f"{self._base_url}/streets/",
            params={"calendarId": calendar_id, "cityId": city_id},
        )
        streets = [Street(obj) for obj in await res.json()]
        return streets

    async def async_get_housenumbers(
        self, calendar_id: int, street_id: int
    ) -> list[str]:
        "Return housenumbers."
        res = await self._session.request(
            "GET",
            f"{self._base_url}/housenumbers/",
            params={"calendarId": calendar_id, "streetId": street_id},
        )
        housenumbers = await res.json()
        return housenumbers

    async def async_get_fractions(
        self, calendar_id: int, city_id: int, street_id: int, housenumber: str
    ) -> list[Fraction]:
        """Return fractions."""
        res = await self._session.request(
            "GET",
            f"{self._base_url}/v2/fractions/",
            params={
                "calendarId": calendar_id,
                "cityId": city_id,
                "streetId": street_id,
                "housenumber": housenumber,
            },
        )
        obj = await res.json()
        raw_fractions = obj["fractions"]
        fractions = [Fraction(obj) for obj in raw_fractions]
        return fractions

    async def async_get_collections(
        self,
        calendar_id: int,
        city_id: int,
        street_id: int,
        housenumber: str,
        fraction_ids: list[int],
    ) -> list[Collection]:
        """Return collections."""
        res = await self._session.request(
            "GET",
            f"{self._base_url}/v2/export/",
            params={
                "calendarId": calendar_id,
                "cityId": city_id,
                "streetId": street_id,
                "housenumber": housenumber,
                "fractionIds": fraction_ids,
            },
        )
        collections = [Collection(obj) for obj in await res.json()]
        return collections
