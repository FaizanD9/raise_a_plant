from sqlalchemy import func

from app.models.PlanteDAOInterface import PlantDAOInterface
from app.models.Plante import Plante


class PlanteDAO(PlantDAOInterface):
    def __init__(self, session_factory):
        self.SessionFactory = session_factory

    def connect(self):
        """retourne une session de connexion ORM"""
        return self.SessionFactory()

    def count(self):
        """nombre de plantes en base"""
        session = self.connect()
        try:
            return session.query(Plante).count()
        finally:
            session.close()

    def findAll(self):
        """trouve toutes les plantes"""
        session = self.connect()
        try:
            return session.query(Plante).order_by(Plante.id).all()
        finally:
            session.close()

    def findById(self, id):
        """trouve une plante par son id"""
        session = self.connect()
        try:
            return session.query(Plante).filter(Plante.id == id).first()
        finally:
            session.close()

    def findByIds(self, ids):
        """trouve les plantes dont l'id est dans la liste"""
        if not ids:
            return []
        session = self.connect()
        try:
            return session.query(Plante).filter(Plante.id.in_(ids)).all()
        finally:
            session.close()

    def findPage(self, family=None, search=None, page=1, per_page=24):
        """trouve une page de plantes, avec filtres optionnels"""
        session = self.connect()
        try:
            query = session.query(Plante)
            if family:
                query = query.filter(Plante.family == family)
            if search:
                query = query.filter(Plante.common_name.ilike(f"%{search}%"))
            total = query.count()
            offset = (page - 1) * per_page
            plants = query.order_by(Plante.id).offset(offset).limit(per_page).all()
            return plants, total
        finally:
            session.close()

    def findIdsByFamily(self, family):
        """trouve les id des plantes d'une catégorie"""
        session = self.connect()
        try:
            rows = (
                session.query(Plante.id)
                .filter(Plante.family == family)
                .order_by(Plante.id)
                .all()
            )
            return [row[0] for row in rows]
        finally:
            session.close()

    def findAllFamiliesWithCount(self):
        """trouve toutes les familles avec leur nombre de plantes"""
        session = self.connect()
        try:
            return (
                session.query(Plante.family, func.count(Plante.id))
                .filter(Plante.family.isnot(None))
                .group_by(Plante.family)
                .order_by(Plante.family)
                .all()
            )
        finally:
            session.close()