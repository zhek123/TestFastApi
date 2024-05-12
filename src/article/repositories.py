import uuid

from sqlalchemy import update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.article.models import Article

from src.article.schemas import ArticleCreate, ArticleRead


class ArticleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_articles(self, articles_data: list[ArticleCreate]) -> list[ArticleRead]:
        articles = [Article(title=article.title, description=article.description) for article in articles_data]
        self.session.add_all(articles)
        await self.session.flush()
        res = [ArticleRead.model_validate(article) for article in articles]
        await self.session.commit()
        return res

    async def update_articles(self, title: str, description: str, article_ids: list[uuid.UUID]) -> None:
        query = select(Article).where(Article.id.in_(article_ids)).with_for_update()
        await self.session.execute(query)

        await self.session.execute(
            update(Article).where(Article.id.in_(article_ids)).values(title=title, description=description)
        )
        await self.session.commit()

    async def delete_articles(self, article_ids: list[uuid.UUID]) -> None:
        await self.session.execute(delete(Article).where(Article.id.in_(article_ids)))
        await self.session.commit()

    async def get_article_record(self, article_id: uuid.UUID) -> ArticleRead:
        result = await self.session.execute(select(Article).where(Article.id == article_id))
        article = result.scalar_one_or_none()
        return ArticleRead.model_validate(article) if article else None

    async def list_article_records(self, skip: int = 0, limit: int = 100) -> list[ArticleRead]:
        result = await self.session.execute(select(Article).offset(skip).limit(limit))
        articles = result.scalars().all()
        return [ArticleRead.model_validate(article) for article in articles]

    async def get_article_record_ids(self, article_ids: list[uuid.UUID]) -> list[uuid.UUID]:
        result = await self.session.execute(select(Article.id).where(Article.id.in_(article_ids)))
        ids = result.scalars().all()
        return ids
