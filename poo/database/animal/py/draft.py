class Animal:
    def __init__(self, species: str, sound: str): # construtor
        self.species: str = species # atributos
        self.age: int = 0
        self.sound: str = sound
    
    def ageBy(self, increment: int) -> None:
        self.age += increment
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            self.age = 4
        
    def makeSound(self):
        if self.age == 0:
            print("---")
        elif self.age == 4:
            print("RIP")
        else:
            print(self.sound)


    def __str__(self) -> str: # toString
        return f"{self.species}:{self.age}:{self.sound}"


def main(): 
    animal: Animal = Animal("","") # 2: criar um obj com qq valor inicial
    while True: # 3: loop infinito

        line: str = input() # 4: perguntar ao usuario
        print("$" + line) # echo
        args: list[str] = line.split(" ") # 5: separar argumentos

        if args[0] == "end":
            break
        elif args[0] == "init": # color size
            species: str = args[1]
            sound: str = args[2]
            animal = Animal(species, sound)
        elif args[0] == "show":
            print(animal)
        elif args[0] == "grow":
            animal.ageBy(int(args[1]))
        elif args[0] == "noise":
            animal.makeSound()
        else: # 7: erro
            print("fail: comando não encontrado")

main() # passo 1