from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    contacts = relationship("Contact", back_populates="owner", cascade="all, delete")


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="contacts")
