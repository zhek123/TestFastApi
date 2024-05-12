from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.article.repositories import ArticleRepository
from src.article.schemas import ArticleRead


class GetArticleSelector:
    def __init__(self, session: AsyncSession):
        self.repo = ArticleRepository(session)

    async def execute(self, article_id: UUID) -> ArticleRead:
        article = await self.repo.get_article_record(article_id)
        if not article:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
        return article


class ListArticlesSelector:
    def __init__(self, session: AsyncSession):
        self.repo = ArticleRepository(session)

    async def execute(self, skip: int, limit: int) -> list[ArticleRead]:
        return await self.repo.list_article_records(skip, limit)


class DeleteArticleSelector:
    def __init__(self, session: AsyncSession):
        self.repo = ArticleRepository(session)

    async def execute(self, article_ids: list[UUID]) -> None:
        await self.repo.delete_articles(article_ids)
