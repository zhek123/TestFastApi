from fastapi import FastAPI
from src.article.routers import router as article_router
app = FastAPI()
app.include_router(article_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
