class Currency:
  def __init__ (self):
    self.peso = 1
    self.dolar = 1
  def peso_to_dolar(self,peso):
      return ((peso * 0.00026))
  def dolar_to_peso(self,dolar):
      return ((dolar * 3908.75))

while True:
    
    converter_currency = Currency()
    print ("Currency converter")
    nombre = input("Write your name: ")
    print ("Enter the currency to convert")
    print("TODAY 1 USD = 3.908,75 COP")
    print("1. COP to USD")
    print("2. USD to COP")
    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        print("Your selection is COP to USD")
        print("Peso Colombiano: ")
        peso = float(input("$"))
        dolar = converter_currency.peso_to_dolar(peso)
        print("$", dolar)

    elif user_choice == 2:
        print("Your selection is USD to COP")
        print("Dolar estadounidense: ")
        dolar = float(input("$"))
        peso = converter_currency.dolar_to_peso(dolar)
        print("$", peso)
    