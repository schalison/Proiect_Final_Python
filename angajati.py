from departament import Departament

class Angajat(Departament):
    # Variabila de clasa care va contine obiecte de tip Angajat
    lista_angajati = []

    def __init__(self, workdep, empname, job, hiredate, salary):
        """ Constructorul clasei Angajat. """
        super().__init__(workdep)
        self.empname = empname
        self.job = job
        self.hiredate = hiredate
        self.__salary = salary

    @ classmethod
    def load_angajati(cls, nume_fisier):
        """ Creeaza obiecte de tip Angajat si le adauga in lista_angajati, bazate
        pe informatiile din fisierul nume_fisier. """
        pass

    @ classmethod
    def update_fisier(cls):
        """ Updateaza fisierul 'angajati.csv' cu informatiile actuale din lista_angajati. """
        pass
