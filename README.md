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
