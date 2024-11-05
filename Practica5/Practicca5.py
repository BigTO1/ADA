def max_area(altura):
    izquierda = 0
    derecha = len(altura) - 1
    max_area = 0

    while izquierda < derecha:
        # Calcula el área actual
        area_actual = min(altura[izquierda], altura[derecha]) * (derecha - izquierda)
        # Actualiza el área máxima si se encuentra una mayor
        max_area = max(max_area, area_actual)

        # Mueve el puntero de la línea de menor altura
        if altura[izquierda] < altura[derecha]:
            izquierda += 1
        else:
            derecha -= 1

    return max_area

alturas = [3, 1, 4, 7, 2, 5, 6, 8, 3, 9, 4, 6]
mayorAgua = max_area(alturas)

print(f"La mayor cantidad de liquido que se puede almacenar es: {mayorAgua}")