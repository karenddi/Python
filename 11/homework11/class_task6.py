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

    def __init__(self, job, salary, name, surname, seniority, student):

        self.job = job
        self.salary = salary
        self.name = name
        self.surname = surname
        self.seniority = seniority
        self.student = student

    def payrise(self):

        new_salary = (self.salary * 1.2)
        return new_salary

    def salary_student(self):

        if self.student == True:
            print ( "You do not pay health insurance" )

            tax_measure = (self.salary * 0.2)
            salary_net = (self.salary - tax_measure)
            print ( "Your salary net is:", salary_net )
            return salary_net
        else:
            print("This employee is not a student!")

    def salary_normal(self):

        if self.student == False:

            tax_measure = (self.salary * 0.2)
            health_insurance_measure = (self.salary * 0.1)
            salary_net = (self.salary - tax_measure - health_insurance_measure)
            print("Your salary net is:", salary_net)
            return salary_net
        else:
            print("This employee is a student!")






    def email(self):

        full_name = (self.name + self.surname)
        full_name = full_name.lower()


        consonants = set("bcdfghjklmnpqrstvwxyz")

        my_consonants = []

        for x in full_name:
            if x in consonants:
                my_consonants.append(x)

        my_consonants = ''.join(map(str, my_consonants))


        employee_email = '{}@corplife.com'.format(my_consonants)
        print(employee_email)


if __name__ == "__main__":


    employee_1 = Employee("barista", 2000, "Jola", "McDonald", 2, False)
    employee_2 = Employee("accountant", 3500,"Hannah", "Kowalsky", 6, True)

    print(employee_1.payrise())
    employee_2.salary_student()
    employee_1.salary_student()
    employee_1.email()
