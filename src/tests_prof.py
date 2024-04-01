# Imports
from carburant import Carburant
from pompe import Pompe
from station import Station
from substance_chimique import SubstanceChimique

# SubstanceChimique - attributs
gazole = SubstanceChimique(
    nom='gazole', 
    numero_cas='68476-34-6', 
    numero_ce='270-676-1'
)

substance_chimique_attr = (
    'nom', 
    '_SubstanceChimique__numero_cas', 
    '_SubstanceChimique__numero_ce'
)

for attribut in substance_chimique_attr:
    assert hasattr(gazole, attribut)
    assert not callable(getattr(gazole, attribut))

# SubstanceChimique - méthodes
substance_chimique_meth = ('__init__', '__eq__', '__repr__', '__hash__')

for method in substance_chimique_meth:
    assert hasattr(SubstanceChimique, method)
    assert callable(getattr(SubstanceChimique, method))

# Carburant - attributs
gazole_carburant = Carburant(
    nom='Gazole', 
    composition_chimique={gazole: 1.0}
)

carburant_attr = (
    'nom', 
    'composition_chimique'
)

for attribut in carburant_attr:
    assert hasattr(gazole_carburant, attribut)
    assert not callable(getattr(gazole_carburant, attribut))

# Carburant - méthodes
carburant_meth = ('__init__',)

for method in carburant_meth:
    assert hasattr(Carburant, method)
    assert callable(getattr(Carburant, method))

# Pompe - attributs
gazole_pompe = Pompe(
    carburant=gazole_carburant, 
    volume_maximal=4_000, 
    volume_disponible=3_200
)

pompe_attr = (
    'carburant', 
    '_Pompe__volume_maximal', 
    '_Pompe__volume_disponible'
)

for attribut in pompe_attr:
    assert hasattr(gazole_pompe, attribut)
    assert not callable(getattr(gazole_pompe, attribut))

# Pompe - méthodes
pompe_meth = ('__init__', '_vide', '_remplir', '_servir')

for method in pompe_meth:
    assert hasattr(Pompe, method)
    assert callable(getattr(Pompe, method))

# Station - attributs
station = Station(
    pompes={'gazole': gazole_pompe}, 
    prix={'gazole': 1.799}
)

station_attr = (
    'pompes', 
    'prix'
)

for attribut in station_attr:
    assert hasattr(station, attribut)
    assert not callable(getattr(station, attribut))

# Station - méthodes
station_meth = (
    '__init__', 
    '_Station__verifier_nom_carburant',
    '_Station__verifier_pompe', 
    '_mettre_a_jour_prix',
    '_remplir_pompe', 
    'servir'
)

for method in station_meth:
    assert hasattr(Station, method)
    assert callable(getattr(Station, method))
