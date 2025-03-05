class Pila:
    def __init__(self, capacidad): 
        self.stack = []
        self.capacidad = capacidad  

    def apilar(self, elemento):
        if self.esta_llena():
            print("La pila está llena. No se puede agregar más elementos.")
        else:
            self.stack.append(elemento)
            print(f"Se apiló: {elemento}")

    def desapilar(self):
        if not self.esta_vacia():
            elemento = self.stack.pop()
            print(f"Se desapiló: {elemento}")
        else:
            print("La pila está vacía.")

    def mostrar(self):
        print("Pila actual:", self.stack)

    def esta_vacia(self):
        return len(self.stack) == 0

    def esta_llena(self):
        return len(self.stack) >= self.capacidad



pila = Pila(3)

pila.apilar("22")
pila.apilar("25")
pila.apilar("30")
pila.apilar("40")  

pila.mostrar()

pila.desapilar()
pila.desapilar()

pila.mostrar()

pila.mostrar()

pila.desapilar()
pila.desapilar()

pila.mostrar()
