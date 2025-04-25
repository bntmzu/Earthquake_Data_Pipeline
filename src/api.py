import asyncio
from datetime import datetime, timezone, timedelta
import aiohttp
from src.config import BASE_URL

def get_day_range(days_back: int) -> tuple[str, str]:
    end = datetime.now(timezone.utc) - timedelta(days=days_back)
    start = end - timedelta(days=1)
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")

async def fetch_earthquakes(session: aiohttp.ClientSession, start: str, end: str) -> dict:
    params = {
        "format": "geojson",
        "starttime": start,
        "endtime": end,
        "minmagnitude": 5
    }
    async with session.get(BASE_URL, params=params) as response:
        print(f"Fetching earthquakes from {start} to {end}")
        return await response.json()

async def gather_data(days: int = 7) -> list[dict]:
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(days):
            start, end = get_day_range(i)
            tasks.append(fetch_earthquakes(session, start, end))
        return await asyncio.gather(*tasks)
