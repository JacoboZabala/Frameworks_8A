import random
 
for _ in range(100):
    
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    

    if dado_1 == dado_2:
        if dado_1 == dado_2:
            print("Han habido dos pares consecutivos")
            print("El juego ha finalizado")
            print("Lanzando los dados")
            print("El resultado es")
            print(dado_1)
            print(dado_2)

    elif dado_1 != dado_2:
        print("Lanzando los dados")
        print("El resultado es")
        print(dado_1)
        print(dado_2)
