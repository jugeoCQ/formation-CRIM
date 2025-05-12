from autocorrecteur.correction import corriger_une_reponse
import numpy as np

def correction_exercice1(reponse):
    """
    Correction de l'exercice 1 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = np.array([0.70710678+0.j,0.+0.j,0.+0.j,0.70710678+0.j])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 1", tol=0, max_essais=3, info="Révisez la simulation du qubit.")

def correction_exercice2_1(reponse):
    """
    Correction de l'exercice 1 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = np.array([0.70710678+0.j,0.+0.j,0.+0.j,-0.70710678+0.j])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 2.1", tol=0, max_essais=3, info="Révisez la simulation du qubit.")

def correction_exercice2_2(reponse):
    """
    Correction de l'exercice 1 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = np.array([0.+0.j, 0.70710678+0.j, 0.70710678+0.j, 0.+0.j])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 2.2", tol=0, max_essais=3, info="Révisez la simulation du qubit.")

def correction_exercice2_3(reponse):
    """
    Correction de l'exercice 1 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = np.array([0.+0.j, 0.70710678+0.j, -0.70710678+0.j, -0.+0.j])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 2.3", tol=0, max_essais=3, info="Révisez la simulation du qubit.")


def correction_exercice3(reponse):
    """
    Correction de l'exercice 1 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = np.array([0.8660254+0.j,0.-0.5j])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 3", tol=0, max_essais=3, info="Révisez la simulation du qubit.")

def correction_exercice5(reponse):
    """
    Correction de l'exercice 1 : Simulation d'un qubit.
    """
    # Réponse attendue
    attendu = np.array(0.)

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 4", tol=0, max_essais=3, info="Révisez la simulation du qubit.")