
# Python1_Proiect

Acesta este proiectul final Python1.

## Obiectiv: 
Se cere crearea unei aplicatii care sa ajute gestionarea angajatilor unei firme, pe baza unui fisier de tip csv.

Aplicatia va avea urmatoarea ierarhie de meniuri:

```
|__ 1. Vizualizare angajati
    |__ 1. Vizualizare a tuturor angajatilor in functie de departament
    |__ 2. Vizualizarea angajatilor dintr-un departament
    |__ 3. Iesire la meniul principal

|__ 2. Informatii firma
    |__ 1. Afisare medie salariala
    |__ 2. Afisare nr angajati/ departament
    |__ 3. Afisare nr de angajati cu vechime mai mare de x ani
    |__ 4. Iesire la meniul principal
    
|__ 3. Adaugare angajati

|__ 4. Iesire
```

## Cerinte:
- Implementarea functionalitatii fiecarei optiuni din meniu folosind scheletul de cod actual inventivitatea voastra.
- Documentatie sub forma unui fisier txt/pdf/GitHub in care se va explica functionalitatea fiecarei optiuni
- Scheletul de cod poate fi modificat la libera alegere: se pot adauga/ sterge functii in functie de cum considerati ca este necesar pentru a respecta cerintele aplicatiei.


# main.py
Contine: 
- Meniul principal
- functii corespunzatoare fiecarei optiuni din meniu

## Meniul principal cu cele 3 optiuni - COMPLET

    1. Vizualizare angajati
    2. Informatii despre firma
    3. Adaugare angajati
    4. Iesire

- Functiile sunt apelate in functie de input-ul utilizatorului folosind dictionarul dict_optiuni, care mapeaza fiecare optiune cu functia optiunii corespunzatoare

## Functia vizualizare() - //todo
Reprezinta submeniul de vizualizare, care contine urmatoarele optiuni:
    1. Vizualizare a tuturor angajatiilor in functie de departament
    2. Vizualizare a angajatiilor de pe un singur departament
    3. Iesire
    
Optiunea 1 - exemplu output:
```
|__ 1. Vizualizare angajati
    |__ 1. Vizualizare a tuturor angajatilor in functie de departament
    |__ 2. Vizualizarea angajatilor dintr-un departament
    |__ 3. Iesire la meniul principal

|__ 2. Informatii firma
    |__ 1. Afisare medie salariala
    |__ 2. Afisare nr angajati/ departament
    |__ 3. Afisare nr de angajati cu vechime mai mare de x ani
    |__ 4. Iesire la meniul principal
    
|__ 3. Adaugare angajati

|__ 4. Iesire
```
### Vizualizare a tuturor angajatiilor in functie de departament
- Va afisa toti angajatii din baza de date impartiti pe departamente. Exemplu: 
- Apeleaza metoda afisare_angajati() din clasa Angajat


### Vizualizarea angajatilor pe un departament
- Va lua input de la user cu un departament si va afisa salariatii care corespund departamentului respectiv. Exemplu:
- Apeleaza functia afisare_departament() din clasa Angajat cu parametrul inputului de la user


### Iesire
- va iesi la meniul principal din main

## Functia informatii_firma() //todo
    
    1. Afisare medie salariala
    2. Afisare nr de angajati/ departament
    3. Afisare numar de angajati cu vechime mare mare de x ani
    4. Iesire
    
### Afisare medie salariala
- Va calcula media salariala pe toti angajatii din firma si o va afisa. Exemplu:
    ```
    Media salariala actuala este: 3890 lei
    ```
### Afisare nr de angajati/ departament
- Va afisa nr de angajati pe fiecare departament existent in firma. Exemplu:
    ```
    HR: 4 angajati
    IT: 7 angajati
    Management: 2 angajati
    ```
### Afisarea angajatilor cu vechime mare mare de x ani
- Va lua input de la user cu nr de ani x
- Va calcula in functie de inputul de la utilizator cati angajati sunt in firma de mai mult timp. Exemplu:

    ```
    Introduceti x: 1
    Sunt 4 persoane in firma cu vechime mai mare de 1 an
    ```
### Iesire 
- va iesi la meniul principal din main


## Functia adaugare_angajati() //todo
- Se va lua input de la user cu datele necesare pentru a crea un obiet de tip angajat
- Se va apela metoda adaugare_angajat() din clasa Angajat, folosind parametrii luati ca input de la user
     
## Functia iesire() - COMPLETA
- functie care apeleaza functia exit() din modulul sys pentru a iesi din program
    
    ```
    def iesire():
    """ Functie care corespunde optiunii 4 din meniu. Foloseste functia exit() din modulul sys
    pentru a iesi din program"""

    print("La revedere!")
    sys.exit()
    ```
 # Angajati.py
 - contine clasa care deriva din clasa Departament 
 - Clasa Angajat contine:
    -- variabila de clasa angajati, care va contine toate obiectele de tip Angajat
    -- Constructorul
    -- Metoda de clasa load_angajati
    -- Metoda de clasa afisare_anagajati()
    -- Metoda de clasa afisare_departament()
    -- Metoda de clasa adaugare_angajat()
    -- Metoda de clasa update_fisier()
    
 ## Metoda load_angajati() - COMPLETA
 - Citeste fisierul angajati.txt si creaza obiecte de tip Angajat
 - Adauga obiectele create in lista de angajati

    ```
    @classmethod
    def load_angajati(cls):
        """
        Metoda de clasa care incarca si creaza obiecte de tip Angajat,
        dupa care le adauga in lista angajati:

        """
        #  -- Deschide fisierul "angajati.txt" si obtine o lista_angajati in formatul:
        #  ["HR/Maria Popescu/Manager/2020-7-12/7600","nume_dep/nume/post/data_angajarii/salar"]
        with open("angajati.txt") as f:
            lista_angajati = f.read().splitlines()

        # Parcurge lista obtinuta mai sus si imparte fiecare element in functie de "/".
        for angajat in lista_angajati:
            #  Se obtine lista ang in formatul:
            #  ["HR","Maria Popescu", "Manager",  "2020-7-12", "7600"]
            ang = angajat.split("/")

            # Converteste data angajarii din string in datetime.date, dandu-i split in functie de "-".
            # data_ang[1] va fi "2020", data_ang[2] va fi "7", data_ang[3] va fi "12"
            data_ang = ang[3].split("-")
            data_ang = datetime.date(int(data_ang[0]), int(data_ang[1]), int(data_ang[2]))

            # Creaza obiectul de tip Angajat cu parametrii dati
            cls.angajati.append(Angajat(ang[0], ang[1], ang[2], data_ang, float(ang[4])))

            # Daca departamentul nu exista, il va adauga in lista de departamente. Fara duplicate.
            if ang[0] not in [i.nume_dep for i in Departament.departamente]:
                departament = Departament(ang[0])
                Departament.departamente.append(departament)
    ```
    
 ## Metoda afisare_angajati() //todo
 - va fi apelata in main la optiunea 1 din meniul de vizualizare
 - va afisa fiecare angajat in functie de departament

      ```
    HR:
    Nume: John
    Functie: Manager HR
    Data angajarii: 2020-7-11
    Salar: 4500 lei
    
    IT:
    Nume: Ion
    Functie: Project Manager
    Data angajarii: 2021-3-22
    Salar: 4300
    
    Nume: Alina
    Functie: IT Helpdesk
    Data angajarii: 2021-5-3
    Salar: 3800
    ```
    
## Metoda afisare_departament() //todo
- Va afisa toti angajatii din departamentul introdus de catre utilizator

    ```
    Introduceti departamentul: it
    
    IT:
    Nume: Ion
    Functie: Project Manager
    Data angajarii: 2021-3-22
    Salar: 4300
    
    Nume: Alina
    Functie: IT Helpdesk
    Data angajarii: 2021-5-3
    Salar: 3800
    ```
 
 ## Metoda adaugare_angajat() //todo
- Se va crea si adauga obiectul de tip angajat la lista de angajati
- Challenge: se va da update la fisierul angajati.txt cu noul angajat, apeland metoda update_fisier()
    ```
     #Exemplu:
     Introduceti departamentul: curatentie
     Nu este un departament valid.
     Introduceti departamentul: hr
     Introduceti numele angajatului: Maria
     Introduceti postul: asistent
     Introduceti data angajarii in formatul aaaa-ll-zz: 2021-11-22
     Introduceti salariul: 3400
     Angajat adaugat cu succes!
     ```
     
 ## Metoda update_fisier() //todo
 - Se va da update la fisierul angajati.txt cu angajatii actuali din lista de angajati

# Departament.py
- Contine:
    -- variabila de clasa departamente, care contine obiectele de tip Departament
    -- metoda afisare_departamente()
    
## Metoda afisare_departamente()
- va afisa departamentele din firma
- Folositoare pentru a aduce utilizatorului la cunostiinta ce departamente sunt, cand doreste sa adauge un angajat nou. Exemplu:

    ```
    Departamentele actuale sunt:
        -- IT
        -- HR
       Introduceti un departament: 
    ```
    
    
# Fisierul angajati.txt
- contine angajatii in formatul 

```
Departament/Nume/Functie/Data angajarii/Salar

```
- Puteti modifica fisierul cu ce doriti cu scopul de a testa functionalitatea acestuia.
