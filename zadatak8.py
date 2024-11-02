lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def filtriraj_parne(lista):
  
    for num in lista:
        if num % 2 != 0 :
            lista.remove(num)
    return lista

print(filtriraj_parne(lista))
