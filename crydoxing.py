from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time
import os.path


os.system('clear' if os.name == 'posix' else 'cls')

intro = """

 ▄▄· ▄▄▄   ▄· ▄▌    ·▄▄▄▄        ▐▄• ▄ ▪   ▐ ▄  ▄▄ •        By Spaso      Discord: Spaso#9999
▐█ ▌▪▀▄ █·▐█▪██▌    ██▪ ██ ▪      █▌█▌▪██ •█▌▐█▐█ ▀ ▪       
██ ▄▄▐▀▀▄ ▐█▌▐█▪    ▐█· ▐█▌ ▄█▀▄  ·██· ▐█·▐█▐▐▌▄█ ▀█▄       
▐███▌▐█•█▌ ▐█▀·.    ██. ██ ▐█▌.▐▌▪▐█·█▌▐█▌██▐█▌▐█▄▪▐█
·▀▀▀ .▀  ▀  ▀ •     ▀▀▀▀▀•  ▀█▄▀▪•▀▀ ▀▀▀▀▀▀▀ █▪·▀▀▀▀ 

          

                > Appuyer sur Entrer <                                       

"""


Anime.Fade(Center.Center(intro), Colors.purple_to_red, Colorate.Vertical, interval=0.035, enter=True)



import os

pseudo = input("Pseudo de la victime: ")
output_file = "crydoxing.txt"
no_results = True

with open(output_file, "w") as file:
    file.write(f"Recherche de \"{pseudo}\"\n\n")

for root, dirs, files in os.walk("."):
    for filename in files:
        filepath = os.path.join(root, filename)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            if pseudo.lower() in file.read().lower():
                no_results = False
                with open(output_file, "a") as output:
                    output.write(f"{filepath}\n")
                    output.write(f"{pseudo} trouvé :\n")
                    file.seek(0)
                    for i, line in enumerate(file.readlines()):
                        if pseudo.lower() in line.lower():
                            output.write(f"{i+1}: {line.strip()}\n")

if no_results:
    with open(output_file, "a") as file:
        file.write(f"\nAucun résultat trouvé pour \"{pseudo}\".\n")
        file.write("Fermeture du programme...")
    print(f"\nAucun résultat trouvé pour \"{pseudo}\". Veuillez consulter le fichier \"{output_file}\".")
else:
    with open(output_file, "a") as file:
        file.write("\nFin de la recherche.")
    print(f"Résultats trouvés pour \"{pseudo}\". Veuillez consulter le fichier \"{output_file}\".")

input("\nAppuyez sur une touche pour fermer le programme...")


def banner():
    print(f"""
    \t\t         ▐▄• ▄ ▪   ▐ ▄  ▄▄ • 
    \t\t        ▐█ ▌▪▀▄ █·▐█▪██▌    ██▪ ██ ▪      █▌█▌▪██ •█▌▐█▐█ ▀ ▪
    \t\t        ██ ▄▄▐▀▀▄ ▐█▌▐█▪    ▐█· ▐█▌ ▄█▀▄  ·██· ▐█·▐█▐▐▌▄█ ▀█▄
    \t\t        ▐███▌▐█•█▌ ▐█▀·.    ██. ██ ▐█▌.▐▌▪▐█·█▌▐█▌██▐█▌▐█▄▪▐█
    \t\t         ▀▀▀ .▀  ▀  ▀ •     ▀▀▀▀▀•  ▀█▄▀▪•▀▀ ▀▀▀▀▀▀▀ █▪·▀▀▀▀ 
    \t\t                                
    \t\t 
    \t\t                            by Spaso
    \t\t                  
    \t\t               https://doxbin.com/user/OupsSpaso                                 
    \t\t
    \t\t                       http://spaso.site/               \n\n\n\n""")


