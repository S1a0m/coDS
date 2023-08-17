##################################################################
# Le programme que vous lisez n'est pas encore prêt à être lancé #
# Il nécessite encore des méthodes de cryptage et de décryptage  #
# Qui ne sont pas encore prêt                                    #
##################################################################

from getpass import getpass
import re
import hashlib
import json
import datetime
from pathlib import Path
import shutil

print("""
 *********BIENVENUE**************************************************************************
**********************************************************************************************
                                          DDDDDDDDDD                                        **
                                          DDDDDDDDDDD                                       **
                                          DDDD    DDDD                                      **
                                          DDDD     DDDD         SSSSSSSSSSSSSSSS            **
       cccccccccccc      oooooooooooo     DDDD      DDDD       SSSSSSSSSSSSSSSSSS           **
      ccccccccccccc     oooooooooooooo    DDDD       DDDD     SSSS                          **
     cccc              oooo        oooo   DDDD        DDDD   SSSS                           **
    cccc              oooo          oooo  DDDD         DDDD   SSSS                          **
    cccc	          oooo          oooo  DDDD        DDDD     SSSSSSSSSSSSSSSSSS           **
     cccc              oooo        oooo   DDDD       DDDD       SSSSSSSSSSSSSSSSSS          **
      ccccccccccccc     oooooooooooooo    DDDDDDDDDDDDDD                      SSSSSS        **
       cccccccccccc      oooooooooooo     DDDDDDDeoDDDD                        SSSSSS       **           
                                                                              SSSSSSSS      **                        
       sssssssssssssssssssssssssssssssssssssssssssssssssssssssssSSSSSSSSSSSSSSSSSSSSSS      **
                            ssssssssssssssssssssssssssssssssssSamSSSSSSSSSSSSSSSSSSSS       **
           ssssssssssssssssssssssssssssssssssssssssssssssssssssssSSSSSSSSSSSSSSSSSSS        **
               ssssssssssssssssssssssssssssssssssssssssssssssssssssssssSSSSSSSSSSSS         **
                                                                                            **
 Auteurs: AMOUSSOU P. Samson                                                                **
          AMOUSSOU D. Sylvestre                                                             **
<< Cryptons, non... Codons. Amusons nous à crypter*********************************** >>******
**********************************************************************************************
 ***************************************************************************Non! Décryptons!*
                   """)

print("""Ce présent programme est juste une petite idée née lors d'une fantaisie entre son
petit frère et l'auteur du code. Il s'agira à travers le programme de crypter du texte ou 
de le décrypter en précisant le nom du fichier ou le chemin d'accès au fichier.

Le fichier à crypter ou à décrypter ainsi que les fichiers sortants doivent tous être dans le
répertoire courant d'où est lancé le programme. Merci.

Pour commencer entrez le nom du fichier texte ou le chemin d'acces au fichier. 
""")

########Création de la classe en rapport avec le type fichier à crypter ou à décrypter#################"

class Fichier_coDS:


    def __init__(self, proprio = None, name_fichier = None, key = None, type_fichier = None):
        self.proprio = proprio                                         # propriétaire du fichier
        self.name_fichier = name_fichier
        self.type_fichier = type_fichier
        self._key = self._crypt_key(key)                                 # cle du fichier

    def crypter(self, name_fichier, key):
        "fonction qui reçoit le nom d'un fichier et une clee pour la cryptee"
        return fichier_crypte

    def decrypter(self, name_fichier, key):
        "fonction qui reçoit le nom d'un fichier et une clee pour la decryptee"
        return fichier_decrypte

    def _info_fichier(self):
        return {'Propriétaire du fichier' : {self.proprio},
                'Nom du fichier' : {self.name_fichier},
                'Type du fichier' : {self.type_fichier},
                'Clé d\'accès' : {self._key}}

    def _crypt_key(self, key):
        cle = bytes(key)                                        # conversion de la chaine en byte
        cle_chiffree = hashlib.sha1(cle).hexdigest()
        return cle_chiffree


                         ######Main#########
fichier_choisie = input("[coDS] >> ")                                   #nom du fichier entrant ou chemin d'acces au fichier
fichier_existe = Path(fichier_choisie).exists()
while True:

    if fichier_existe:
        # Conversion du chemin conforme
        print("\t$$$ AU MENU : Appuyer\n"
              "\t$$$ a : pour crypter\n"
              "\t$$$ b : pour decrypter\n"
              "\t$$$ c : pour passer root\n"
              "\t$$$ q : pour quitter")

        opt_choisie = input("[coDS] >> ")

        if opt_choisie == 'a' or opt_choisie == 'b':
            print("Entrez votre pseudo :")
            proprio = input("[coDS] >> ")

            if opt_choisie == 'a':
                print("Entrez la clé de cryptage :")
                key = input(f"[{proprio}] >> ")
                while not re.fullmatch('\d{3}', key):
                    print("La clé doit être un nombre de trois chiffres!")
                    key = input(f"[{proprio}] >> ")

                file = Fichier_coDS(proprio, fichier_choisie, key, type_fichier="décrypté")                            # création de l'objet à crypter
                fichier = file.crypter(fichier_choisie, key)
                heure_crypte = datetime.datetime.now()
                info_fichier = file._info_fichier()                                                         # infos concernant le fichier suite au cryptage
                info_fichier['Crypté le'] = heure_crypte                                                   # ajout de la date de création du fichier au dictionnaire
                with open(f"{fichier_choisie}.json", 'w') as f:
                    json.dump(info_fichier, f, indent=2)                                                       # creation du fichier json pour enregistrer les infos concernant le fichier

                with open("README.txt", 'w') as f:                                                          # fichier README pour empêcher la suppression du fichier json
                    f.write('ATTENTION le fichier json créé suite au cryptage est strictement requis.'
                            'Il vous aidera à décripter votre fichier si besoin y est.'
                            'Et ne doit donc en aucun être cas supprimé!')

                print(f"Fichier bien crypté par {file.proprio}")
                print(f"Nom du fichier  : {fichier}")                                                                  # le nouveau fichier crée
                print(f"Accéder aux fichiers README.txt et {fichier_choisie}.json pour plus de détails.")
                break
            elif opt_choisie == 'b':
                print("Entrez la clé de décryptage :")
                key = input(f"[{proprio}] >> ")                                                         # La clé devrait être normalement crypté Bientôt ...
                while not re.fullmatch('\d{3}', key):
                    print("La clé doit être un nombre de trois chiffres!")
                    key = input(f"[{proprio}] >> ")

                print("Indiquez le nom du fichier json associé :")
                fichier_json = input("[coDS] >> ")
                with open(fichier_json) as j:
                    dict_json = json.load(j)

                while True:
                    if dict_json['Clé d\'accès'] == key and dict_json['Type du fichier'] == 'crypté':     # vérifier si la clé est correcte et que le type est 'crypté' avant de procéder au décryptage
                        file = Fichier_coDS(key)
                        fichier = file.decrypter(fichier_choisie, key)
                        print("Vôtre fichier est bien décrypté.")
                        print(f"Vous pouvez le consulter sous le nom de {fichier}.")
                        print(f"À bientôt {proprio}")
                        break
                    else:
                        print("La clé entrée est incorrecte ou le fichier entré est déjà crypté. Voulez vous réessayer ? (y/n)")            # si l'utilisateur veut réessayer
                        essai = input(f"[{proprio}] >> ")
                        if essai == 'y':
                            continue
                        else:
                            break
                break
            break

        elif opt_choisie == 'c':
            print('Bientôt ...')                   # interface root pour administrer les fichiers entrant et sortant du programme
            break
        elif opt_choisie == 'q':
            print("À bientôt :-)")
            break
        else:
            print("""Vous n'avez pas saisie une option du menu. Veuillez reprendre!""")
            continue

    else:
        # Le chemin n'existe pas
        print("Le fichier n'existe pas.")
        print("Voulez-vous bien retapper le chemin exact (y/n) ?")
        opt_choisie = input("[coDS] >> ")

        if opt_choisie == 'y':
            opt_choisie = input("[coDS] >> ")
        else:
            break



