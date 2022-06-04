from datetime import datetime
import os
import pandas as pd 
import csv

def getCurrentDate(listData: list) -> str:
    '''
    Cette fonction renvoit la date d'aujourd'hui avec plusieurs possibilités:
    YYYYMMDD ou YYYYMM ou YYYYDD ou MMDD en fonction des arguments passés dans une liste
        Parameters:
        -----------
            listData (list): doit contenir les éléments 'year', 'month' ou 'day'
        Returns:
        --------
            date (str): la date d'aujourd'hui avec le format souhaité
    '''
    listData = [element.lower() for element in listData]
    currentDate =''

    if 'year' in listData:
        currentDate += str(datetime.now().year)

    if 'month' in listData:
        currentDate += str(datetime.now().month)

    if 'day' in listData:
        currentDate += str(datetime.now().day)

    return currentDate


def writeToCsv(path_file: str, dico: dict, list_columns: list) -> None:
    '''
    Fonction qui va ecrire dans un fichier csv les données passées sous forme de dictionnaire
        Parameters:
        -----------
            path_file (str): chemin du fichier csv
            dico (dict): dictionnaire a ecrire dans le csv
            list_columns (list): liste des colonnes a faire coincider avec les fieldnames du csv
        Returns:
        --------
            None
    '''
    if not isinstance(path_file, str):
        raise TypeError(f"Le chemin du fichier doit être de type 'str' et non pas '{type(path_file)}'.")
    if not path_file.endswith('.csv'):
        raise ValueError(f"Le fichier doit etre de format 'CSV'")
    if not isinstance(dico, dict):
        raise TypeError(f"Le paramètre dico doit être de type 'dict' et non pas '{type(dico)}'.")
    if not isinstance(list_columns, list):
        raise TypeError(f"list_columns doit être de type 'list' et non pas '{type(list_columns)}'.")
    with open(path_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list_columns)
        writer.writerow(dico)


def cleanDf(path_file: str, columns: list) -> None:
    '''
    Fonction qui va nettoyer un csv des doublons en se basant sur une liste de colonnes comme subset
        Parameters:
        -----------
            path_file (str): chemin qui mene au fichier csv
            columns (list): liste des colonnes a prendre en compte pour le drop_duplicates
        Returns:
        --------
            None
    '''
    if not isinstance(path_file, str):
        raise TypeError(f"Le chemin du fichier doit être de type 'str' et non pas '{type(path_file)}'.")
    if not path_file.endswith('.csv'):
        raise ValueError(f"Le fichier doit etre de format 'CSV'")
    if not isinstance(columns, list):
        raise TypeError(f"'columns' doit être de type 'list' et non pas '{type(columns)}'.")
    df = pd.read_csv(path_file)
    df = df.drop_duplicates(subset=columns)
    df.to_csv(path_file, index=False)


def initiateCsvFile(csvFilePath: str, list_columns: list) -> bool:
    '''
    Fonction qui va initialiser un fichier csv vide avec la liste des colonnes voulues
        Parameters:
        -----------
            csvFilePath (str): chemin qui mene au fichier csv
            list_columns (list): liste des colonnes a mettre dans le csv
        Returns:
        --------
            (bool) True si tout c'est bien passé sinon False
    '''
    if not isinstance(csvFilePath, str):
        raise TypeError(f"Le chemin du fichier doit être de type 'str' et non pas '{type(csvFilePath)}'.")
    if not csvFilePath.endswith('.csv'):
        raise ValueError(f"Le fichier doit etre de format 'CSV'")
    if not isinstance(list_columns, list):
        raise TypeError(f"list_columns doit être de type 'list' et non pas '{type(list_columns)}'.")
    if not os.path.isfile(csvFilePath):
        df = pd.DataFrame(columns=list_columns)
        df.to_csv(csvFilePath, index=False)
        return True
    else:
        return False

def diffList(list1: list, list2: list) -> list:
    '''
    Fonction qui renvoie la difference entre deux listes
        Parameters:
        -----------
            list1 (list): Première liste
            list2 (list): Deuxième liste
        Returns:
        --------
            (list) contenant seulement la différence entre les deux listes
    '''
    return list(set(list1).symmetric_difference(set(list2)))