import unittest

from catalogue import *
from livre_s17 import Livre

CATALOGUE = [
    Livre("1984", "Orwell", "9780451524935", 328, 1949),
    Livre("La Ferme des animaux", "Orwell", "9780141036137", 112, 1945),
    Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
    Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
]

class TestCatalogue(unittest.TestCase):

    def test_trier_par_titre(self):
        titres = [l.titre for l in trier_par_titre(CATALOGUE)]
        self.assertEqual(
            titres,
            [
                "1984",
                "Fahrenheit 451",
                "La Ferme des animaux",
                "Le Meilleur des mondes"
            ]
        )

    def test_trier_par_annee(self):
        annees = [l.annee for l in trier_par_annee(CATALOGUE)]
        self.assertEqual(annees, [1932, 1945, 1949, 1953])

    def test_trier_par_annee_inverse(self):
        annees = [l.annee for l in trier_par_annee(CATALOGUE, True)]
        self.assertEqual(annees, [1953, 1949, 1945, 1932])

    def test_non_modification(self):
        copie = CATALOGUE[:]
        trier_par_titre(CATALOGUE)
        self.assertEqual(CATALOGUE, copie)

    def test_rechercher_par_auteur(self):
        self.assertEqual(
            len(rechercher_par_auteur(CATALOGUE, "Orwell")),
            2
        )

    def test_rechercher_par_isbn(self):
        livre = rechercher_par_isbn(
            CATALOGUE,
            "9780451524935"
        )
        self.assertEqual(livre.titre, "1984")

    def test_dedoublonnage(self):
        doublon = Livre(
            "1984 (réédition)",
            "Orwell",
            "9780451524935",
            328,
            1949
        )

        livres = CATALOGUE + [doublon]

        self.assertEqual(compter_distincts(livres), 4)
        self.assertEqual(len(dedoublonner(livres)), 4)

    def test_regrouper(self):
        groupes = regrouper_par_auteur(CATALOGUE)
        self.assertEqual(len(groupes["Orwell"]), 2)

if __name__ == "__main__":
    unittest.main()