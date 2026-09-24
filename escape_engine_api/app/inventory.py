class Inventaire:
	def __init__(self):
		self.objets = []

	def ajouter(self, objet):
		self.objets.append(objet)

	def retirer(self, nom_objet):
		for objet in self.objets:
			if objet.get_nom().lower() == nom_objet.lower():
				self.objets.remove(objet)
				return objet
		return None

	def est_vide(self):
		return not self.objets

	def afficher(self):
		if self.est_vide():
			print("Inventaire vide.")
			return

		print("Inventaire de Gilles")
		for objet in self.objets:
			print(f"- {objet.get_nom()}")

	

