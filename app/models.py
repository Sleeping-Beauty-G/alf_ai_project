from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, func
from .database import Base

class QueryHistory(Base):
    __tablename__ = "query_history"

    id = Column(Integer, primary_key=True, index=True)
    cadastral_number = Column(String, index=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    result = Column(Boolean, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
