class Car:

    car_general="brusco"
    car_numb=0
    ordine=[]


    def __init__(self,model,year,color,proprietario):
        self.model=model
        self.year=year
        self.color=color
        self.proprietario=proprietario
        Car.car_numb +=1
        Car.ordine.append(proprietario)


    def guida(self):
        print(f"stai guidando {self.model}")

    def stop(self):
        print(f"ti sei schiantato {self.model}")

    def descr(self):
        print(f"")