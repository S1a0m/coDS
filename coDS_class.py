import hashlib
import json

class Fichier_coDS:

    # dictionnaires general de l'alphabet coDS
    # une clé par défaut qui est à 130

    general_key = 130

    alphabet = [
        ('A', 'a'), ('B', 'b'), ('C', 'c'),
        ('D', 'd'), ('E', 'e'), ('F', 'f'),
        ('G', 'g'), ('H', 'h'), ('I', 'i'),
        ('J', 'j'), ('K', 'k'), ('L', 'l'),                                 # Lettres de l'alphabet
        ('M', 'm'), ('N', 'n'), ('O', 'o'),
        ('P', 'p'), ('Q', 'q'), ('R', 'r'),
        ('S', 's'), ('T', 't'), ('U', 'u'),
        ('V', 'v'), ('W', 'w'), ('X', 'x'),
        ('Y', 'y'), ('Z', 'z')
    ]

    dictio_lang_numbers = {
        0: 'n', 1: 'o', 2: 'q', 3: 'r', 4: 't',                                # correspondance nombre de l'alphabet --> lettre
        5: 'u', 6: 'w', 7: 'x', 8: 'y', 9: 'z'
    }

    dictio_normal_numbers = {
        0: 'hn', 1: 'ho', 2: 'hq', 3: 'hr', 4: 'ht',                          # correspondance nombre --> lettre
        5: 'hu', 6: 'hw', 7: 'hx', 8: 'hy', 9: 'hz'
    }

    ponctuation = {
        '.': 'p', ',': 'v', '*': 'm', '/': 'd', '=': 'g',                         # correspondance ponctuation --> convention_ponctuation
        ';': '4psv1', '!': '4pse1', '?': '4psi1',  '+': '4pss1',
        '-': '4mss1'
    }

# commencer un mot   '0x'
# separer deux mots   choisir aleatorement dans cette liste [a, b, f, j, k, l]

    white_caracteres = { '\b': '0x', ' ': ('a', 'b', 'f', 'j', 'k', 'l') }

    def __init__(self, name_file, key, json_file=None):
        self.name_file = name_file
        self.json_file = json_file
        self.type_file = self.type_file(self.json_file)
        self.__user_dict = self.__user_coDS_lang()
        self.__key = self.__crypt_key(key)                                 # cle du fichier

    def __crypt_key(self, param_key):
        key = bytes(param_key)                                        # conversion de la chaine en byte
        key_crypte = hashlib.sha1(key).hexdigest()
        return key_crypte

    def __user_coDS_lang(self, key):
        "methode de creation du dictionnaire spécifique à l'utilisateur"
        return final_dict
        pass

    def auth_key(self, json_file):
        "methode pour verifier l'authenticite d'une clee"
        f_t = False
        with open(json_file) as f:
            file_info = json.load(f)
        if file_info["key"] == self.__key:
            f_t = True
            return f_t
        else:
            return f_t

    def get_name_file(self):
        return self.name_file

    def type_file(self, json_file=None, t_f=False):
        "methode pour détecter le type du fichier"
        if json_file is not None:
            with open(json_file) as f:
                file_info = json.load(f)
                return file_info["type"]
        else:
            if t_f == False:
                return 'file_decrypte'
            else:
                return 'file_crypte'

    def crypt_file(self, name_file):
        "methode pour crypter un fichier"
         return file_crypte, file_crypte.json

    def decrypt_file(self, name_fichier, key):
        "methode pour decrypter un fichier"
        return file_decrypte


