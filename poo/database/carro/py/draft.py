class Carro:
    def __init__(self):
        self.passageiros: int = 0
        self.kmp: int = 0
        self.gas: int = 0
        self.maxgas: int = 100
        self.maxpass: int = 2

    def Entrar(self):
        if self.passageiros < self.maxpass:
            self.passageiros += 1
        else:
            print('fail: limite de pessoas atingido')

    def Sair(self):
        self.passageiros -= 1
        if self.passageiros < 0:
            print('fail: nao ha ninguem no carro')
            self.passageiros = 0

    def Abastecer(self, gasolina: int) -> None:
        self.gas += gasolina
        if self.gas >= self.maxgas:
            self.gas = self.maxgas

    def Drive(self, gasto: int) -> None:
            if self.gas == 0:
                print("fail: tanque vazio")
            elif self.passageiros == 0:
                print("fail: nao ha ninguem no carro")
            elif self.gas < gasto:
                self.kmp += self.gas
                print(f"fail: tanque vazio apos andar {self.gas} km")
                self.gas = 0
            else:
                self.kmp += gasto
                self.gas -= gasto



    def __str__(self) -> str:
        return f"pass: {self.passageiros}, gas: {self.gas}, km: {self.kmp}"

def main():
    carro: Carro =  Carro()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "enter":
            carro.Entrar()
        if args[0] == "leave":
            carro.Sair()
        if args[0] == "fuel":
            carro.Abastecer(int(args[1]))
        if args[0] == "drive":
            carro.Drive(int(args[1]))
        if args[0] == "show":
            print(carro)

main()