class Towel:
    def __init__(self,color:str, size: str): # construtor
        self.color: str = color #atributo
        self.size: str = size
        self.wetnees: int = 0

print('Qual a cor da sua toalha?')
color = input()
print('Qual o tamanho da sua toalha?')
size = input()
towel: Towel = Towel(color, size)


print(f"Sua toalha é {towel.color} e do tamanho {towel.size}")
