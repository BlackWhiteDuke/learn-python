# Yimo Liu
# 30 septembre
# défi 4

# Définir un dictionnaire pour les taux de change entre différent devise
échanger_taux = {
    "usd_cad": 1.36, "usd_euro": 0.95, "usd_peso": 24,
    "cad_usd": 0.74, "cad_euro": 0.7, "cad_peso": 12.81,
    "euro_cad": 1.43, "euro_usd": 1.06, "euro_peso": 18.38,
    "peso_usd": 0.057, "peso_cad": 0.078, "peso_euro": 0.054
}

# Demander à l'utilisateur la devise et le montant qu'il veut choisir
De_devise = input("Sélectionnez le type de devise que vous voulez convertir(cad/usd/euro/peso): ")
À_devise = input("Sélectionnez le type de devise cible(cad/usd/euro/peso): ")
montant = float(input("Entrez le montant que vous voulez convertir: "))

# Générer la clé pour le dictionnaire basé sur les choix de l'utilisateur
key = f"{De_devise}_{À_devise}"

# Calculer le montant converti
convert_montant = montant * échanger_taux[key]

print(f"{montant} {De_devise} converti en {À_devise} équivaut à {convert_montant:.2f}")
