from routes.books import router as booksRouter
from routes.pages import router as pagesRouter
from fastapi import FastAPI
import uvicorn
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read_file(open("config.ini"))

app = FastAPI(title="Sayan's 9Hentai API", description="A simple API for hentai", version="1.0.0")
app.include_router(booksRouter, prefix="/books", tags=["books"])
app.include_router(pagesRouter, prefix="/pages", tags=["pages"])

uvicorn.run(app, port=int(cfg['api']['port']), host=cfg['api']['host'])