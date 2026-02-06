from decorator import my_decorator, split_string, upper_case_decorator


@my_decorator
def my_function():
    print("Dentro da função")


my_function()


@upper_case_decorator
def text():
    return "Olá mundo!"


print(text())


@split_string
@upper_case_decorator
def text2():
    return "Olá mundo a todos!"


print(text2())
