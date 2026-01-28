#Função de potencia de um numero
power = lambda x, y: x ** y
print(power(2, 3))  # Saída: 8  
#Função de soma de dois numeros
add = lambda a, b: a + b  
print(add(5, 7))    # Saída: 12

#Função que verifica se um numero é par
is_even = lambda num: num % 2 == 0   
print(is_even(4))   # Saída: True
print(is_even(5))   # Saída: False
#Função que retorna o maior entre dois numeros
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))  # Saída: 20
print(max_num(30, 15))  # Saída: 30
#Função que concatena duas strings
concat = lambda str1, str2: str1 + " " + str2
print(concat("Hello", "World"))  # Saída: "Hello World"