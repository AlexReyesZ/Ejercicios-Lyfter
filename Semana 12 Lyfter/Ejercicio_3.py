from datetime import date

#THE CLASS
class User:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date  

    @property
    def age(self):
        """Calculates the age based on the current year."""
        today = date.today()
        return today.year - self.birth_date.year

#THE DECORATOR
def adult_only(func):
    """Checks if the user is 18 or older before running the function."""
    def wrapper(user):
        if user.age < 18:
            raise PermissionError(f"Access Denied: {user.name} is a minor.")   # Raise an error to stop the process
        
        # If the user is an adult, execute the original function
        return func(user)
    return wrapper

# 3. THE IMPLEMENTATION
@adult_only
def enter_club(user):
    print(f"Welcome to the club, {user.name}! ")

# --- TESTING ---

# Example 1: Adult user
user_alex = User("Alex", date(1998, 11, 20))
enter_club(user_alex)

# Example 2: Minor user
user_justin = User("Justin", date(2015, 5, 20))

# enter_club(user_justin) # This line would raise a PermissionError