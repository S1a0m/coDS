from colorama import Fore, Style, init

init()

# variables de presentation #

welcome = Fore.MAGENTA + Style.BRIGHT + """
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
     cccc              oooo        oooo   DDDD        DDDD     SSSSSSSSSSSSSSSSSSSSS        **
      ccccccccccccc     oooooooooooooo    DDDDDDDDDDDDDDD         SSSSSSSSSSSSSSSSSSS       **
       cccccccccccc      oooooooooooo     DDDDDDDeoDDDDD                       SSSSSSS      **           
                                                                              SSSSSSSS      **                        
       sssssssssssssssssssssssssssssssssssssssssssssssssssssssssSSSSSSSSSSSSSSSSSSSSSS      **
                            ssssssssssssssssssssssssssssssssssSamSSSSSSSSSSSSSSSSSSSS       **
           ssssssssssssssssssssssssssssssssssssssssssssssssssssssSSSSSSSSSSSSSSSSSSS        **
               ssssssssssssssssssssssssssssssssssssssssssssssssssssssssSSSSSSSSSSSS         **
                                                                                            **
 Authors: AMOUSSOU P. Samson                                                                **
          AMOUSSOU D. Sylvestre                                                             **
<< Cryptons, non... Codons. Amusons nous à crypter*********************************** >>******
**********************************************************************************************
 ***************************************************************************Non! Décryptons!*
                   """ + Style.RESET_ALL

menu = (Fore.BLUE + Style.BRIGHT + "\t   |AU MENU| : Entrer\n\t_____________________\n\t-> a : pour crypter\n\t-> b "
                                   ": pour decrypter\n\t-> q :"
                                   " pour quitter\n\t_____________________" + Style.RESET_ALL)
# pense a renommer la variable affiche
affiche = ("\n"
           "  ^\n"
           " /|\\\n"
           "/_!_\\")

attention = Fore.RED + Style.BRIGHT + affiche + Style.RESET_ALL

#########################################################################################################
# dictionnaires general de l'alphabet coDS
# une clé par défaut qui est à 130

default_key = 130

alphabet = [
    ('A', 'a'), ('B', 'b'), ('C', 'c'),
    ('D', 'd'), ('E', 'e'), ('F', 'f'),
    ('G', 'g'), ('H', 'h'), ('I', 'i'),
    ('J', 'j'), ('K', 'k'), ('L', 'l'),  # Lettres de l'alphabet
    ('M', 'm'), ('N', 'n'), ('O', 'o'),
    ('P', 'p'), ('Q', 'q'), ('R', 'r'),
    ('S', 's'), ('T', 't'), ('U', 'u'),
    ('V', 'v'), ('W', 'w'), ('X', 'x'),
    ('Y', 'y'), ('Z', 'z')
]

dictio_lang_numbers = {
    0: 'n', 1: 'o', 2: 'q', 3: 'r', 4: 't',  # correspondance nombre de l'alphabet --> lettre
    5: 'u', 6: 'w', 7: 'x', 8: 'y', 9: 'z'
}

dictio_normal_numbers = {
    0: 'hn', 1: 'ho', 2: 'hq', 3: 'hr', 4: 'ht',  # correspondance nombre --> lettre
    5: 'hu', 6: 'hw', 7: 'hx', 8: 'hy', 9: 'hz'
}

ponctuation = {
    '.': 'p', ',': 'v', '*': 'm', '/': 'd', '=': 'g',  # correspondance ponctuation --> convention_ponctuation
    ';': '4psv1', '!': '4pse1', '?': '4psi1', '+': '4pss1',
    '-': '4mss1'
}

# commencer un mot   '0x'
# separer deux mots   choisir aleatorement dans cette liste [a, b, f, j, k, l]

white_caracteres = {'\b': '0x', ' ': ('a', 'b', 'f', 'j', 'k', 'l')}
