lista_n = list()
lista_t = list()
agenda = dict()
while True:
    entr = input('Ingresa nombre y numero de telefono y escribe fin para terminar')
    if entr == 'fin': break
    ls =entr.split()
    n = ls[0]
    t = ls[1]
    lista_n.append(n)
    lista_t.append(t)
agenda = zip(lista_n, lista_t)

for nombre, telefono in agenda:
    if input('Buscar por nombre: ') == nombre:
        print(telefono)
    break