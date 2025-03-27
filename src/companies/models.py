from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    is_public = Column(Boolean, default=True, nullable=False)

    synonyms = relationship("CompanySynonym", back_populates="company", cascade="all, delete-orphan")


class CompanySynonym(Base):
    __tablename__ = "company_synonyms"

    id = Column(Integer, primary_key=True, index=True)
    synonym = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)

    company = relationship("Company", back_populates="synonyms")
