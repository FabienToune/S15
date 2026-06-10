from unittest import TestCase, main
from mode_livraison import (
    ModeLivraison,
    LivraisonStandard, 
    LivraisonExpress,
    PointRelais,
    RetraitMagasin,
    comparer_livraisons
)

class LivraisonErreur(ModeLivraison):    
    def delai_estime(self):
        return 2


class TestContrat(TestCase):
   
    def test_sous_classe_incomplete(self):
        with self.assertRaises(TypeError):
            LivraisonErreur()
        
    
class TestCout(TestCase):
    
    def test_valeur_attendues(self):
        self.assertEqual(LivraisonStandard().cout(2.0), 7.99)
    
    def test_validation_du_poids_typeError(self):
        with self.assertRaises(TypeError):
            ModeLivraison._valider_poids("f")
    
    def test_validation_du_poids_ValueError(self):
        with self.assertRaises(ValueError):
            ModeLivraison._valider_poids(0)


class TestDelai(TestCase):

    def test_LivraisonStandard(self):
        self.assertEqual(LivraisonStandard().delai_estime(), 3)
    
    def test_LivraisonExpress(self):
        self.assertEqual(LivraisonExpress().delai_estime(), 1)
    
    def test_PointRelais(self):
        self.assertEqual(PointRelais("RelaisColis").delai_estime(), 4)


class TestEtatConfigurable(TestCase):

    def test_supplement_lecture_seul(self):
        with self.assertRaises(AttributeError):
            LivraisonExpress().supplement = 20
    
    def test_nom_reseau_lecture_seul(self): 
        with self.assertRaises(AttributeError):
            PointRelais("nom").nom_reseau = "test"

    def test_supplement_negatif(self):
        with self.assertRaises(ValueError):
            LivraisonExpress(-1)

    def test_nom_reseau_vide(self): 
        with self.assertRaises(ValueError):
            PointRelais(" ")


class TestPolymorphisme(TestCase):
    
#  LivraisonStandard : 8.74 EUR en 3 jour(s)
# LivraisonExpress : 20.74 EUR en 1 jour(s)
# PointRelais : 3.50 EUR en 4 jour(s)
    # , LivraisonExpress(), PointRelais("Relais")
    # \nLivraisonExpress : 18.74 EUR en 1 jour(s)\n PointRelais : 3.50 EUR en 4 jour(s)
    def test_comparer_livraisons_sur_les_trois_sous_classe(self):
        modes = [LivraisonStandard(), LivraisonExpress(), PointRelais("RelaisColis")]
        chaine = "LivraisonStandard : 8.74 EUR en 3 jour(s)\nLivraisonExpress : 18.74 EUR en 1 jour(s)\nPointRelais : 3.50 EUR en 4 jour(s)"
        self.assertEqual(comparer_livraisons(modes, 2.5),chaine )


class TestDuckTyping(TestCase):
    def test_RetraitMagasin_accepte_par_comparer_livraison(self):
        modes = [LivraisonStandard(), LivraisonExpress(), PointRelais("RelaisColis"), RetraitMagasin()]
        chaine = "LivraisonStandard : 8.74 EUR en 3 jour(s)\nLivraisonExpress : 18.74 EUR en 1 jour(s)\nPointRelais : 3.50 EUR en 4 jour(s)\nRetraitMagasin : 0.00 EUR en 0 jour(s)"
        self.assertEqual(comparer_livraisons(modes, 2.5),chaine )

    def test_pas_un_mode_livraison(self):
        self.assertNotIsInstance(RetraitMagasin, ModeLivraison)

if __name__ == "__main__":
    main()