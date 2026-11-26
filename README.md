# Infeo Wastecalendar API Client

Simple python library to interface with the Infeo Wastecalendar API.
Used to retrieve the planned trash collection dates managed by users of Infeo software.

*This is an unofficial library. It isn't connected to the company Infeo in any way.*
I simply looked at the publicly available HTML Forms to retrieve the collection dates and
built this library from this information.

Currently known cities which are provided by the API:
- Innsbruck
- Klagenfurt
- Leoben
- Salzburg
- St. Pölten

## Usage

```python
import asyncio
from datetime import datetime as dt

from aiohttp import ClientSession
from infeo_wastecalendar import InfeoWastecalendarAPI, WellKnownBaseUrl


async def main():
    async with ClientSession() as session:
        client = InfeoWastecalendarAPI(session, WellKnownBaseUrl.SALZBURG)

        calendars = await client.async_get_calendars()
        calendar = calendars[0]

        cities = await client.async_get_cities(calendar.id)
        city = cities[0]

        streets = await client.async_get_streets(calendar.id, city.id)
        street = streets[0]

        housenumbers = await client.async_get_housenumbers(calendar.id, street.id)
        housenumber = housenumbers[0]

        fractions = await client.async_get_fractions(
            calendar.id, city.id, street.id, housenumber
        )

        collections = await client.async_get_collections(
            calendar.id,
            city.id,
            street.id,
            housenumber,
            [fraction.id for fraction in fractions],
        )
        next_collection = next(
            filter(
                lambda collection: (
                    collection.plannedCollection.date() >= dt.now().date()
                ),
                collections,
            )
        )
        print(
            f"{next_collection.plannedCollection.date()}: {
                [fraction.fractionName for fraction in next_collection.fractions]
            }"
        )


if __name__ == "__main__":
    asyncio.run(main())
```
