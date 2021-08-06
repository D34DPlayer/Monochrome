import uuid
import enum

from sqlalchemy import Column, String, select, or_, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(15), nullable=False, unique=True)
    email = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)

    @classmethod
    async def from_username_email(cls, db_session: AsyncSession, username_email: str, mail: str = ""):
        if mail == "":
            mail = username_email
        stmt = select(cls).where(or_(cls.username == username_email, cls.email == mail))
        result = await db_session.execute(stmt)
        return result.scalars().first()

    @classmethod
    async def all(cls, db_session: AsyncSession, limit: int = 20, offset: int = 0):
        return await cls.pagination(db_session, select(cls), limit, offset, (cls.username,))