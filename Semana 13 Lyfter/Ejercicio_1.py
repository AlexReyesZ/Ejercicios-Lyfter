class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Apunta al plato que tiene abajo

class Stack:
    def __init__(self):
        self.top = None   # El plato que está arriba de todo

    def push(self, data):
        new_node = Node(data)
        # El nuevo plato ahora sostiene al que antes estaba arriba
        new_node.next = self.top 
        # Ahora el nuevo plato es el que está arriba
        self.top = new_node

    def pop(self):
        if self.top is not None:
            # Quitamos el de arriba moviendo el puntero al de abajo
            self.top = self.top.next

    def show(self):
        current = self.top
        while current:
            print(f"[{current.data}]")
            current = current.next
        print("-"*6)

# --- PRUEBA ---
stc = Stack()
stc .push("Plato A")
stc .push("Plato B")
stc .push("Plato C")
stc .show()  # Muestra C arriba y A abajo
stc .pop()
stc .show()  # Solo queda A y B