lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

def ukloni_duplikate(lista):
  
    lista2 = []
    for num in lista:
        if num not in lista2:
            lista2.append(num)
    return lista2

print(ukloni_duplikate(lista))
