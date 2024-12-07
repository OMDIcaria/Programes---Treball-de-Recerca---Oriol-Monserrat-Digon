#!/usr/bin/env python
"""
Màquina_Enigma.py.
Programa per encriptar text amb una versió simplificada de la Màquina Enigma.

Aquest programa rep un text introduït per l’usuari, demana les posicions
inicials dels rotors i encripta el text utilitzant una simulació simplificada
de la Màquina Enigma.

El programa està basat en el model de la Màquina Enigma "Comercial Enigma A, B"
segons: https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables

Institut Icària

Aquest programa implementa una versió reduïda del mecanisme de la Màquina
Enigma amb rotors i reflector, incloent el moviment automàtic dels rotors però
no el claviller.
"""


__author__ = "Oriol Monserrat Digón"
__email__ = "omonserrat@instituticaria.cat"
__date__ = "2024/12/03"


import string
from unidecode import unidecode


def xifratge_cesar_normal(lletr, despla, rot):
    """
    xifratge_cesar_normal. Aplica un desplaçament Cèsar a una lletra
    utilitzant un rotor.

    Arguments:
        lletra: La lletra a desplaçar.
        desplaçament: El desplaçament a aplicar.
        rotor: El rotor que defineix l'abecedari amb que xifrar.

    Retorna:
        La lletra xifrada després del desplaçament aplicat pel rotor.
    """
    index = abecedari.index(lletr)
    nova_posicio = (index + despla) % 26
    return rot[nova_posicio]


def xifratge_cesar_invers(lletr, despla, rot):
    """
    xifratge_cesar_invers. Aplica un desplaçament Cèsar invers a una lletra
    utilitzant un rotor. Posat en paraules fàcils, desfà la codificació del
    rotor per codificar.

    Arguments:
        lletra: La lletra a desplaçar.
        desplaçament: El desplaçament a aplicar.
        rotor: El rotor que defineix el mapa de xifratge.

    Retorna:
        La lletra original abans del desplaçament aplicat pel rotor.
    """
    index = rot.index(lletr)
    nova_posicio = (26 + index - despla) % 26
    return abecedari[nova_posicio]


def maquina_enigma():
    """
    maquina_enigma. Simula el funcionament d'una Màquina Enigma simplificada.

    Aplica el mecanisme de la Màquina Enigma amb tres rotors i un reflector
    per xifrar el text proporcionat per l'usuari.

    Retorna:
        El text encriptat utilitzant la Màquina Enigma.
    """
    # "Abecedari" dels rotors:
    rotor_1 = (
        'D', 'M', 'T', 'W', 'S', 'I', 'L', 'R', 'U', 'Y', 'Q', 'N', 'K',
        'F', 'E', 'J', 'C', 'A', 'Z', 'B', 'P', 'G', 'X', 'O', 'H', 'V'
    )
    rotor_2 = (
        'H', 'Q', 'Z', 'G', 'P', 'J', 'T', 'M', 'O', 'B', 'L', 'N', 'C',
        'I', 'F', 'D', 'Y', 'A', 'W', 'V', 'E', 'U', 'S', 'R', 'K', 'X'
    )
    rotor_3 = (
        'U', 'Q', 'N', 'T', 'L', 'S', 'Z', 'F', 'M', 'R', 'E', 'H', 'D',
        'P', 'X', 'K', 'I', 'B', 'V', 'Y', 'G', 'J', 'C', 'W', 'O', 'A'
    )
    reflector = (
        'E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C',
        'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D'
    )

    # Calcular el desplaçament inical dels rotors:
    desplaçament_1 = rotor_1.index(pos_rotor_1)
    desplaçament_2 = rotor_2.index(pos_rotor_2)
    desplaçament_3 = rotor_3.index(pos_rotor_3)

    resultat = ""
    for lletra in text_upper:
        if lletra in abecedari:
            # Càlcul de la sortida del text xifrat:
            r1 = xifratge_cesar_normal(lletra, desplaçament_1, rotor_1)
            r2 = xifratge_cesar_normal(r1, desplaçament_2, rotor_2)
            r3 = xifratge_cesar_normal(r2, desplaçament_3, rotor_3)
            r4 = xifratge_cesar_normal(r3, 0, reflector)
            r5 = xifratge_cesar_invers(r4, desplaçament_3, rotor_3)
            r6 = xifratge_cesar_invers(r5, desplaçament_2, rotor_2)
            r7 = xifratge_cesar_invers(r6, desplaçament_1, rotor_1)
            resultat += r7

            # Càlcul de les noves posicionss dels rotors:
            if desplaçament_2 == 25 and desplaçament_1 == 25:
                desplaçament_3 = (desplaçament_3 + 1) % 26
            if desplaçament_1 == 25:
                desplaçament_2 = (desplaçament_2 + 1) % 26
            desplaçament_1 = (desplaçament_1 + 1) % 26

    return resultat


if __name__ == '__main__':
    # Entrada de l'usuari:
    text_usuari = input("Introdueix el text a encriptar: ")
    pos_rotor_1 = input("Introdueix la posició del rotor I: ").upper()
    pos_rotor_2 = input("Introdueix la posició del rotor II: ").upper()
    pos_rotor_3 = input("Introdueix la posició del rotor III: ").upper()

    # Generació de l'abecedari:
    abecedari = list(string.ascii_uppercase)

    # Formatitxazació del text:
    text_no_accents = unidecode(text_usuari)
    text_upper = text_no_accents.upper()

    text_encriptat = maquina_enigma()

    print(f"Text encriptat: {text_encriptat}")
