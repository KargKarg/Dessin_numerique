import numpy as np


def tab_data(nom):

    """Fonction qui crée un array avec les données du txt"""

    tableau = np.loadtxt(nom)
    return tableau
