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

Pour commencer entrez le nom ou le chemin d'acces au fichier texte. 
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
                'Enregistré le ' : {save},
                'Chemin d\'accès au fichier' : {self.name_fichier},
                'Type du fichier' : {self.type_fichier},
                'Cle d\'accès' : {self._key}}

    def _crypt_key(self, key):
        cle = bytes(key)                                        # conversion de la chaine en byte
        cle_chiffree = hashlib.sha1(cle).hexdigest()
        return cle_chiffree



opt_choisie = input("[coDS] >> ")                                      # option choisie dans le menu
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

        if opt_choisie == 'a':
            print("Entrez votre pseudo :")
            proprio = input("[coDS] >> ")
            print("Le nouveau nom au fichier crypté :")
            name_fichier = input(f"[{proprio}] >> ")
            print("La cle de cryptage :")

            key = input(f"[{proprio}] >> ")
            while not re.fullmatch('\d{3}', key):
                print("La clé doit être un nombre de trois chiffres!")
                key = input(f"[{proprio}] >> ")

            file = Fichier_coDS(proprio, name_fichier, key, type_fichier="crypté")                                       # création de l'objet à crypter
            file.crypter()
            print(f"Fichier bien enregistré le {date} par {file.proprio}")
            print(f"Type du fichier : {file.type_fichier}\n"
                  f"Chemin d'acces : {file.name_fichier}")
            break

        elif opt_choisie == 'b':
            print('b')
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



