from autocorrecteur.correction import corriger_une_reponse, correction_multiple
import numpy as np

def correction_exercice1(reponse):
    """
    Correction de l'exercice 1 : Simulation d'un qubit.
    """
    # Réponse attendue
    tol = 15
    attendu = {'010': np.array(1000)}
    if isinstance(reponse, np.ndarray):
        tol = 0.015
        attendu = np.array([0.,0.,1.,0.,0.,0.,0.,0.])

    # Appel de la fonction de correction
    corriger_une_reponse(reponse, attendu, nom_exo="Exercice 1", tol=tol, max_essais=3, info="Révisez la simulation du qubit.")

def correction_fonction(func):
    """
    Correction de la fonction de simulation d'un qubit.
    """
    # Réponse attendue
    result = func('000')
    if isinstance(result, dict) and all(isinstance(v, np.ndarray) for v in result.values()):
        cas_de_test = [('000', {'000': np.array(1000)}), 
                    ('001', {'001': np.array(1000)}), 
                    ('010', {'010': np.array(1000)}),
                    ('011', {'011': np.array(1000)}),
                    ('100', {'100': np.array(1000)}), 
                    ('101', {'101': np.array(1000)}),
                    ('110', {'110': np.array(1000)}),
                    ('111', {'111': np.array(1000)})]
    else:
        cas_de_test = [('000', np.array([1.,0.,0.,0.,0.,0.,0.,0.])), 
                ('001', np.array([0.,1.,0.,0.,0.,0.,0.,0.])), 
                ('010', np.array([0.,0.,1.,0.,0.,0.,0.,0.])),
                ('011', np.array([0.,0.,0.,1.,0.,0.,0.,0.])),
                ('100', np.array([0.,0.,0.,0.,1.,0.,0.,0.])), 
                ('101', np.array([0.,0.,0.,0.,0.,1.,0.,0.])),
                ('110', np.array([0.,0.,0.,0.,0.,0.,1.,0.])),
                ('111', np.array([0.,0.,0.,0.,0.,0.,0.,1.]))]
    
    correction_multiple(func, cas_de_test, nom_exo="Exercice 1", tol=1e-6)
    # Appel de la fonction de correction
    # corriger_une_reponse(func, attendu, nom_exo="Fonction de simulation", tol=1e-6, max_essais=3, info="Révisez la simulation du qubit.")

