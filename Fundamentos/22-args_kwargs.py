"""
*args - usado para passar uma quantidade variável de argumentos não nomeados para uma função.
**kwargs - usado para passar uma quantidade variável de argumentos nomeados (chave-valor) para uma função.
"""

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all(1, 2, 3, 4, 5))  # Saída: 15

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Saída:
# name: Alice