from sqlalchemy import DateTime, func
from sqlalchemy.orm import declared_attr, Mapped, mapped_column
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class UUIDAuditBaseModel(Base):
    __abstract__ = True
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
