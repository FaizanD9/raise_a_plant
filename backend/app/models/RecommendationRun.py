from sqlalchemy import Column, Float, Integer, String, Text

from app.models.base import Base, BaseModelMixin, TimestampMixin


class RecommendationRun(Base, BaseModelMixin, TimestampMixin):
    """Modèle du journal des recherches : une ligne par recherche calculée.
    Permet d'afficher les temps de réponse min, max et moyen de chaque méthode
    dans le tableau de bord.
    """
    __tablename__ = "recommendation_runs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    approach = Column(String(40), nullable=False, index=True)  # "heuristic" ou "vector"
    # temps du calcul de la méthode seul (scores + tri)
    algo_ms = Column(Float, nullable=False)
    # temps total côté serveur (filtrage + calcul + pagination)
    total_ms = Column(Float, nullable=False)
    result_count = Column(Integer, nullable=False)
    corpus_size = Column(Integer, nullable=False)
    query_text = Column(Text, nullable=True)