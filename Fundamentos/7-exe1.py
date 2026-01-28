# nome = input("Digite seu nome: ")
# print(nome[::-1])

x = "arara"
y = "revi"

texto1 = x.lower().replace(" ", "")
texto2 = y.lower().replace(" ", "")
palindrome = texto1 == x[::-1]
palindrome2 = texto2 == y[::-1]
print(f"{x} é um palíndromo? {palindrome}")
print(f"{y} é um palíndromo? {palindrome2}")