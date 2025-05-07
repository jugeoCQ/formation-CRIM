from IPython.display import display, HTML
import numpy as np

_tentatives = {}

# --- MESSAGES STYLISÉS ---

def afficher_message(titre, texte, couleur_bordure, couleur_fond, couleur_titre):
    html = f'''
    <div style="border-left: 6px solid {couleur_bordure}; background-color: {couleur_fond};
                padding: 10px 20px; border-radius: 6px; margin: 10px 0;">
        <h4 style="color: {couleur_titre}; margin: 0;">{titre}</h4>
        <p style="margin: 0; color: #000000;">{texte}</p>
    </div>'''
    display(HTML(html))

def message_succes(titre="✅ Réussi", texte="Bonne réponse !"):
    afficher_message(titre, texte, "#4CAF50", "#e8f5e9", "#2e7d32")

def message_erreur(titre="❌ Erreur", texte="La réponse est incorrecte."):
    afficher_message(titre, texte, "#f44336", "#ffebee", "#c62828")

def message_attention(titre="⚠️ Attention", texte="Vérifiez votre réponse."):
    afficher_message(titre, texte, "#ff9800", "#fff3e0", "#ef6c00")

def message_info(titre="ℹ️ Info", texte="Voici une information utile."):
    afficher_message(titre, texte, "#2196F3", "#e3f2fd", "#1565c0")

# --- CORRECTION AUTOMATISÉE ---

def comparer(val1, val2, tol):
        if isinstance(val1, (float, int)) and isinstance(val2, (float, int)):
            return abs(val1 - val2) < tol
        if isinstance(val1, (list, tuple)) and isinstance(val2, (list, tuple)):
            return len(val1) == len(val2) and all(comparer(v1, v2,tol) for v1, v2 in zip(val1, val2))
        if isinstance(val1, dict) and isinstance(val2, dict):
            return val1.keys() == val2.keys() and all(comparer(val1[k], val2[k],tol) for k in val1)
        if isinstance(val1, np.ndarray) and isinstance(val2, np.ndarray):
            if val1.shape != val2.shape:
                return False
            return np.allclose(val1, val2, atol=tol)
        if isinstance(val1,np.ndarray) and isinstance(val2, np.ndarray):
            return np.allclose(val1, val2, atol=tol)
        return val1 == val2

def corriger_une_reponse(reponse, attendu, nom_exo="Exercice", tol=1e-6, max_essais=3, info=None):
    global _tentatives
    identifiant = nom_exo
    _tentatives[identifiant] = _tentatives.get(identifiant, 0) + 1

    correct = comparer(reponse, attendu,tol)

    if correct:
        message_succes(f"✅ {nom_exo}", "Bonne réponse !")
        reset_tentatives(identifiant)
    else:
        message_erreur(f"❌ {nom_exo}", f"Mauvaise réponse.<br><strong>Attendu :</strong> {attendu}<br><strong>Obtenu :</strong> {reponse}")
        if _tentatives[identifiant] >= max_essais and info:
            message_info(f"ℹ️ {nom_exo}", info)

# --- RÉINITIALISATION ---

def reset_tentatives(nom_exo=None):
    global _tentatives
    if nom_exo:
        _tentatives[nom_exo] = 0
    else:
        _tentatives.clear()

def correction_multiple(fonction, cas_de_test, nom_exo="Exercice", tol=1e-6, info=None):
    """
    Teste une fonction avec plusieurs cas de test et affiche les succès et échecs dans une seule boîte.

    :param fonction: La fonction à tester.
    :param cas_de_test: Une liste de tuples (entrée, attendu) où 'entrée' est un tuple des arguments
                        à passer à la fonction et 'attendu' est le résultat attendu.
    """
    global _tentatives
    identifiant = nom_exo
    _tentatives[identifiant] = _tentatives.get(identifiant, 0) + 1
    max_essais = 3
    resultats = []
    tous_reussis = True
    for i, (entree, attendu) in enumerate(cas_de_test, 1):
        try:
            resultat = fonction(entree)
            if comparer(resultat, attendu, tol):
                resultats.append((i, entree, resultat, attendu, "succès"))
            else:
                resultats.append((i, entree, resultat, attendu, "échec"))
                tous_reussis = False
        except Exception as e:
            if type(resultat) != type(attendu):
                resultats.append((i, entree, resultat, attendu, "type erreur"))
            else:
                resultats.append((i, entree, str(e), attendu, "erreur"))
            tous_reussis = False

    # Construire le message combiné
    contenu = ""
    for i, entree, resultat, attendu, statut in resultats:
        if statut == "succès":
            contenu += f"<p style='color: #2e7d32;'>✅ Test {i} : Entrée : {entree} | Résultat : {resultat} | Attendu : {attendu}</p>"
        elif statut == "échec":
            contenu += f"<p style='color: #c62828;'>❌ Test {i} : Entrée : {entree} | Résultat : {resultat} | Attendu : {attendu}</p>"
        elif statut == "erreur":
            contenu += f"<p style='color: #c62828;'>❌ Test {i} : Entrée : {entree} | Erreur : {resultat}</p>"
        elif statut == "type erreur":
            contenu += f"<p style='color: #c62828;'>❌ Test {i} : Entrée : {entree} | Type attendu : {type(attendu).__name__}, Type obtenu : {type(resultat).__name__}</p>"

    if tous_reussis:
        afficher_message("✅ Bonne réponse !", contenu, "#4CAF50", "#e8f5e9", "#2e7d32")
        reset_tentatives(identifiant)
    else:
        afficher_message("❌ Certains tests ont échoué", contenu, "#f44336", "#ffebee", "#c62828")
        if _tentatives[identifiant] >= max_essais and info:
            message_info(f"ℹ️ {nom_exo}", info)