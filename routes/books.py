import typing
from fastapi import APIRouter, Depends
from hentai import books
router = APIRouter()

@router.get("/{id}", response_model=typing.Optional[books.Model])
async def getBookById(commons: dict = Depends(books.get_book)):
    return commons

