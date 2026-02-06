def my_decorator(function):
    def wrapper():
        print("Antes de executar a função")
        function()
        print("Depois da função")

    return wrapper


def upper_case_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper
