# POR QUÉ: Usamos '__' (double underscore) para ENCAPSULAMIENTO.
# Esto hace que el balance sea "privado". Nadie puede hacer 
# 'account.__balance = 1000000' desde fuera por seguridad.

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance=initial_balance

    def deposit(self, amount):
        if amount >0:
            self.__balance+=amount
            print(f'Deposited: ${amount}. Current balance: ${self.__balance}')
# POR QUÉ: Validamos que el monto sea positivo antes de sumar.
    
    def withdraw(self, amount):
        if 0 <amount <= self.__balance:
            self.__balance -=amount
            return True
        return False
# POR QUÉ: Verificamos si hay dinero suficiente antes de restar.

    def get_balance(self):
        return self.__balance
# POR QUÉ: Como el balance es privado, necesitamos un "Getter"
# para que el usuario pueda ver su saldo sin modificarlo.



class SavingAccount(BankAccount):
    def __init__(self, initial_balance, min_balance):
        super().__init__(initial_balance)
        self.min_balance=min_balance
# POR QUÉ: super() inicializa la parte de 'BankAccount'.
# No queremos reescribir la lógica del balance, solo extenderla.
    
    
    def withdraw(self, amount):
        if (self.get_balance() - amount) >= self.min_balance:
            return super().withdraw(amount)
        else:
            print(f'Denied: Must keep at least ${self.min_balance}')
            return False
        

# --- TESTING AREA ---
print("--- Testing Savings Account ---")
# Creamos una cuenta con $500 y un mínimo de $100
my_account = SavingAccount(500, 100)

print(f"Initial Balance: ${my_account.get_balance()}")

# Intento 1: Retirar mucho (Debe fallar)
print("\nAttempting to withdraw $450...")
my_account.withdraw(450) 

# Intento 2: Retirar poco (Debe funcionar)
print("\nAttempting to withdraw $100...")
my_account.withdraw(100)