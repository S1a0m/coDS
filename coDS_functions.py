# import coDS_class
from pathlib import Path
import coDS_variables
from colorama import Fore, Style, init

init()


def file_exist():
    enter_file = input("\nEntrer le nom/chemin d'acces du fichier $> ")
    file_there = Path(enter_file).exists() and Path(enter_file).is_file()
    return file_there


def warning():
    print(Fore.RED + Style.BRIGHT + "\n/_!_\\" + Style.RESET_ALL,
          " Le fichier que vous avez entré n'existe pas.\
            \nIl est possible qu'il s'agisse d'un dossier.\
            \nVérifiez si vous l'avez bien écrit et qu'il s'agit bel et bien d'un fichier texte.")


def file_right(file, right):
    "fonction qui vérifie les droits sur le fichier"
    try:
        f = open(file, right)
        f.close()
        return True
    except PermissionError:
        return False


def main_crypt():
    return 1


def main_decrypt():
    return 2


def main_coDS():
    """la fonction principale de tout le projet coDS"""
    while True:
        if file_exist():                                                       # traitement
            print()
            print(coDS_variables.menu)
            choose_option = input("Choisir une option $> ")
            while choose_option:
                if choose_option == 'a':
                    main_crypt()
                    print("Fichier bien crypté")
                    break
                elif choose_option == 'b':
                    main_decrypt()
                    print("Fichier bien décrypté")
                    break
                elif choose_option == 'q':
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + "/_!_\\" + Style.RESET_ALL,
                          " Vous devez entrer l'une des options du menu.\nReprenez!")
                    choose_option = input("Choisir une option $> ")
            break
        else:
            warning()                                                             # avertier l'utilisateur si le fichier n'existe pas
            resume = input("Voulez-vous reprendre? (y/n) $> ")
            if resume == 'y':
                continue
            else:
                break


if __name__ == '__main__':
    print()
