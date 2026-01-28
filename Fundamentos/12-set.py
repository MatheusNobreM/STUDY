filmSet= {"pulp fiction", "matrix", "star wars", "clube da luta"}
filmeSet2= {"star wars", "vingadores", "homem aranha"}

Filme = filmSet.union (filmeSet2)
print(Filme)
Filme2 = filmSet.intersection (filmeSet2)
print(Filme2) 
Filme3 = filmSet.difference (filmeSet2)
print(Filme3)
Filme4 = filmSet.symmetric_difference (filmeSet2)
print(Filme4)
filmSet.add ("interestelar")
print(filmSet)  
filmSet.remove ("matrix")
print(filmSet)  
filmSet.clear()
print(filmSet)  