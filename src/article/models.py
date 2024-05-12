from sqlalchemy import String

from src.models import UUIDAuditBaseModel
from sqlalchemy.orm import Mapped, mapped_column


class Article(UUIDAuditBaseModel):
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
