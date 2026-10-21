from httpx import AsyncClient, Timeout

WELL_KNOWN_BASE_URLS = {
    "Innsbruck": "https://services.infeo.at/aloa/api/ikb/wastecalendar",
    "Klagenfurt": "https://services.infeo.at/awm/api/klagenfurt/wastecalendar",
    "Leoben": "https://services.infeo.at/aloa/api/leoben/wastecalendar",
    "Salzburg": "https://services.infeo.at/Awm/api/salzburg/wastecalendar",
    "St. Pölten": "https://services.infeo.at/awm/api/st.p%C3%B6lten/wastecalendar",
}


class InfeoWastecalendarAPI:
    """Client to interact with the Infeo Wastecalendar API."""

    def __init__(self, base_url: str):
        self._client = AsyncClient(
            base_url=base_url, timeout=Timeout(5, read=30), follow_redirects=True
        )

    async def async_get_calendars(self):
        res = await self._client.get(
            "/calendars/", params={"showUnpublishedCalendars": "false"}
        )
        res.raise_for_status()
        calendars = res.json()
        return calendars

    async def async_get_cities(self, calendar_id: int):
        res = await self._client.get("/cities/", params={"calendarId": calendar_id})
        res.raise_for_status()
        cities = res.json()
        return cities

    async def async_get_streets(self, calendar_id: int, city_id: int):
        res = await self._client.get(
            "/streets/", params={"calendarId": calendar_id, "cityId": city_id}
        )
        res.raise_for_status()
        streets = res.json()
        return streets

    async def async_get_housenumbers(
        self, calendar_id: int, street_id: int
    ) -> list[str]:
        res = await self._client.get(
            "/housenumbers/", params={"calendarId": calendar_id, "streetId": street_id}
        )
        res.raise_for_status()
        housenumbers = res.json()
        return housenumbers

    async def async_get_fractions(
        self, calendar_id: int, city_id: int, street_id: int, housenumber: str
    ):
        res = await self._client.get(
            "/v2/fractions/",
            params={
                "calendarId": calendar_id,
                "cityId": city_id,
                "streetId": street_id,
                "housenumber": housenumber,
            },
        )
        res.raise_for_status()
        fractions = res.json()
        return fractions["fractions"]

    async def async_get_collections(
        self,
        calendar_id: int,
        city_id: int,
        street_id: int,
        housenumber: str,
        fraction_ids: list[int],
    ):
        res = await self._client.get(
            "/v2/export/",
            params={
                "calendarId": calendar_id,
                "cityId": city_id,
                "streetId": street_id,
                "housenumber": housenumber,
                "fractionIds": fraction_ids,
            },
        )
        res.raise_for_status()
        collections = res.json()
        return collections
