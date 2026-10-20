user_logged_in=False

def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise PermissionError('User not autenticated')
        
        return func(*args, **kwargs)
    return wrapper

@requires_login
def view_profile():
    print(' Showing user profile details...')

#---Testing---

user_logged_in = False
try:
    view_profile()
except PermissionError as e:
    print(f"Error: {e}")

user_logged_in = True
view_profile()