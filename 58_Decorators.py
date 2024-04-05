def greet(info):
    def _greet(*args, **kwargs):
        print("Let's add these numbers")
        info(*args, **kwargs)
        print("Hope you find it useful!")
    return _greet
    

@greet
def info(a, b):
    print(f"{a} * {b} = {a*b}")

info(234, 2342)