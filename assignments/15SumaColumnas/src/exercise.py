def crearmatriz():
    Lista = []
    Fila = int(input())
    Columna = int(input())
    if Fila > 0 and Columna > 0:
        for i in range(Fila):
            Lista.append([])
            for y in range(Columna):
                x = int(input())
                Lista[i].append(x)
    else:
        print('Error')
    return Lista

def main():
    Matriz = crearmatriz()
    Lista_col = []
    if len(Matriz) > 0:
        for i in range(len(Matriz[0])):
            count = 0
            for y in range(len(Matriz)):
                count += Matriz[y][i]
            Lista_col.append(count)
        print(Lista_col)


if __name__=='__main__':
    main()
