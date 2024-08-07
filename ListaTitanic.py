import csv

class Pasajero:
    def __init__(self, PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked):
        self.PassengerId = int(PassengerId)
        self.Survived = int(Survived)
        self.Pclass = int(Pclass)
        self.Name = Name
        self.Sex = Sex
        self.Age = round(float(Age)) if Age else 0
        self.SibSp = int(SibSp)
        self.Parch = int(Parch)
        self.Ticket = Ticket
        self.Fare = float(Fare)
        self.Cabin = Cabin
        self.Embarked = Embarked

    def __str__(self):
        return f"{self.PassengerId} {self.Name} {self.Age} {self.Pclass}"
    
    
    
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def ListarPasajeros(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            return
        else:
            a = self.cabeza
            while a.siguiente:
                a = a.siguiente
            a.siguiente = nuevo_nodo

    def LeerCsv(filename):
        pasajeros = Lista()
        with open(filename, 'r', encoding='utf-8') as csvFile:
            reader = csv.DictReader(csvFile, delimiter=',')
            for row in reader:
                pasajero = Pasajero(
                    PassengerId=row['PassengerId'],
                    Survived=row['Survived'],
                    Pclass=row['Pclass'],
                    Name=row['Name'],
                    Sex=row['Sex'],
                    Age=row['Age'].replace(", ", " . ") if row['Age'] else '0',
                    SibSp=row['SibSp'],
                    Parch=row['Parch'],
                    Ticket=row['Ticket'],
                    Fare=row['Fare'],
                    Cabin=row['Cabin'],
                    Embarked=row['Embarked']
                )
                pasajeros.ListarPasajeros(pasajero)
        return pasajero

    def Mostrar(self):
        a = self.cabeza
        while a:
            print(a.dato, end=(" -> "))
            a = a.siguiente
        print("None")

a = Lista()
file_path = 'Titanic.csv'
lista_pasajeros = Lista.LeerCsv(file_path)

print(type(lista_pasajeros))
lista_pasajeros.Mostrar()
