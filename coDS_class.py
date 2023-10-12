import hashlib
import json
import coDS_variables

from sympy import gcd, divisors, symbols, Eq, solve


class Abc_co:
    """ let us suppose
    this equation :
    ax + by = c """

    def __init__(self, a, fetish=1):            # there is also fetish attribute to make c != b
        self.a = int(a)
        self.fetish = int(fetish)
        self.__b = self.__find_b()
        self.__c = gcd(self.a, self.__b) * self.fetish

    def __find_b(self):
        # trouver b
        divisors_list = divisors(self.a)       # recuperer l'ensemble des diviseurs de a dans une liste
        i = len(divisors_list) - 2
        b = divisors_list[i]                     # recuperer l'avant dernier element de la liste
        return b

    def solutions(self):
        """ This method find 26 solutions
        of the equation behind and bring
        them in a list """
        # tri et solutions de l'equation
        x, y = symbols("x y")
        equation = Eq(self.a * x + self.__b * y, self.__c)
        solution = solve(equation, (x, y))
        # le tri n'est pas encore effectue
        return solution


class File_co:
# ces  variables ci-dessous representent les dictionnaires elementaires
# du projet coDS

    default = coDS_variables.default_key
    alpha = coDS_variables.alphabet
    lang = coDS_variables.dictio_lang_numbers
    normal = coDS_variables.dictio_normal_numbers
    dot = coDS_variables.ponctuation
    white_caract = coDS_variables.white_caracteres

    def __init__(self, name_file, key, json_file=None):
        self.name_file = name_file
        self.json_file = json_file
        self.type_file = self.type_file(self.json_file)
        self.__user_dict = self.__user_coDS_lang()
        self.__key = self.__crypt_key(key)                                 # cle du fichier

    @staticmethod
    def __crypt_key(key: int) -> str:
        key = bytes(key)                                        # conversion de la chaine en byte
        key_crypte = hashlib.sha1(key).hexdigest()
        return key_crypte

    def __user_coDS_lang(self):
        """ methode de creation du dictionnaire
        spécifique à l'utilisateur """
        return final_dict
        pass

    def auth_key(self, json_file):
        """ methode pour verifier l'authenticite d'une clee """
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
        """ methode pour détecter le type du fichier """
        if json_file is not None:                       # verifier si le fichier json est accessible
            with open(json_file) as f:
                file_info = json.load(f)
                return file_info["type"]
        else:                                           # si oui determiner le fichier crypte associe
            if t_f:                                     # la variable t_f(vrai/faux) pour voir s'il est crypte ou non
                return 'file_decrypted'
            else:
                return 'file_encrypted'

    def crypt_file(self, name_file):
        """ methode pour crypter un fichier """
         return file_crypte, file_crypte.json

    def decrypt_file(self, name_fichier, key):
        """ methode pour decrypter un fichier """
        return file_decrypte


