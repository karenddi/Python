# Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
#
# Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
# Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
#
# Pracownik powinien mieć pole typu boolowskiego zawierające status studenta.
# Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
#
# Wszyscy pracownicy mają wspólną nazwę firmy.
# Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy.

class Employee:

    def __init__(self, job, salary, name, surname, seniority):

        self.job = job
        self.salary = salary
        self.name = name
        self.surname = surname
        self.seniority = seniority

    def payrise(self):

        new_salary = (self.salary * 1.2)
        return new_salary

    def tax(self):

        tax_measure = self.salary()




if __name__ == "__main__":


    employee_1 = Employee("barista", 2000, "Jola", "McDonald", 2)
    print(employee_1.payrise())