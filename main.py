# ============================================================
# Parcial 2 - Estructura de Datos I
# Código base final
# ============================================================


# ============================================================
# Punto 1: Lista Circular - Josephus modificado
# ============================================================

class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoCircular(dato)

        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            return

        actual = self.head
        while actual.next != self.head:
            actual = actual.next

        actual.next = nuevo
        nuevo.next = self.head

    def crear_lista(self, n):
        for i in range(1, n + 1):
            self.insertar_final(i)

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        resultado = []
        actual = self.head

        while True:
            resultado.append(str(actual.dato))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(resultado) + " -> (ciclo)")

    def josephus_modificado(self, m):
        """
        TODO:
        Implementar el algoritmo de Josephus con la regla:
        - Eliminar cada m-ésimo nodo
        - Si el eliminado es múltiplo de 5, saltar el siguiente
        - Continuar hasta que quede uno solo
        - Retornar el valor del nodo sobreviviente
        """
        current = self.head
        previous = None

        while current.next!= null and head.current!= null:
            for i in range :m-1
            current = current
            current = current.next
            eliminate = current.data

            if head = null:
                current = current.next
                previous.next = current.next
                current.next = previous
            if eliminate % 5 == 0:
                previous = current
                current = current.next
            return current    



# ============================================================
# Punto 2: Lista Simple - Método único
# ============================================================

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaSimple:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoSimple(dato)

        if not self.head:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        print(" -> ".join(resultado) + " -> None")

    def partir_voltear_intercalar(self):
        """
        TODO (ÚNICO MÉTODO A IMPLEMENTAR):

        Dada una lista simplemente enlazada:

        1. Dividir la lista en dos mitades
           - Si es impar, el nodo central queda en la primera mitad
           - NO calcular tamaño
           - Usar punteros (lento/rápido)

        2. Invertir la segunda mitad
           - Solo manipular punteros
           - No usar estructuras auxiliares

        3. Intercalar ambas listas
           - Alternar nodos de primera mitad y segunda invertida
           - No crear nodos nuevos

        4. Actualizar self.head con el resultado final

        Restricciones:
        - No modificar valores
        - No usar listas, arreglos, pilas, etc.
        - Solo usar referencias (.next)
        """
        slow = self.head
        fast = self.head
        prev = None
        while fast.next = None and fast.next.next = null:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        Intercalar = Slow.next
        slow.next = None
        current = slow.next
        prev = None
        while current != null:
            next_node = current.next
            current.next = prev
            prev = current
            current = next


# ============================================================
# Pruebas base
# ============================================================

if __name__ == "__main__":

    print("===== Punto 1 =====")
    lista_c = ListaCircular()
    lista_c.crear_lista(7)
    lista_c.mostrar()

    sobreviviente = lista_c.josephus_modificado(3)
    print("Sobreviviente:", sobreviviente)


    print("\n===== Punto 2 =====")
    lista_s = ListaSimple()

    for x in [1, 2, 3, 4, 5, 6]:
        lista_s.insertar_final(x)

    lista_s.mostrar()

    lista_s.partir_voltear_intercalar()

    print("Resultado:")
    lista_s.mostrar()