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

***********
*MENU: Cliquer
a : Pour crypter
b : Pour décrypter
c : Pour passer root
q : Pour quitter
**********************
***********************

""")

class Fichier_coDS:
    def __init__(self, proprio, name_fichier, type_fichier, key):
        self.proprio = proprio                                         # propriétaire du fichier
        self.name_fichier = name_fichier
        self.type_fihier = type_fichier
        self._key = self._crypt_key(key)                                 # cle du fichier

    def crypter(self):

    def decrypter(self):

    def info_fichier(self):

    def _crypt_key(self):



opt_choisie = input("[coDS] >> ")                                      # option choisie dans le menu
flag = True                                                            # pour continuer dans la boucle

while flag:
    if opt_choisie == 'a':
        print('a')
        break
    elif opt_choisie == 'b':
        print('b')
        break
    elif opt_choisie == 'c':
        print('c')
        break
    elif opt_choisie == 'q':
        print("À bientôt :-)")
        flag = False
    else:
        print("""Vous n'avez pas saisie une option du menu.
        Veuillez reprendre!""")
        opt_choisie = input("[coDS] >> ")

