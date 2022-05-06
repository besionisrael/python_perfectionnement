
class Rectangle:
    '''Classe de rectangles'''
    def __init__(self, longueur  = 0, largeur = 0):
        self.L = longueur
        self.l = largeur
        self.nom = "Rectangle"
    
    def perimetre(self):
        return (self.L + self.l)*2
    
    def surface(self):
        return self.L * self.L

    def mesures(self):
        print(f'Un {self.nom} de Longueur {self.L} et de largeur {self.l}')
        print(f"a une surface de {self.surface()}")
        print(f" et un perimètre de {self.perimetre()}")

class Carre(Rectangle):
    '''Classe de carrés'''
    domaine = "Geometrie"
    def __init__(self, cote): 
        Rectangle.__init__(self, cote, cote) 
        #super().__init__(cote, cote)
        self.nom = "Carré"
    
    def mesures(self):
        super().mesures()
        print(f"un {self.nom} de Coté de {self.L}")
    
    @classmethod
    def carre_unitaire(cls):
            return cls(cote = 1)
        
    @staticmethod
    def affiche_domaine():
        print(f"Champ concerné: {Carre.domaine}")

#Property
class House:

	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Entrez une valeur valide")

	@price.deleter
	def price(self):
		del self._price


r1 = Rectangle(10, 4)
r2 = Rectangle(40,4)
c1 = Carre(15)
Carre.carre_unitaire()
Carre.affiche_domaine()


