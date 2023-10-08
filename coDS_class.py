import hashlib
import json
import coDS_variables

class Fichier_coDS:
# ces  variables ci-dessous representent les dictionnaires elementaires
# du projet coDS

    default = coDS_variables.default_key
    alpha = coDS_variables.alphabet
    lang = coDS_variables.dictio_lang_numbers
    normal = coDS_variables.dictio_normal_numbers
    ponct = coDS_variables.ponctuation
    white_caract = coDS_variables.white_caracteres

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
      #  f_t = False
        with open(json_file) as f:
            file_info = json.load(f)
        if file_info["key"] == self.__key:
        #    f_t = True
            return True
        else:
            return False

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
                return 'file_decrypted'
            else:
                return 'file_encrypted'

    def crypt_file(self, name_file):
        "methode pour crypter un fichier"
         return file_crypte, file_crypte.json

    def decrypt_file(self, name_fichier, key):
        "methode pour decrypter un fichier"
        return file_decrypte


