from livre_s17 import Livre


def trier_par_titre(livres):
    return sorted(livres, key=lambda livre: livre.titre)


def trier_par_auteur_puis_titre(livres):
    return sorted(livres, key=lambda livre: (livre.auteur, livre.titre))


def trier_par_annee(livres, recents_dabord=False):
    return sorted(livres, key=lambda livre: livre.annee,
                  reverse=recents_dabord)


def trier_par_auteur_puis_annee_recente(livres):
    return sorted(livres,
                  key=lambda livre: (livre.auteur, -livre.annee))


def rechercher_par_auteur(livres, auteur):
    return [livre for livre in livres if livre.auteur == auteur]


def rechercher_par_isbn(livres, isbn):
    for livre in livres:
        if livre.isbn == isbn:
            return livre
    return None


def compter_distincts(livres):
    return len(set(livres))


def dedoublonner(livres):
    return list(dict.fromkeys(livres))


def indexer_par_isbn(livres):
    return {livre.isbn: livre for livre in livres}


def regrouper_par_auteur(livres):
    groupes = {}

    for livre in livres:
        groupes.setdefault(livre.auteur, []).append(livre)

    return groupes