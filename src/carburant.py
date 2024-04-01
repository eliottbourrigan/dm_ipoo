from substance_chimique import SubstanceChimique


class Carburant:
    """ Représente un carburant.

    Attributes
    ----------
    nom : str
        Le nom du carburant.
    composition_chimique : dict[SubstanceChimique, float]
        La composition chimique du carburant.

    Examples
    --------
    >>> butane = SubstanceChimique(
    ...     nom='butane', numero_cas='106-97-8', numero_ce='203-448-7')
    >>> propane = SubstanceChimique(
    ...     nom='propane', numero_cas='74-98-6', numero_ce='200-827-9')
    >>> carburant = Carburant(
    ...     nom='SP95', composition_chimique={butane: 0.95, propane: 0.05})

    """
    def __init__(
            self, nom: str,
            composition_chimique: dict[SubstanceChimique, float]):
        """Initialise un carburant.

        Parameters
        ----------
        nom : str
            Le nom du carburant.
        composition_chimique : dict[SubstanceChimique, float]
            La composition chimique du carburant.

        """
        # Vérification des types des arguments
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être de type 'str'.")
        if not isinstance(composition_chimique, dict):
            raise TypeError("La composition chimique doit être un 'dict'.")

        # Vérification de la somme des proportions
        proportions = composition_chimique.values()
        if not sum(proportions) == 1:
            raise ValueError("La somme des proportions doit être égale à 1.")

        # Les proportions doivent être supérieures à 0
        if not all(proportion > 0 for proportion in proportions):
            raise ValueError("Les proportions doivent être > 0.")

        # Assignation des attributs
        self.nom = nom
        self.composition_chimique = composition_chimique
