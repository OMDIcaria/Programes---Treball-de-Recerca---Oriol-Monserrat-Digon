#!/usr/bin/env python
"""
Xifra_de_Vigènere.py.
Programa per encriptar text amb la xifra de Vigenère.

Aquest programa rep un text introduït per l’usuari, demana una clau i encripta
el text utilitzant la xifra de Vigenère.

Institut Icària

Aquest programa aplica el xifratge de Vigenère, utilitzant una clau
proporcionada per l’usuari. El resultat és un text encriptat on cada lletra es
desplaça segons la lletra corresponent de la clau.
"""


__author__ = "Oriol Monserrat Digón"
__email__ = "omonserrat@instituticaria.cat"
__date__ = "2024/12/01"


import string
from unidecode import unidecode


# Funció de xifratge de Vigenère:
def xifratge_vigenere(text, clau):
    """
    xifratge_vigenere. Aplica la xifra de Vigenère a un text donat.

    Aquesta funció encripta un text aplicant la xifra de Vigenère. Cada lletra
    del text es desplaça segons la lletra corresponent de la clau.

    Arguments:
        text: El text a encriptar. Ha de ser una cadena de text.
        clau: Una clau alfabètica per al xifratge. Ha de ser una cadena
              text.

    Retorna:
        resultat: Text encriptat amb la xifra de Vigenère.
    """
    resultat = ""

    # Convertim el text i la clau a majúscules per simplificar:
    text = text.upper()
    clau = clau.upper()

    # Informació necessaria de la clau:
    llargada_clau = len(clau)
    clau_index = 0

    # Encriptació:
    for lletra in text:
        # Si és una lletra:
        if lletra in abecedari:
            # Trobar la posició en l'abecedari de la lletra i la clau:
            index_text = abecedari.index(lletra)
            index_clau = abecedari.index(clau[clau_index])

            # Calcular la nova posició:
            nova_posicio = (index_text + index_clau) % 26

            # Afegir la lletra corresponent:
            resultat += abecedari[nova_posicio]

            # Avançar la clau:
            clau_index = (clau_index + 1) % llargada_clau

    # Si el caràcter no és una lletra, simplement no s'afegeix.

    return resultat


if __name__ == '__main__':
    # Entrada de l'usuari:
    text_usuari = input("Introdueix el text a encriptar: ")
    clau = input("Introdueix la clau per la xifra de Vigenère: ")

    # Generació de l'abecedari:
    abecedari = list(string.ascii_uppercase)

    # Eliminació d'accents en el text:
    text_no_accents = unidecode(text_usuari)

    # Encriptar i mostrar el resultat:
    text_encriptat = xifratge_vigenere(text_no_accents, clau)
    print(f"Text encriptat: {text_encriptat}")
