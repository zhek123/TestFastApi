from uuid import UUID
from database import get_async_session
from src.article.schemas import ArticleRead, ArticleCreate, UpdateArticlesPayload
from src.article.selectors import GetArticleSelector, ListArticlesSelector
from src.article.services import CreateArticleService, UpdateArticleService, DeleteArticleService
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException

router = APIRouter()


@router.get("/articles/{article_id}", response_model=ArticleRead)
async def read_article(article_id: UUID, session: AsyncSession = Depends(get_async_session)):
    selector = GetArticleSelector(session)
    return await selector.execute(article_id)


@router.get("/articles/", response_model=list[ArticleRead])
async def list_articles(skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_async_session)):
    selector = ListArticlesSelector(session)
    return await selector.execute(skip, limit)


@router.post("/articles/", status_code=201, response_model=list[ArticleRead])
async def create_articles(articles: list[ArticleCreate], session: AsyncSession = Depends(get_async_session)):
    service = CreateArticleService(session)
    return await service.execute(articles)


@router.patch("/articles/", status_code=204)
async def update_articles(payload: UpdateArticlesPayload, session: AsyncSession = Depends(get_async_session)):
    service = UpdateArticleService(session)
    try:
        await service.execute(payload.title, payload.description, payload.article_ids)
    except Exception as e:  # Добавлена обработка исключений для примера
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/articles/", status_code=204)
async def delete_articles(article_ids: list[UUID], session: AsyncSession = Depends(get_async_session)):
    service = DeleteArticleService(session)
    await service.delete_articles(article_ids)
