class Flight():
    #función para determinar la capacidad total del vuelo
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers= []

    #función para añadir los datos de los pasajeros
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    #función para determinar la capacidad
    def open_seats(self):
        return self.capacity - len(self.passengers)

#flight se considera el objeto de la clase Flight y la iniciamos dandole el valor 3
#para determinar la capacidad total del vuelo
flight = Flight(3)
#people son los nombres de las personas que van a coger el vuelo
people = ["Harry", "Ron", "Hermione", "Ginny"]
#Utilzamos el bucle for para añadir las personas del vuelo según la capacidad total
for person in people:
    #forma uno del if
    """ success = flight.add_passenger(person)
    if success:
        print(f"Añadido {person} al vuelo exitosamente.") """

    #Forma mas correcta del if
    if flight.add_passenger(person):
        print(f"Añadido {person} al vuelo exitosamente.")
    else:
        print(f"No hay asiento para {person}, lo sentimos")

