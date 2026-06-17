# VENV
## Créer un environement virtuel python
```
python -m venv venv_name
```
## Activer l'environement virtuel python
```
source venv_name/bin/activate
```
## Désactiver l'environement virtuel python
```
deactivate
```
## Vérifier l'environement virtuel python
```
which python
```
---
# PIP
## Utilisation de pip --requirement
**pip install --requirement requirements.txt**  
**pip install -r requirements.txt**  
*requirements.txt*  
```
package_1
package_2==1.2.3
package_3>=4.5.6
package_4~=3.4.0
```
- Sans version : Installe la dernière version disponible.  
- == : Version exacte.  
- >= : Version minimale.  
- ~= : Version compatible (ex: ~=1.24.0 permet 1.24.x mais pas 1.25.0).  
## Générer un fichier requirements.txt
```
pip freeze > requirements.txt
```
---
# POETRY
## Générer un fichier pyproject.toml dans un projet existant
**poetry init**  
## Créer un nouveau projet
**poetry new nom_projet**
Cette commande va créer :  
```
nom_projet/
├── pyproject.toml
├── README.md
├── src/
│   └── nom_projet/
│       └── __init__.py
└── tests/
```
## Ajouter des dépendances
**poetry add dependance_1 dependance_2 ...**  
**poetry add "dependance>=2,<3"** *avec N° de version*  
## Ajouter des dépendances de développement
**poetry add --group dev pytest mypy**  
## Installer les dépendances
**poetry install**  
