class Calculadora:
    def __init__(self,batterymax: int):
        self.display: float = 0
        self.battery: int = 0
        self.batteryMax: int = batterymax

    def __str__(self) -> str:
        return f"{self.display}:{self.battery}:{self.batteryMax}"
    