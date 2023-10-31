class Motorbike:
    new = True
    motor = False
    
    def __init__(self,color,plate,gas_liters,wheels_numbers,brand,model,manufacturing_date,top_speed,weight):
        self.color = color
        self.__plate = plate
        self.gas_liters = gas_liters
        self.wheels_number = wheels_numbers
        self.brand = brand
        self.__model = model
        self.manufacturing_date = manufacturing_date
        self.__top_speed = top_speed
        self.__weight = weight
        
    def start(self):
        if self.motor:
            print("La moto ya esta andando")
        else:
            self.motor = True
            print("La moto arranco")
            
    def stop(self):
        if not self.motor:
            print("La moto ya esta parada")
        else:
            self.motor = False
            print("La moto se detuvo")
    
    @property
    def model(self):
        return self.__model
    
    def price_check(self):
        print("El precio de la motocicleta", self.brand, self.model, "es de $", self.price)