import pytest
from pompe import Pompe
from carburant import Carburant
from substance_chimique import SubstanceChimique
from station import Station


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


@pytest.fixture
def station_test(pompe_test):
    return Station(pompes={'SP95': pompe_test}, prix={'SP95': 2.0})


def test_station_initialisation(station_test):
    assert 'SP95' in station_test.pompes, \
        "La pompe SP95 doit être présente dans la station."
    assert station_test.prix['SP95'] == 2.0, \
        "Le prix de SP95 doit être de 2.0."


def test_station_servir(station_test):
    station_test.servir('SP95', 3)
    assert not station_test.pompes['SP95']._vide(), \
        "La pompe ne devrait pas être vide après avoir servi 3 unités."


def test_station_remplir_pompe_sans_changement_prix(station_test):
    station_test._remplir_pompe('SP95', 5)
    assert station_test.prix['SP95'] == 2.0, \
        "Le prix de SP95 devrait rester à 2.0 sans changement spécifié."


def test_station_mettre_a_jour_prix_sans_changement_volume(station_test):
    station_test._mettre_a_jour_prix('SP95', 2.5)
    assert station_test.prix['SP95'] == 2.5, \
        "Le prix de SP95 devrait être mis à jour à 2.5."


def test_station_servir_pompe_vide(station_test):
    station_test.servir('SP95', 5)  # Vide la pompe
    with pytest.raises(ValueError):
        station_test.servir('SP95', 1), \
            "Servir depuis une pompe vide devrait lever une ValueError."


def test_station_erreur_nom_carburant(station_test):
    with pytest.raises(ValueError):
        station_test.servir('SP98', 3), \
            "Servir un carburant non existant devrait lever une ValueError."


def test_mauvais_types_initialisation(pompe_test):
    with pytest.raises(TypeError):
        Station(pompes=1, prix={'SP95': 2.0})
    with pytest.raises(TypeError):
        Station(pompes={'SP95': pompe_test}, prix=1)


def test_prix_negatifs(pompte_test):
    with pytest.raises(ValueError):
        Station(pompes={'SP95': pompe_test}, prix={'SP95': -2.0})


def test_clefs_non_identiques(pompe_test):
    with pytest.raises(ValueError):
        Station(pompes={'SP95': pompe_test}, prix={'SP98': 2.0})


def test_verifier_pompe_inexistante(station_test):
    with pytest.raises(ValueError):
        station_test.__verifier_pompe('SP98')


def test_mettre_a_jour_prix_negatif(station_test):
    with pytest.raises(ValueError):
        station_test._mettre_a_jour_prix('SP95', -1)


def test_mettre_a_jour_prix_pompe_vide(station_test):
    station_test.servir('SP95', 5)  # Assurez-vous que la pompe est vide
    with pytest.raises(ValueError):
        station_test._mettre_a_jour_prix('SP95', 2.5)


def test_remplir_pompe_vide_sans_nouveau_prix(station_test):
    station_test.servir('SP95', 5)  # Vide la pompe
    with pytest.raises(ValueError):
        station_test._remplir_pompe('SP95', 5, None)


def test_remplir_pompe_non_vide_avec_nouveau_prix(station_test):
    with pytest.raises(ValueError):
        station_test._remplir_pompe('SP95', 5, 3.0)


def test_remplir_pompe_vide_avec_prix_negatif(station_test):
    station_test.servir('SP95', 5)  # Vide la pompe
    with pytest.raises(ValueError):
        station_test._remplir_pompe('SP95', 5, -1)


def test_remplir_pompe_vide_avec_prix_positif(station_test):
    station_test.servir('SP95', 5)  # Vide la pompe
    station_test._remplir_pompe('SP95', 5, 3.0)
    assert station_test.prix['SP95'] == 3.0, \
        "Le prix de SP95 devrait être mis à jour à 3.0."


def test_servir_volume_negatif(station_test):
    with pytest.raises(ValueError):
        station_test.servir('SP95', -1)
