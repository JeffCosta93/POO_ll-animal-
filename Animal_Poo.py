class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Som genérico de animal.")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} ({self.raca}): Au Au!")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.cor = cor

    def fazer_som(self):
        print(f"{self.nome} ({self.cor}): Miau Miau!")


animal_generico = Animal("")
cachorro = Cachorro(nome="Thor", raca="Labrador")
gato = Gato(nome="Joe", cor="Cinza")

# Chamando o método fazer_som de diferentes objetos
animal_generico.fazer_som()  # Som genérico de animal.
cachorro.fazer_som()  # Labrador: Au Au!
gato.fazer_som()  # Cinza: Miau Miau!
