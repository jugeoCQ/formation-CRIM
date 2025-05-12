from autocorrecteur.correction import corriger_une_reponse
import numpy as np

def correction_exercice1(reponse):
    """
    Correction de l'exercice 1 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = np.array([0.5+0.j, 0. +0.8660254j])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 1", tol=0, max_essais=3, info="Révisez la simulation du qubit.")

def correction_exercice2(reponse):
    """
    Correction de l'exercice 2 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = np.bool_(True)

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 2", tol=0, max_essais=3, info="Révisez la simulation du qubit.")

def correction_exercice3(reponse):
    """
    Correction de l'exercice 3 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = np.array([0.70710678, 0.70710678])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 3", tol=0, max_essais=3, info="Révisez la simulation du qubit.")

def correction_exercice4(reponse):
    """
    Correction de l'exercice 4 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = [0.5, 0.5]

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 4", tol=1e-6, max_essais=3, info="Révisez la simulation du qubit.")

def correction_exercice5(reponse):
    """
    Correction de l'exercice 5 : Simulation d'un qubit.
    """
    # Réponse attendue
    rounded_rep = {k: int(np.round(v, -2)) for k, v in reponse.items()}
    attendu = {0: 500, 1: 500}

    # Appel de la fonction de correction
    corriger_une_reponse(rounded_rep, attendu, nom_exo="Exercice 5", tol=50, max_essais=3, info="Révisez la simulation du qubit.")