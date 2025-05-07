from autocorrecteur.correction import corriger_une_reponse
import numpy as np

def correction_exercice1(reponse):
    """
    Correction de l'exercice 1 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = {'0000': np.array(500), '1111': np.array(500)}

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 1", tol=15, max_essais=3, info="Révisez la simulation du qubit.")

