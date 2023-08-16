from getpass import getpass
import re
import hashlib
import json
import pathlib
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

Pour commencer entrez le nom du fichier texte. 
""")

class Fichier_coDS:
    def __init__(self, proprio, name_fichier, key, type_fichier):
        self.proprio = proprio                                         # propriétaire du fichier
        self.name_fichier = name_fichier
        self.type_fichier = type_fichier
        self._key = self._crypt_key(key)                                 # cle du fichier

    def crypter(self, key):

    def decrypter(self, key):

    def info_fichier(self):
        return {'Propriétaire du fichier' : {self.proprio},
                'Enregistré le ' : {date},
                'Nom du fichier' : {self.name_fichier},
                'Type du fichier' : {self.type_fichier},
                'Clé d\'accès' : {self._key}}

    def _crypt_key(self, key):
        cle = bytes(key)                                        # conversion de la chaine en byte
        cle_chiffree = hashlib.sha1(cle).hexdigest()
        return cle_chiffree
    pass


fichier_choisie = input("[coDS] >> ")                                   #nom du fichier entrant
flag = True                                                            # pour continuer dans la boucle

while flag:

    try:
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
                fichier = file.crypter()
                with open(f"{fichier_choisie}.json", 'w') as f:
                    f.write('ATTENTION le fichier que vous lisez est strictement requis.'
                            'Il vous aidera à décripter votre fichier si besoin y est.'
                            'Il ne doit donc être en aucun cas supprimé!\n')
                    json.dump(file.info_fichier(), f, indent=2)                                                       # creation du fichier json pour enregistrer les infos concernant le fichier

                print(f"Fichier bien enregistré par {file.proprio}")
                print(f"Nom du fichier  : {fichier}")                                                                  # le nouveau fichier crée
                print(f"Accéder au fichier {fichier_choisie}.json pour plus de détails.")
                break
         #########################################################################################
            break

        elif opt_choisie == 'c':
            print('Bientôt ...')
            break
        elif opt_choisie == 'q':
            print("À bientôt :-)")
            break
        else:
            print("""Vous n'avez pas saisie une option du menu.
            Veuillez reprendre!""")
            continue

    except :
        # Le chemin n'existe pas
        print("Le chemin n'existe pas ou ne suit pas les regles d'un chemin.")
        print("Voulez-vous bien retapper le chemin exact (y/n) ?")
        opt_choisie = input("[coDS] >> ")

        if opt_choisie == 'y':
            opt_choisie = input("[coDS] >> ")
        else:
            break



