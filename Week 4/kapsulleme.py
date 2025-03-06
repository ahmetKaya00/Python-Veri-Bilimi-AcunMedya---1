class BankaHesabi:
    def __init__(self,bakiye):
        self.__bakiye = bakiye
    
    def bakiye_goster(self):
        print(f"Bakiyeniz: {self.__bakiye} TL")