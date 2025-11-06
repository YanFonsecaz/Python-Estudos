class Contador:
    def __init__(self, inicio,fim):
        self.atual = inicio
        self.fim = fim

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.atual > self.fim:
            raise StopIteration
        valor =self.atual
        self.atual += 1
        return valor
    
for numero in Contador(1,5):
    print(numero)

class Contador2:
    def __init__(self,num):
        self.num = num
        self.inicio = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.inicio >= len(self.num):
            raise StopIteration
        valor = self.num[self.inicio]
        self.inicio += 1
        return valor

for numero in Contador2([0,20,30,40]):
    print(numero)