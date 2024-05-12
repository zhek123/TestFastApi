from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.article.repositories import ArticleRepository
from uuid import UUID


async def check_article_ids_exist(repo, article_ids: list[UUID]) -> None:
    existing_ids = set(await repo.get_article_record_ids(article_ids))
    requested_ids_set = set(article_ids)
    missing_ids = requested_ids_set - existing_ids

    if missing_ids:
        detail = f"Articles with the following IDs not found: {', '.join(str(id) for id in missing_ids)}"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
