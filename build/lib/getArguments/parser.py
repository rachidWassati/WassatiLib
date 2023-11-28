import argparse

def parser(**kwargs):
    """
    Cette fonction construit un parser customisé, pour des options des lignes de commandes.

    Args:
        kwargs (list): la liste des arguments pour le parser

    Returns:
        dict: paire de clés-valeurs avec pour chaque argument la valeur associé saisi dans la ligne de commande
    """
    parser = argparse.ArgumentParser()
    for key, value in kwargs.items():
        parser.add_argument(f'-{key}', f'--{value}', required= True)

    return vars(parser.parse_args())
