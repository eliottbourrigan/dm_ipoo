import pytest
from substance_chimique import SubstanceChimique
from carburant import Carburant


@pytest.mark.parametrize("nom, composition, expected_exception", [
    # Cas de test avec somme des proportions différente de 1
    ("SP95", {SubstanceChimique(
            nom='octane', numero_cas='111-65-9',
            numero_ce='203-892-1'): 0.90,
        SubstanceChimique(
            nom='heptane', numero_cas='142-82-5',
            numero_ce='205-563-8'): 0.05}, ValueError),
    # Cas de test avec proportion négative
    ("SP95", {SubstanceChimique(
            nom='octane', numero_cas='111-65-9',
            numero_ce='203-892-1'): -0.95,
        SubstanceChimique(
            nom='heptane', numero_cas='142-82-5',
            numero_ce='205-563-8'): 1.95}, ValueError),
    # Cas de test valide
    ("SP95", {SubstanceChimique(
            nom='octane', numero_cas='111-65-9',
            numero_ce='203-892-1'): 0.95,
        SubstanceChimique(
            nom='heptane', numero_cas='142-82-5',
            numero_ce='205-563-8'): 0.05}, None),
])
def test_carburant_composition(nom, composition, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            Carburant(nom, composition)
    else:
        carburant = Carburant(nom, composition)
        assert carburant.nom == nom
        assert carburant.composition_chimique == composition
        total_proportion = sum(composition.values())
        assert total_proportion == 1, \
            "La somme des proportions doit être égale à 1"


def test_carburant_nom_incorrect_type():
    with pytest.raises(TypeError):
        Carburant(123, {SubstanceChimique(
            nom='butane', numero_cas='106-97-8', numero_ce='203-448-7'): 1.0})


def test_carburant_composition_incorrect_type(sp95_kwargs):
    with pytest.raises(TypeError):
        Carburant(sp95_kwargs['nom'], "ceci n'est pas un dictionnaire")
