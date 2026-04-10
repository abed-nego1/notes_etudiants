etudiants = []
def ajouter_etudiants(nom, note):
	etudiants.append({"nom": nom, "note": note})
	print(f"Etudiant {nom} ajouté avec la note {note}.")

def calcul_moyenne():
	if not etuidants:
	print ("Aucun étudiants enregistré.")
	return 0
     total= sul(e['note'] for e in entudiants)
	moyenne= total/len(etudiants)
	print(f"Moyenne de la classe :{moyenne:.2f}")
	return moyenne
