from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    recipe_id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    dish_id = Column(Integer, ForeignKey("items.dish_id"), nullable=False)
    resource_id = Column(Integer, ForeignKey("resources.resource_id"), nullable=False)
    cost = Column(Integer, index=True, nullable=False, server_default='0.0')

    items = relationship("Items", back_populates="recipes")
    resources = relationship("Resource", back_populates="recipes")
