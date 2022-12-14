from routes.books import router as booksRouter
from routes.pages import router as pagesRouter
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Sayan's 9Hentai API", description="A simple API for hentai", version="1.0.0")
app.include_router(booksRouter, prefix="/books", tags=["books"])
app.include_router(pagesRouter, prefix="/pages", tags=["pages"])

uvicorn.run(app)