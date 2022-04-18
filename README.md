
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

## Functia vizualizare
Reprezinta submeniul de vizualizare, care contine urmatoarele optiuni:
    1. Vizualizare a tuturor angajatiilor in functie de departament
    2. Vizualizare a angajatiilor de pe un singur departament
    3. Iesire
    

### Vizualizare a tuturor angajatiilor in functie de departament
- Va afisa toti angajatii din baza de date impartiti pe departamente. Exemplu: 

```
===================================
            Vizualizare            
===================================
1. Vizualizare a tuturor angajatilor in functie de departament
2. Vizualizarea angajatilor dintr-un departament
3. Iesire la meniul principal
    
Introduceti optiunea dvs: 1
====================
HR
====================
---------------
Nume:  Maria Popescu
Position:  Site Manager
Data angajarii:  2020-07-12
Salary:  7600.0

---------------
Nume:  Anca Dimitrie
Position:  Contabil
Data angajarii:  2019-08-22
Salary:  5400.0

... (output omitted)

====================
IT
====================
---------------
Nume:  Adrian Popa
Position:  IT Helpdesk
Data angajarii:  2018-09-11
Salary:  5400.0

... (output omitted)


====================
Customer Relations
====================
---------------
Nume:  Ana Iordache
Position:  Customer Support Representative
Data angajarii:  2022-04-10
Salary:  3200.0

... (output omitted)
---------------
Nume:  Mircea Popa
Position:  Customer Support Representative
Data angajarii:  2022-04-08
Salary:  2980.0

---------------
Nume:  Maria Badescu
Position:  Customer Support Representative
Data angajarii:  2022-04-10
Salary:  3380.0
```


### Vizualizarea angajatilor pe un departament
- Va lua input de la user cu un departament si va afisa salariatii care corespund departamentului respectiv. Exemplu:
```
===================================
            Vizualizare            
===================================
1. Vizualizare a tuturor angajatilor in functie de departament
2. Vizualizarea angajatilor dintr-un departament
3. Iesire la meniul principal
    
Introduceti optiunea dvs: 2
Introduceti departamentul dorit: hr
---------------
Nume:  Maria Popescu
Position:  Site Manager
Data angajarii:  2020-07-12
Salary:  7600.0

---------------
Nume:  Anca Dimitrie
Position:  Contabil
Data angajarii:  2019-08-22
Salary:  5400.0

... (output omitted)
```


### Iesire
- va iesi la meniul principal din main

## Functia informatii_firma()
Reprezinta submeniul de vizualizare, care contine urmatoarele optiuni:
    1. Afisare medie salariala
    2. Afisare nr de angajati/ departament
    3. Afisare numar de angajati cu vechime mare mare de x ani
    4. Iesire
    
### Afisare medie salariala
- Va calcula media salariala pe toti angajatii din firma si o va afisa. Exemplu:
    ```
    ===================================
                Vizualizare            
    ===================================
    1. Afisare medie salariala.
    2. Afisare nr angajati/ departament
    3. Afisare nr de angajati cu vechime mai mare de x ani.
    4. iesire la meniul principal
        
    introduceti optiunea: 1
    Introduceti departamentul dorit [* pentru toate]: *
    Media salariilor pe departamentul * este: 4371.36
    ```
    
    ```
    ===================================
                Vizualizare            
    ===================================
    1. Afisare medie salariala.
    2. Afisare nr angajati/ departament
    3. Afisare nr de angajati cu vechime mai mare de x ani.
    4. iesire la meniul principal

    introduceti optiunea: 1
    Introduceti departamentul dorit [* pentru toate]: it
    Media salariilor pe departamentul it este: 5580.0
    ```
    
### Afisare nr de angajati/ departament
- Va afisa nr de angajati pe fiecare departament existent in firma. Exemplu:
    ```
    ===================================
                Vizualizare            
    ===================================
    1. Afisare medie salariala.
    2. Afisare nr angajati/ departament
    3. Afisare nr de angajati cu vechime mai mare de x ani.
    4. iesire la meniul principal

    Introduceti optiunea: 2
    --- HR: 5
    --- IT: 6
    --- Customer Relations: 11

    ```
### Afisarea angajatilor cu vechime mare mare de x ani
- Va lua input de la user cu nr de ani x
- Va calcula in functie de inputul de la utilizator cati angajati sunt in firma de mai mult timp. Exemplu:

    ```
    ===================================
                Vizualizare            
    ===================================
    1. Afisare medie salariala.
    2. Afisare nr angajati/ departament
    3. Afisare nr de angajati cu vechime mai mare de x ani.
    4. iesire la meniul principal

    Introduceti optiunea: 3
    Introduceti x: 1
    In firma sunt 4 angajati mai vechi de 1 an(i).
    ```
### Iesire 
- va iesi la meniul principal din main


## Functia adaugare_angajati()
- Se va lua input de la user cu datele necesare pentru a crea un obiet de tip angajat.
- Se va face update la fisierul 'angajati.csv' cu datele actualizate.

```
===================================
               Meniu               
===================================
1. Vizualizare
2. Informatii despre firma
3. Adaugare angajati
4. Iesire
===================================
Introduceti optiune: 3
Introduceti departamentul: HR
Introduceti numele angjatului: Maria Oprescu
Introduceti pozitia angajatului: Contabil
Introduceti data angajarii in formatul aaaa-ll-zz: 2022-04-12
Introduceti salariul: 4890
Angajat adaugat cu succes.
```

- Nu uitati sa tratati erorile. Exemplu: 

```
===================================
               Meniu               
===================================
1. Vizualizare
2. Informatii despre firma
3. Adaugare angajati
4. Iesire
===================================
Introduceti optiune: 3
Introduceti departamentul: abcd
Departament inexistent.
Introduceti departamentul: 
...
```

- Continutul fisierului dupa update:
```
HR;Maria Popescu;Site Manager;2020-07-12;7600.0
HR;Anca Dimitrie;Contabil;2019-08-22;5400.0
HR;Marian Cantemir;Talent reqruiter;2021-05-12;4200.0
IT;Adrian Popa;IT Helpdesk;2018-09-11;5400.0
IT;Adriana Milescu;Software Developer;2021-07-08;5700.0
IT;Maria Popovici;Software Developer;2021-06-22;5780.0
IT;Marius Petrila;DevOps Engineer;2018-07-12;6200.0
IT;Alexandru Milea;Junior DevOps;2021-10-11;4200.0
HR;Mihai Tomescu;Project Manager;2022-03-03;6800.0
HR;Ana-Maria Punga;Manager Assistant;2022-04-12;4800.0
Customer Relations;Ana Iordache;Customer Support Representative;2022-04-10;3200.0
Customer Relations;Adrian Tomescu;Customer Support Representative;2022-04-09;3280.0
Customer Relations;Mihnea Giuca;Customer Support Representative;2022-04-06;3370.0
Customer Relations;Adrian Damian;Senior Customer Support Representative;2022-04-10;3200.0
Customer Relations;Ana-Maria Popescu;Customer Support Representative;2022-04-10;3200.0
Customer Relations;Bogdan Iordache;Customer Support Representative;2022-04-10;3200.0
IT;Adrian Nemescu;Network Administrator;2022-02-22;6200.0
Customer Relations;Adrian Toma;Customer Support Representative;2022-04-11;3200.0
Customer Relations;Carina Tibu;Customer Support Representative;2022-04-12;3280.0
Customer Relations;Mihai Corici;Customer Support Representative;2022-04-10;1600.0
Customer Relations;Mircea Popa;Customer Support Representative;2022-04-08;2980.0
Customer Relations;Maria Badescu;Customer Support Representative;2022-04-10;3380.0
HR;Maria Oprescu;Contabil;2022-04-17;4980.0
```
- Puteti modifica fisierul cu ce doriti cu scopul de a testa functionalitatea acestuia.
