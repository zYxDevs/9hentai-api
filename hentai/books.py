from __future__ import annotations
import typing
import aiohttp
from pydantic import BaseModel


class Results(BaseModel):
    id: int
    title: str
    alt_title: str
    total_page: int
    total_favorite: int
    total_download: int
    total_view: int
    image_server: str


class Model(BaseModel):
    status: bool
    results: Results


async def get_book(id: int) -> typing.Optional[Model]:
    async with aiohttp.ClientSession() as session:
        async with session.post("https://www1.9hentai.com/api/getBookByID", data={
            "id": id
        }) as response:
            res = await response.json()
            response = Model(**res)
            return response

async def get_pages(id: int) -> typing.Optional[typing.List[str]]:
    book = await get_book(id)
    pages = []
    if book:
        pages.extend(f"{book.results.image_server}/{id}/{i}.jpg" for i in range(1, book.results.total_page + 1))

    return pages 