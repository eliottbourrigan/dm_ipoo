from pompe import Pompe


class Station:
    """Représente une station-service.

    Attributes
    ----------
    pompes : dict[str, Pompe]
        Les pompes de la station-service.
    prix : dict[str, float]
        Les prix des carburants.

    Examples
    --------
    >>> from pompe import Pompe
    >>> from carburant import Carburant
    >>> from substance_chimique import SubstanceChimique
    >>> butane = SubstanceChimique(
    ...     nom='butane', numero_cas='106-97-8', numero_ce='203-448-7')
    >>> propane = SubstanceChimique(
    ...     nom='propane', numero_cas='74-98-6', numero_ce='200-827-9')
    >>> sp95 = Carburant(
    ...     nom='SP95', composition_chimique={butane: 0.95, propane: 0.05})
    >>> pompe = Pompe(carburant=sp95, volume_maximal=10, volume_disponible=5)
    >>> station = Station(
    ...     pompes={'sp95': pompe}, prix={'sp95': 2.0})
    >>> station.servir('sp95', 3)
    >>> station.prix['sp95']
    2.0
    >>> station.servir('sp95', 3)
    >>> station.prix['sp95']
    >>> station._remplir_pompe('sp95', 5, 3.0)
    >>> station.prix['sp95']
    3.0

    """

    def __init__(
            self, pompes: dict[str, Pompe],
            prix: dict[str, float]) -> None:
        """Initialise une station-service.

        Parameters
        ----------
        pompes : dict[str, Pompe]
            Les pompes de la station-service.
        prix : dict[str, float]
            Les prix des carburants.

        """

        # Vériication des types des arguments
        if not isinstance(pompes, dict):
            raise TypeError("Les pompes doivent être un 'dict'.")
        if not isinstance(prix, dict):
            raise TypeError("Les prix doivent être un 'dict'.")

        # Les prix doivent être supérieurs à 0
        if not all(prix[pompe] > 0 for pompe in prix):
            raise ValueError("Les prix doivent être > 0.")

        # Vérifier que les noms des pompes correspondent aux clés des prix
        if not set(pompes) == set(prix):
            raise ValueError(
                "Les clés des pompes et des prix doivent être identiques.")

        # Assignation des attributs
        self.pompes = pompes
        self.prix = prix

    def __verifier_nom_carburant(self, nom_carburant: str):
        """Vérifie si un nom de carburant est valide.

        Parameters
        ----------
        nom_carburant : str
            Le nom du carburant.

        """
        if nom_carburant not in self.prix:
            raise ValueError("Le nom du carburant est invalide.")

    def __verifier_pompe(self, nom_carburant: str):
        """Vérifie que le nom du carburant correspond à celui de la pompe.

        Parameters
        ----------
        nom_carburant : str
            Le nom du carburant.

        """
        carburants_station = [p.carburant.nom for p in self.pompes.values()]
        if nom_carburant not in carburants_station:
            raise ValueError("Le carburant ne correspond à aucune pompe.")

    def _mettre_a_jour_prix(
            self, nom_carburant: str, nouveau_prix: float):
        """Met à jour le prix d'un carburant.

        Parameters
        ----------
        nom_carburant : str
            Le nom du carburant.
        nouveau_prix : float
            Le nouveau prix du carburant.

        """

        # Vérification du nom du carburant
        self.__verifier_nom_carburant(nom_carburant)

        # Vérification du nouveau prix
        if nouveau_prix <= 0:
            raise ValueError("Le prix doit être > 0.")

        #  Il est impossible de modifier le prix d’un carburant indisponible
        if self.pompes[nom_carburant]._vide():
            raise ValueError("La pompe est vide.")

        # Mise à jour du prix
        self.prix[nom_carburant] = nouveau_prix

    def _remplir_pompe(
            self, nom_carburant: str, volume: int,
            nouveau_prix: int = None):
        """Remplit une pompe d'un volume donné.

        Parameters
        ----------
        nom_carburant : str
            Le nom du carburant.
        volume : int
            Le volume à ajouter à la pompe.
        nouveau_prix : float
            Le nouveau prix du carburant.

        """
        # Vérification du nom du carburant
        self.__verifier_nom_carburant(nom_carburant)

        # Vérification de la pompe
        self.__verifier_pompe(nom_carburant)

        # Si le carburant est indisponible, il faut mettre le prix a jour
        if self.pompes[nom_carburant]._vide() and nouveau_prix is None:
            raise ValueError("Le prix du carburant doit être renseigné.")

        # Si le carburant est disponible, pas de nouveau prix
        if not self.pompes[nom_carburant]._vide() and nouveau_prix is not None:
            raise ValueError(
                "Le prix du carburant ne doit pas être renseigné.")

        # Mise à jour du prix si nécessaire
        if nouveau_prix is not None:
            # Vérification du nouveau prix
            if nouveau_prix <= 0:
                raise ValueError("Le prix doit être > 0.")

            # Mise à jour du prix
            self.prix[nom_carburant] = nouveau_prix

        # Remplissage de la pompe
        self.pompes[nom_carburant]._remplir(volume)

    def servir(self, nom_carburant: str, volume: int):
        """Sert un volume de carburant.

        Parameters
        ----------
        nom_carburant : str
            Le nom du carburant.
        volume : int
            Le volume à servir.

        """
        # Vérification du nom du carburant
        self.__verifier_nom_carburant(nom_carburant)

        # Vérification de la pompe
        self.__verifier_pompe(nom_carburant)

        # La pompe est-elle vide ?
        if self.pompes[nom_carburant]._vide():
            raise ValueError("La pompe est vide.")

        # Le volume doit être positif
        if volume <= 0:
            raise ValueError("Le volume doit être > 0.")

        # Servir le volume
        self.pompes[nom_carburant]._servir(volume)

        # Si la pompe est maintenant vide, le prix doit être None
        if self.pompes[nom_carburant]._vide():
            self.prix[nom_carburant] = None
