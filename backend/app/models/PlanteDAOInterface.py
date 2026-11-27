class PlantDAOInterface:
    """Liste des opérations qu'un DAO de plantes doit fournir.    """

    def connect(self):
        """retourne une session de connexion ORM"""
        pass

    def count(self):
        """nombre de plantes en base"""
        pass

    def findAll(self):
        """trouve toutes les plantes"""
        pass

    def findById(self, id):
        """trouve une plante par son id"""
        pass

    def findByIds(self, ids):
        """trouve les plantes dont l'id est dans la liste"""
        pass

    def findPage(self, family=None, search=None, page=1, per_page=24):
        """trouve une page de plantes, avec filtres optionnels"""
        pass

    def findIdsByFamily(self, family):
        """trouve les id des plantes d'une catégorie"""
        pass


    def findAllFamiliesWithCount(self):
        """trouve toutes les familles avec leur nombre de plantes"""
        pass