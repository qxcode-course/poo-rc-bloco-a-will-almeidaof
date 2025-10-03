# |    Cauculator    |
# |------------------|
# | battery: int     |
# | maxBattery: int  |
# | display: float   |
# --------------------



# Contruindo classe Calculator

class Calculator:
  def _init_(self, maxBattery: int):
    self.battery:    int   = 0;
    self.maxBattery: int   = maxBattery;
    self.display:    float = 0.00;

  def _str_(self) -> str:
    return f"display = {self.display:.2f}, battery = {self.battery}";

  def charge (self, value: int):
    self.battery += value;
    if self.battery > self.maxBattery:
      self.battery = self.maxBattery;

  def sum(self, a: float, b: float):
    if self.battery == 0:
      print("fail: bateria insuficiente");
    
    else:
      self.display = a + b;
      self.battery -= 1;

  def division(self, num: float, den:float):
    if self.battery == 0:
      print("fail: bateria insuficiente");

    elif den == 0:
      print("fail: divisao por zero");
      self.battery -= 1;

    else:
      self.display = num / den;
      self.battery -= 1;

# Contrindo função main()

def main():
  calculator: Calculator = Calculator();

  while True:
    line: str = input();
    args: list[str] = line.split(" ");
    
    print(f"${line}");

    match args[0]:
      case "init":
        calculator.maxBattery = int(args[1]);
        calculator.battery = 0;
        calculator.display = 0;
      
      case "show":
        print(calculator);

      case "charge":
        calculator.charge(int(args[1]));

      case "sum":
        calculator.sum(int(args[1]), int(args[2]));

      case "div":
        calculator.division(int(args[1]), int(args[2]));
      
      case "end":
        break;

      case _:
        print("error: comando não encontrado");

main();