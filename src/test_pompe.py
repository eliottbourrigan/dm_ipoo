import pytest
from carburant import Carburant
from pompe import Pompe
from substance_chimique import SubstanceChimique


# Fixture pour créer un carburant de test
@pytest.fixture
def carburant_test():
    butane = SubstanceChimique(
        nom='butane', numero_cas='106-97-8', numero_ce='203-448-7')
    propane = SubstanceChimique(
        nom='propane', numero_cas='74-98-6', numero_ce='200-827-9')
    return Carburant(
        nom='SP95', composition_chimique={butane: 0.95, propane: 0.05})


@pytest.fixture
def pompe_test(carburant_test):
    return Pompe(
        carburant=carburant_test, volume_maximal=10, volume_disponible=5)


def test_pompe_initialisation(carburant_test):
    pompe = Pompe(
        carburant=carburant_test, volume_maximal=10, volume_disponible=5)
    assert not pompe._vide(), \
        "La pompe ne devrait pas être vide après " + \
        "initialisation avec du volume disponible."


def test_mauvais_types_initialisation_pompe(carburant_test):
    with pytest.raises(TypeError):
        Pompe(
            carburant=carburant_test,
            volume_maximal=10,
            volume_disponible='5'), \
                "Le volume disponible doit être de type 'int'."
    with pytest.raises(TypeError):
        Pompe(
            carburant=carburant_test,
            volume_maximal='10',
            volume_disponible=5), \
                "Le volume maximal doit être de type 'int'."
    with pytest.raises(TypeError):
        Pompe(
            carburant='SP95',
            volume_maximal=10,
            volume_disponible=5), \
                "Le carburant doit être de type 'Carburant'."


def test_pompe_vide_apres_service(pompe_test):
    volume_servi = pompe_test._servir(5)
    assert volume_servi == 5, "Le volume servi doit être de 5."
    assert pompe_test._vide(), \
        "La pompe devrait être vide après avoir servi " + \
        "tout le volume disponible."


def test_pompe_remplir(pompe_test):
    pompe_test._remplir(5)
    assert not pompe_test._vide(), \
        "La pompe ne devrait pas être " + \
        "vide après avoir été remplie."


def test_pompe_servir_plus_que_disponible(pompe_test):
    volume_servi = pompe_test._servir(10)
    assert volume_servi == 5, \
        "Le volume servi ne devrait " + \
        "pas dépasser le volume disponible."


def test_pompe_servir_volume_negatif(pompe_test):
    with pytest.raises(ValueError):
        pompe_test._servir(-1), \
            "Un volume négatif à servir " + \
            "devrait lever une ValueError."


def test_pompe_remplir_volume_negatif(pompe_test):
    with pytest.raises(ValueError):
        pompe_test._remplir(-1), \
            "Un volume négatif à remplir devrait lever une ValueError."


def test_pompe_initialisation_volume_maximal_incorrect(carburant_test):
    with pytest.raises(ValueError):
        Pompe(
            carburant=carburant_test,
            volume_maximal=-10,
            volume_disponible=5), \
                "Un volume maximal négatif devrait lever une ValueError."


def test_pompe_initialisation_volume_disponible_incorrect(carburant_test):
    with pytest.raises(ValueError):
        Pompe(
            carburant=carburant_test,
            volume_maximal=10,
            volume_disponible=11), \
                "Un volume disponible supérieur au volume " + \
                "maximal devrait lever une ValueError."
