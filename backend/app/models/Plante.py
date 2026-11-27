from sqlalchemy import Column, Integer, String, Text, Boolean
from app.models.base import Base, BaseModelMixin


class Plante(Base, BaseModelMixin):
    """modèle représentant une plante"""
    __tablename__ = "plante"

    id = Column(Integer, primary_key=True)
    common_name = Column(String(255))
    scientific_name = Column(Text)
    family = Column(String(255))
    cycle = Column(String(100))
    description = Column(Text)
    watering = Column(String(100))
    sunlight = Column(Text)
    soil = Column(Text)
    indoor = Column(Boolean)
    care_level = Column(String(100))
    fruits = Column(Boolean)
    fruiting_season = Column(String(100))
    harvest_season = Column(String(100))
    default_image = Column(Text)