# Partie 2 : inscription.py V2 (prérequis : logique conditionnelle, opérations logiques, exceptions)

#Catégorie d'un inscrit vis à vis de son age

def categories(annee):
    age = 2022 - int(annee)
    if 6 <= age < 12:
        return "Poussin"
    elif 12 <= age < 18:
        return "Cadet"
    elif 18 <= age < 24:
        return "Junior"
    elif 24 <= age < 30:
        return "Semi-pro"
    elif 30 <= age <= 40:
        return "Pro"
    else:
        print(" Non-admis")

#adresse mail automatique

def email(nom,prenom):
    mail = str(prenom[0]+"."+nom+"@baton-rouge.fr")
    return mail

# Gestioin des erreurs : sur le nombre d'inscrit

while True:
    try:
        nbr_inscrit = int(input("Indiquez le nombre de personnes à inscrire \n"))
        break
    except ValueError:
        print("Veuillez saisir un nombre sous forme de chiffres")

liste_nouveaux = []

for i in range(nbr_inscrit):
#Gestioin des erreurs : sur le nom

    while True:
                try:
                    nom = str(input("Veuillez renseigner le nom ? \n"))
                    break
                except ValueError:
                    print("Veuillez renseigner le nom en lettres")

#Gestioin des erreurs : sur le prénom

    while True:
                try:
                    prenom = str(input("Veuillez renseigner le prénom ? \n"))
                    break
                except ValueError:
                    print("Veuillez renseigner le prénom en lettres")

#Gestioin des erreurs : sur l'année de naissance

    while True:
            try:
                annee = int(input("Veuillez renseigner l'année de naissance ? \n"))
                break
            except ValueError:
                print("Veuillez renseigner l'année de naissance en chiffres")

#Liste des inscriptions

    adresse_email = email(nom, prenom)
    categorie = categories(annee)
    liste_nouveaux.append([prenom, nom, adresse_email, categorie])
    print("Nouvel enregistrement")

print("=======================")
print("Liste des inscriptions")
print("=======================")
for i in enumerate(liste_nouveaux):
    print(i)

