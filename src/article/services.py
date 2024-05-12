from src.article.schemas import ArticleCreate, ArticleRead
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from src.article.repositories import ArticleRepository
from src.article.validators import check_article_ids_exist


class CreateArticleService:
    def __init__(self, session: AsyncSession):
        self.repo = ArticleRepository(session)

    async def execute(self, articles_data: list[ArticleCreate]) -> list[ArticleRead]:
        res = await self.repo.create_articles(articles_data)
        return res


class UpdateArticleService:
    def __init__(self, session: AsyncSession):
        self.repo = ArticleRepository(session)

    async def execute(self, title: str, description: str, article_ids: list[UUID]) -> None:
        await check_article_ids_exist(self.repo, article_ids)
        await self.repo.update_articles(title, description, article_ids)


class DeleteArticleService:
    def __init__(self, session: AsyncSession):
        self.repo = ArticleRepository(session)

    async def delete_articles(self, article_ids: list[UUID]) -> None:
        await check_article_ids_exist(self.repo, article_ids)
        await self.repo.delete_articles(article_ids)
