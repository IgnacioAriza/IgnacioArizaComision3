from Motorbike import Motorbike

motorbike_1 = Motorbike("rojo","123aa4",10,2,"abgui","retcher","12/12/12",120,120)

motorbike_2 = Motorbike("nefgro","123aa4",10,2,"abgui","retcher","12/12/12",120,80)

motorbike_1.start()
motorbike_2.stop()
motorbike_1.start()
motorbike_1.stop()

motorbike_1.price = 1200

print("El precio de la motocicleta", motorbike_1.brand, motorbike_1.model, "es de $", motorbike_1.price)

motorbike_1.price_check()
#motorbike_2.price_check() hacer esto da error porque no existe el atributo precio es esta instancia del objeto