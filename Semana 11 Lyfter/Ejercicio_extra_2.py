from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name):
        self.name=name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    def get_role(self):
        return 'ADMIN'
    
    def has_permission(self, permission):
        return True
    

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.allowed_permissions = ["read", "view_profile"]


    def get_role(self):
        return 'Regular User'
    
    def has_permission(self, permission):
        return permission in self.allowed_permissions
    


#Test
user1 = AdminUser('Alex')
user2 = RegularUser('Antonio')

print(f'User: {user1.name} | Role: {user1.get_role()}')
# Corregido: usamos comillas dobles afuera y simples adentro
print(f"Can delete? {user1.has_permission('delete')}") 

print('-' * 30)

print(f"User: {user2.name} | Role: {user2.get_role()}")
print(f"Can delete? {user2.has_permission('delete')}") 
print(f"Can read? {user2.has_permission('read')}")

