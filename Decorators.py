def hello(name="Meliksah"):
    print("The hello() function has been executed!")
    
    def greet():
        print("\t This is the greet() function inside hello!")
        
    def welcome():
        print("\t This is welcome() inside hello!")
        
    print("This is going to return a function!")
    
    if name == "Meliksah":
        return greet
    else:
        return welcome

my_new_func = hello("Meliksah")        
hello()
my_new_func()


def cool():
    
    def super_cool():
        print("I am very cool!")
        
    return super_cool

my_func = cool()
my_func()


def hello():
    print("Hello Meliksah!")
    
def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())
    
other(hello)


def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code, after the original function")
    return wrap_func

def func_needs_decorator(): #1st way
    print("I want to be decorated :)")
    
decorated_func = new_decorator(func_needs_decorator)

decorated_func()

@new_decorator #2nd way
def func_needs_decorator():
    print("I want to be decorated :)")
    
decorated_func()




















