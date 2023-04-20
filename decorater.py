def add_print_to(original):
    def wrapper():
        print("Start Here")
        original()
        print("End Here")
    return wrapper

@add_print_to
def print_hello():
    print("Hello!")
    


print_hello()
