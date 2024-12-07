#!/usr/bin/env python
"""
Xifrat_Cèsar_amb_abecedari_a_triar.py.
Programa per encriptar text amb la Xifra de Cèsar.

Aquest programa rep un text introduït per l’usuari, permet escollir
l'abecedari a utilitzar, demana el desplaçament que desitja i encripta
el missatge utilitzant la xifra de Cèsar.

Institut Icària

Aquest programa aplica el xifratge de Cèsar a un text donat amb un abecedari
personalitzat. El resultat és una cadena de text on les lletres han estat
desplaçades en l'abecedari seleccionat segons el valor indicat com a
desplaçament.
"""


__author__ = "Oriol Monserrat Digón"
__email__ = "omonserrat@instituticaria.cat"
__date__ = "2024/11/28"


from unidecode import unidecode


# Funció de xifratge de Cèsar:
def xifratge_cesar(text, desplacament):
    """
    xifratge_cesar. Aplica un desplaçament de Cèsar a un text donat.

    Aquesta funció encripta un text aplicant el xifratge de Cèsar. Cada lletra
    del text es desplaça en l'abecedari segons el valor de desplaçament
    proporcionat.

    Arguments:
        text: El text a encriptar. Ha de ser una cadena de text.
        desplaçament: Nombre enter que indica el desplaçament de Cèsar.

    Retorna:
        resultat: Text encriptat amb el xifratge de Cèsar.
    """
    resultat = ""

    # Convertim el text a majúscules per simplificar:
    text = text.upper()

    # Encriptació:
    for lletra in text:
        # Si és una lletra:
        if lletra in abecedari:
            # Trobar la posició en l'abecedari:
            index = abecedari.index(lletra)

            # Calcular la nova posició:
            nova_posicio = (index + desplaçament) % 26

            # Afegir la lletra corresponent:
            resultat += abecedari[nova_posicio]

    # Si el caràcter no és una lletra, simplement no s'afegeix.

    return resultat


if __name__ == '__main__':
    # Entrada de l'usuari:
    text_usuari = input("Introdueix el text a encriptar: ")
    abecedari = input("Introdueixi l'abecedari que desitja usar: ")
    abecedari = abecedari.upper()  # Majuscular.
    desplaçament = int(input("Introdueix el desplaçament Cèsar: "))

    # Eliminació d'accents en el text:
    text_no_accents = unidecode(text_usuari)

    # Encriptar i mostrar el resultat:
    text_encriptat = xifratge_cesar(text_no_accents, desplaçament)
    print(f"Text encriptat: {text_encriptat}")
