class Livre:
    def __init__(self, titre, auteur, isbn, pages, annee):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.pages = pages
        self.annee = annee

    def __eq__(self, other):
        if not isinstance(other, Livre):
            return False
        return self.isbn == other.isbn

    def __hash__(self):
        return hash(self.isbn)

    def __repr__(self):
        return f"Livre({self.titre!r}, {self.auteur!r}, {self.isbn!r})"
