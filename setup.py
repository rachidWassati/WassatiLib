from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='WassatiLib',
    version='1.0.0',
    packages=find_packages(),  # Recherche automatique des packages dans le répertoire du projet
    install_requires= requirements,
    # entry_points={
    #     'console_scripts': [
    #         'mon_script = mon_projet.script:main',  # Exemple de script exécutable
    #     ],
    # },
    author='Rachid Jeffali',
    author_email='rachid.jeffali@gmail.com',
    description='Cette librairie apporte un certains nombre de fonctions afin de faciliter le développement des produits Aligning et Anticipating',
    url='https://github.com/rachidWassati/WassatiLib',
)
