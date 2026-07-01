class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Brazo derecho (quién sigue)
        self.prev = None  # Brazo izquierdo (quién está atrás)

class Deque:
    def __init__(self):
        self.head = None  # Puerta de entrada izquierda
        self.tail = None  # Puerta de entrada derecha

    def push_right(self, data):
        new = Node(data)
        if not self.head:
            self.head = self.tail = new
        else:
            new.prev = self.tail # El nuevo agarra al viejo último
            self.tail.next = new # El viejo último agarra al nuevo
            self.tail = new      # El nuevo es ahora el final

    def push_left(self, data):
        new = Node(data)
        if not self.head:
            self.head = self.tail = new
        else:
            new.next = self.head # El nuevo agarra al jefe actual
            self.head.prev = new # El jefe actual agarra al nuevo
            self.head = new      # El nuevo es el nuevo jefe

    def pop_left(self):
        if self.head:
            if self.head == self.tail: # Solo hay uno
                self.head = self.tail = None
            else:
                self.head = self.head.next # El segundo pasa a ser primero
                self.head.prev = None      # Suelta la mano del que se fue

    def pop_right(self):
        if self.tail:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev # El penúltimo pasa a ser último
                self.tail.next = None      # Suelta la mano del que se fue

    def show(self):
        curr = self.head
        while curr:
            print(f"[{curr.data}]", end=" <-> ")
            curr = curr.next
        print("Empty")

# --- EXECUTION / TEST ---
dq = Deque()

print("--- Agregando datos ---")
dq.push_right("C")  # [C]
dq.push_right("D")  # [C] <-> [D]
dq.push_left("B")   # [B] <-> [C] <-> [D]
dq.push_left("A")   # [A] <-> [B] <-> [C] <-> [D]
dq.show()           # Resultado esperado: [A] <-> [B] <-> [C] <-> [D]

print("\n--- Quitanto extremos ---")
dq.pop_left()       # Quita [A]
dq.pop_right()      # Quita [D]
dq.show()           # Resultado esperado: [B] <-> [C]

print("\n--- Vaciando el Deque ---")
dq.pop_left()       # Quita [B]
dq.pop_left()       # Quita [C]
dq.show()           # Resultado esperado: Empty