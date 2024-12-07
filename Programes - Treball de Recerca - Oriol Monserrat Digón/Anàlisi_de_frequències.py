#!/usr/bin/env python
"""
Gràfic de barres.
Aquest programa genera un gràfic de barres amb la freqüència de les lletres
d'un text.

Institut Icària

Aquest programa analitza un text introduït per l'usuari i mostra la freqüència
de les seves lletres en forma de gràfic de Pareto.
"""

__author__ = "omonserrat@instituticaria.cat"
____ = "omonserrat@instituticaria.cat"
__date__ = "2024/11/28"


import string
import matplotlib.pyplot as plt
from unidecode import unidecode


def grafic_de_barres(text):
    """
    Grafic de barres. Mostra la freqüència de les lletres d'un text

    Aquesta funció analitza el text introduït per l'usuari, calcula la
    freqüència de cada lletra i mostra els resultats en un gràfic de barres.

    Arguments:
        text: Cadena de text a analitzar. Pot contenir qualsevol caràcter.

    Retorna:
        No retorna cap valor. Mostra un gràfic de barres amb les freqüències.
    """
    figura, eixos = plt.subplots()
    eixos.set_xticks(range(0, 26))  # Longitud de l'eix x.

    # Loop per crear les barres del diagrama de barres:
    freq = []

    for i in range(0, 26):
        freq.append(text.count(abecedari_upper[i]) + text.count(abecedari_lower[i]))

    freq_ord = []
    abecedari_ord = []
    for j in range(0, 26):
        freq_max = freq[0]
        index_max = 0
        for k in range(1, len(freq)):
            if freq[k] > freq_max:
                freq_max = freq[k]
                index_max = k

        freq_ord.append(freq_max)
        abecedari_ord.append(abecedari_upper[index_max])
        freq.pop(index_max)
        abecedari_upper.pop(index_max)

    eixos.bar(abecedari_ord, freq_ord, color='cornflowerblue')
    plt.show()


if __name__ == '__main__':
    # Entrada de l'usuari:
    text_usuari = input("Introdueix el text: ")

    # Abecedari
    abecedari_upper = list(string.ascii_uppercase)
    abecedari_lower = list(string.ascii_lowercase)

    # Eliminació d'accents en el text:
    text_no_accents = unidecode(text_usuari)

    # Creació del gràfic
    grafic_de_barres(text_no_accents)
