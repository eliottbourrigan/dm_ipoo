from carburant import Carburant


class Pompe:
    """ Représente une pompe.

    Attributes
    ----------
    carburant : Carburant
        Le carburant de la pompe.
    volume_maximal : int
        Le volume maximal de la pompe.
    volume_disponible : int
        Le volume disponible de la pompe.

    Examples
    --------
    >>> from substance_chimique import SubstanceChimique
    >>> butane = SubstanceChimique(
    ...     nom='butane', numero_cas='106-97-8', numero_ce='203-448-7')
    >>> propane = SubstanceChimique(
    ...     nom='propane', numero_cas='74-98-6', numero_ce='200-827-9')
    >>> sp95 = Carburant(
    ...     nom='SP95', composition_chimique={butane: 0.95, propane: 0.05})
    >>> pompe = Pompe(carburant=sp95, volume_maximal=10, volume_disponible=5)
    >>> pompe._vide()
    False
    >>> pompe._remplir(5)
    >>> pompe._servir(3)
    3
    >>> pompe._servir(9)
    7
    >>> pompe._vide()
    True

    """
    def __init__(
            self, carburant: Carburant,
            volume_maximal: int, volume_disponible: int = 0) -> None:
        """Initialise une pompe.

        Parameters
        ----------
        carburant : Carburant
            Le carburant de la pompe.
        volume_maximal : int
            Le volume maximal de la pompe.
        volume_disponible : int
            Le volume disponible de la pompe.

        """
        # Vérification des types des arguments
        if not isinstance(carburant, Carburant):
            raise TypeError("Le carburant doit être de type 'Carburant'.")
        if not isinstance(volume_maximal, int):
            raise TypeError("Le volume maximal doit être de type 'int'.")
        if not isinstance(volume_disponible, int):
            raise TypeError("Le volume disponible doit être de type 'int'.")

        # Le volume maximal doit être strictement supérieur à 0
        if not volume_maximal > 0:
            raise ValueError("Le volume maximal doit être > 0.")

        # Le volume disponible est entre 0 et le volume maximal
        if not 0 <= volume_disponible <= volume_maximal:
            raise ValueError(
                "Le volume disponible doit être entre 0 et le volume maximal."
            )

        # Assignation des attributs
        self.carburant = carburant
        self.__volume_maximal = volume_maximal
        self.__volume_disponible = volume_disponible

    def _vide(self) -> bool:
        """Indique si la pompe est vide.

        Returns
        -------
        bool
            True si la pompe est vide, False sinon.

        """
        return self.__volume_disponible == 0

    def _remplir(self, volume: int) -> int:
        """Remplit la pompe.

        Parameters
        ----------
        volume : int
            Le volume à ajouter à la pompe.

        Returns
        -------
        int
            Le volume ajouté à la pompe.

        """
        # Vérification du volume
        if not volume > 0:
            raise ValueError("Le volume doit être > 0.")

        # Calcul du volume ajouté
        volume = min(volume, self.__volume_maximal - self.__volume_disponible)

        # Remplissage de la pompe
        self.__volume_disponible += volume

    def _servir(self, volume: int) -> int:
        """Sert du carburant.

        Parameters
        ----------
        volume : int
            Le volume à servir.

        Returns
        -------
        int
            Le volume servi.

        """
        # Vérification du volume
        if not volume > 0:
            raise ValueError("Le volume doit être > 0.")

        # Calcul du volume servi
        volume_servi = min(volume, self.__volume_disponible)

        # Service du carburant
        self.__volume_disponible -= volume_servi
        return volume_servi
