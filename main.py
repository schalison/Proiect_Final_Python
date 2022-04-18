import sys
from angajati import Angajat
from departament import Departament

def vizualizare():
    """ Reprezinta submeniul de vizualizare, care contine urmatoarele optiuni:
    1. Vizualizare a tuturor angajatilor in functie de departament
    2. Vizualizarea angajatilor dintr-un departament
    3. Iesire la meniul principal
    """

    pass

def informatii_firma():
    """ Reprezinta submeniul de informatii despre firma, care contine urmatoarele optiuni:
    1. Afisare medie salariala.
    2. Afisare nr angajati/ departament
    3. Afisare nr de angajati cu vechime mai mare de x ani.
    4. iesire la meniul principal
    """
    pass

def adaugare_angajati():
    """ Reprezinta functia de adaugare a angajatilor. Functia cere datele pentru crearea unui obiect
    nou de tip angajat, il adauga in Angajat.lista_anagajati si face update la fisierul 'angajati.csv'.
    * Nota: adaugarea se poate face si dintr-o functie dedicata din clasa de Angajat (in acest caz,
    functia asta doar va apela functia creata in clasa Angajat, [update docstring])
    """
    pass



def main():
    """ Functia de main a proiectului. Reprezinta meniul principal"""
    dict_optiuni = {

        "1": vizualizare,
        "2": informatii_firma,
        "3": adaugare_angajati,
        "4": sys.exit
    }

    # Apelarea functiei load_angajati pentru a incarca datele din fisier in baza curenta de date
    Angajat.load_angajati("angajati.csv")
    while True:
        print(35 * "=")
        print("Meniu".center(35))
        print(35 * "=")
        print("1. Vizualizare\n2. Informatii despre firma\n3. Adaugare angajati\n4. Iesire")
        print(35 * "=")

        optiune = input("Introduceti optiune: ")
        # Apelarea optiunii corespunzatoare input-ului
        if optiune in dict_optiuni:
            dict_optiuni[optiune]()
        else:
            print("Nu ati introdus o optiune valida.")

if __name__ == "__main__":
    main()