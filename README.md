# Librairie Python
Librairie Python pour les divers projets menés au sein de Wassati

## Installation
Mettre le dossier WassatiLib dans le dossier environnement Anaconda ou Miniconda créé

## Usage
```python
from WassatiLib.getArguments.parser import parser

args = parser(f = 'filePath', o = 'outputFIle')
```

## Liste de fonctions
- getCurrentDate: fonction qui renvoit la current date, elle reçoit en paramètres une liste ['day', 'month', 'year'] avec la possibilité de choisir les éléments souhaités
- 