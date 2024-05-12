from pydantic import BaseModel, Field, ConfigDict
import uuid
from datetime import datetime
from uuid import UUID


class ArticleBase(BaseModel):
    title: str = Field(..., examples=["Sample Title"])
    description: str = Field(..., examples=["Sample Description"])


class ArticleCreate(ArticleBase):
    pass


class ArticleRead(ArticleBase):
    id: uuid.UUID = Field(..., examples=[uuid.uuid4()])
    created_at: datetime = Field(..., examples=[datetime.now()])
    updated_at: datetime = Field(..., examples=[datetime.now()])

    model_config = ConfigDict(from_attributes=True)


class UpdateArticlesPayload(BaseModel):
    title: str
    description: str
    article_ids: list[UUID]
