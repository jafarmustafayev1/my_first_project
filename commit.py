
def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Committing changes...")
        print("Connection closed.")
        return result
    return wrapper
