import pytest
from substance_chimique import SubstanceChimique


def test_creation_valid(gazole_kwargs):
    gazole = SubstanceChimique(**gazole_kwargs)
    assert gazole.nom == gazole_kwargs['nom']
    expected_repr = "SubstanceChimique(nom='" + gazole_kwargs['nom'] + "', " \
                    "numero_cas='" + gazole_kwargs['numero_cas'] + "', " \
                    "numero_ce='" + gazole_kwargs['numero_ce'] + "')"
    assert repr(gazole) == expected_repr


def test_equality(butane_kwargs, ethanol_kwargs):
    butane = SubstanceChimique(**butane_kwargs)
    ethanol = SubstanceChimique(**ethanol_kwargs)
    assert butane != ethanol


def test_repr(butane_kwargs):
    butane = SubstanceChimique(**butane_kwargs)
    expected_repr = "SubstanceChimique(nom='" + butane_kwargs['nom'] + "', " \
                    "numero_cas='" + butane_kwargs['numero_cas'] + "', " \
                    "numero_ce='" + butane_kwargs['numero_ce'] + "')"
    assert repr(butane) == expected_repr


@pytest.mark.parametrize("numero_cas, expected", [
     ("50-00-0", True),
     ("1234567-89-0", False),  # Numéro trop long
     ("123-45-67", False),  # Checksum invalide
])
def test_valide_cas(numero_cas, expected):
    assert SubstanceChimique.valide_cas(numero_cas) == expected


@pytest.mark.parametrize("numero_ce, expected", [
     ("200-578-6", True),
     ("203-448-7", True),
     ("123-456-8", False),  # Checksum invalide
     ("12-3456-7", False),  # Format invalide
])
def test_valide_ce(numero_ce, expected):
    assert SubstanceChimique.valide_ce(numero_ce) == expected


def test_incorrect_type():
    with pytest.raises(TypeError):
        SubstanceChimique(123, '123-45-6', '200-578-6')  # Nom non-string


def test_incorrect_cas(gazole_kwargs):
    gazole_kwargs['numero_cas'] = 'invalid'
    with pytest.raises(ValueError):
        SubstanceChimique(**gazole_kwargs)


def test_incorrect_ce(gazole_kwargs):
    gazole_kwargs['numero_ce'] = 'invalid'
    with pytest.raises(ValueError):
        SubstanceChimique(**gazole_kwargs)
