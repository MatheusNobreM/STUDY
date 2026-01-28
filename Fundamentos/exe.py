p1 = input("")
v1 = float(input(""))
p2 = input("")
v2 = float(input(""))
p3 = input("")
v3 = float(input(""))

dictt = {p1:v1,p2:v2,p3:v3}

print(dictt)
maior = max(dictt, key=dictt.get)
print(f"{maior:.2f}")
media = sum(dictt.values())/len(dictt)

print(f"{media:.2f}")
