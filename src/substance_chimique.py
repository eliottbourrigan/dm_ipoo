class SubstanceChimique:
    """Représente une substance chimique.

    Attributes
    ----------
    nom : str
        Le nom de la substance chimique.
    numero_cas : str
        Le numéro CAS de la substance chimique.
    numero_ce : str
        Le numéro CE de la substance chimique.

    Examples
    --------
    >>> butane = SubstanceChimique(
    ...     nom='butane', numero_cas='106-97-8', numero_ce='203-448-7')
    >>> ethanol = SubstanceChimique(
    ...     nom='éthanol', numero_cas='64-17-5', numero_ce='200-578-6')
    >>> butane == ethanol
    False
    >>> repr_butane = (
    ...     "SubstanceChimique(nom='butane', numero_cas='106-97-8', "
    ... "numero_ce='203-448-7')"
    ... )
    >>> repr(butane) == repr_butane
    True

    """

    def __init__(self, nom: str, numero_cas: str, numero_ce: str) -> None:
        """Initialise une substance chimique.

        Parameters
        ----------
        nom : str
            Le nom de la substance chimique.
        numero_cas : str
            Le numéro CAS de la substance chimique.
        numero_ce : str
            Le numéro CE de la substance chimique.

        """
        # Vérification des types des arguments
        if not isinstance(numero_cas, str):
            raise TypeError("Le numéro CAS doit être de type 'str'.")
        if not isinstance(numero_ce, str):
            raise TypeError("Le numéro CE doit être de type 'str'.")
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être de type 'str'.")

        # Vérification des numéros CAS
        if not self.valide_cas(numero_cas):
            raise ValueError(f"Le numéro CAS {numero_cas} est invalide.")

        # Vérification des numéros CE
        if not self.valide_ce(numero_ce):
            raise ValueError(f"Le numéro CE {numero_ce} est invalide.")

        # Assignation des attributs
        self.nom = nom
        self.__numero_cas = numero_cas
        self.__numero_ce = numero_ce

    def __eq__(self, other: 'SubstanceChimique') -> bool:
        """Vérifie si deux substances chimiques sont égales.

        Parameters
        ----------
        other : SubstanceChimique
            L'autre substance chimique à comparer.

        Returns
        -------
        bool
            True si les substances sont égales, False sinon.

        """
        # Si les deux instances ont les mêmes attributs, elles sont égales
        if self.nom == other.nom and \
            self.__numero_cas == other.__numero_cas and \
                self.__numero_ce == other.__numero_ce:
            return True

        # Si au moins un attribut est identique, une des substances est erronée
        if self.nom == other.nom or \
            self.__numero_cas == other.__numero_cas or \
                self.__numero_ce == other.__numero_ce:
            raise ValueError("Une des deux substances est erronée.")

        # Si aucun attribut n'est identique, les instances ne sont pas égales
        return False

    def __repr__(self) -> str:
        """Retourne une représentation de la substance chimique.

        Returns
        -------
        str
            La représentation de la substance chimique.

        """
        return f"SubstanceChimique(nom='{self.nom}', " \
               f"numero_cas='{self.__numero_cas}', " \
               f"numero_ce='{self.__numero_ce}')"

    def __hash__(self) -> int:
        """Retourne le hash de l'instance.

        Returns
        -------
        int
            Le hash de l'instance.

        """
        return hash(self.__repr__())

    @staticmethod
    def valide_cas(numero_cas: str) -> bool:
        """Vérifie si un numéro CAS donné est valide.

        Parameters
        ----------
        numero_cas : str
            Le numéro CAS à vérifier.

        Returns
        -------
        bool
            True si le numéro CAS est valide, False sinon.

        """
        # Séparation des trois parties du numéro CAS
        parties = numero_cas.split('-')

        # Vérification du nombre de parties
        if len(parties) != 3:
            return False

        # La première partie peut contenir jusqu'à 7 chiffres
        if len(parties[0]) > 7:
            return False

        # La deuxième contient deux chiffres
        if len(parties[1]) != 2:
            return False

        # Calcul de la somme de contrôle
        concat = parties[0] + parties[1]
        checksum = 0
        for i, caractere in enumerate(concat[::-1]):
            checksum += int(caractere) * (i + 1)
        checksum %= 10

        # Vérification du checksum
        return checksum == int(parties[2])

    @staticmethod
    def valide_ce(numero_ce: str) -> bool:
        """Vérifie si un numéro CE donné est valide.

        Parameters
        ----------
        numero_ce : str
            Le numéro CE à vérifier.

        Returns
        -------
        bool
            True si le numéro CE est valide, False sinon.

        """
        # Séparation des trois parties du numéro CE
        parties = numero_ce.split('-')

        # Vérification du nombre de parties
        if len(parties) != 3:
            return False

        # Les longueurs des parties sont [3, 3, 1]
        longueurs = [3, 3, 1]
        for i, partie in enumerate(parties):
            if len(partie) != longueurs[i]:
                return False

        # Calcul de la somme de contrôle
        concat = parties[0] + parties[1]
        checksum = 0
        for i, caractere in enumerate(concat):
            checksum += int(caractere) * (i + 1)
        checksum %= 11

        # Vérification du checksum
        return checksum == int(parties[2])
