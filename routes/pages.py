import typing
from fastapi import APIRouter, Depends
from hentai import books

router = APIRouter()


@router.get("/{id}", response_model=typing.Optional[typing.List[str]])
async def getPagesById(commons: dict = Depends(books.get_pages)):
    return commons