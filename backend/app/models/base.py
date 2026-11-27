import os
from datetime import datetime
from sqlalchemy import Column, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class BaseModelMixin:
    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)
        raise KeyError(f"L'objet '{self.__class__.__name__}' n'a pas l'attribut '{item}'")

    def to_dict(self):
        """Retourne les colonnes de l'objet sous forme de dictionnaire."""
        result = {}
        for col in self.__table__.columns:
            val = getattr(self, col.name)
            if isinstance(val, datetime):
                val = val.strftime("%Y-%m-%d %H:%M:%S")
            result[col.name] = val
        return result


class TimestampMixin:
    """Ajoute automatiquement une date de création aux modèles qui en héritent."""
    created_at = Column(DateTime, default=datetime.now, nullable=False)


def get_engine(db_uri=None):
    """Crée et retourne un moteur SQLAlchemy (backend/data/plantes.db par défaut)."""
    if db_uri is None:
        # base.py -> models/ -> app/ -> backend/
        backend_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        db_path = os.path.join(backend_dir, "data", "plantes.db")
        db_uri = f"sqlite:///{db_path}"
    return create_engine(db_uri, echo=False)


def create_session_factory(engine):
    """Crée la factory de sessions unique à injecter dans les DAO."""
    return sessionmaker(bind=engine, expire_on_commit=False)