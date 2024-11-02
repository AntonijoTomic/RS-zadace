lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def grupiraj_po_paritetu(lista):
    dict = {
        "parni": [],
        "neparni": []
    }
    for num in lista:
        if num % 2 == 0:
            dict["parni"].append(num)
        else:
            dict["neparni"].append(num)
    
    return dict

print(grupiraj_po_paritetu(lista))