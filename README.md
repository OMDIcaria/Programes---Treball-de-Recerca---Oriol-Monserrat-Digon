# Encriptació Clàssica: Evolució i Implementacions amb Python
Aquest repositori recull les implementacions en Python desenvolupades en el marc del meu Treball de Recerca, centrades en l'estudi i la recreació de mètodes d'encriptació clàssica.

L'objectiu és explorar i entendre els sistemes d'encriptació utilitzats des dels temps romans fins a la Segona Guerra Mundial. Aquí trobaràs:

Algorismes clàssics: la Xifra de Cèsar, la Xifra de Vigenère i la Màquina Enigma; un mètode de criptoanàlisi, l'anàlisi de freqüències.

# Xifra de Cèsar:
Aquest programa rep un text introduït per l'usuari, demana el desplaçament que desitja i encripta el missatge utilitzant la xifra de Cèsar. El resultat és una cadena de text on les lletres han estat desplaçades en l'abecedari segons el valor indicat com a desplaçament.

N'he fet dues variacions. La primera usa l'abecedari normal per encriptar i la segona demana a l'usuari l'abecedari que vol usar.

# Xifra de Vigenère:
Aquest programa aplica el xifratge de Vigenère, utilitzant una clau proporcionada per l’usuari. El resultat és un text encriptat on cada lletra es desplaça segons la lletra corresponent de la clau.

# Màquina Enigma:
Aquest programa implementa una versió reduïda del mecanisme de la Màquina Enigma amb rotors i reflector, incloent-hi el moviment automàtic dels rotors però no el claviller. El programa rep un text introduït per l’usuari, demana les posicions inicials dels rotors i encripta el text.

El programa està basat en el model de la Màquina Enigma "Comercial Enigma A, B" segons: https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables
