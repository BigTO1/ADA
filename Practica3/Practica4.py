import random, math, time

puntos = []
puntosMasCercanos = [None] * 2;
distanciaMasCorta = 10000
n = 10000
tiempoInicio = time.time()
for i in range (n):
    punto = [random.randint(-10,10),random.randint(-10,10)]
    puntos.append(punto)

for i in range(len(puntos)):
    for j in range(i+1,len(puntos)):
        x = math.sqrt((puntos[i][0] - puntos[j][0])**2 + (puntos[i][1] - puntos[j][1])**2 )
        if( x < distanciaMasCorta ):
            distanciaMasCorta = x
            puntosMasCercanos[0] = puntos[i]
            puntosMasCercanos[1] = puntos[j]

tiempoFin = time.time()
tiempoEjecucion = tiempoFin  - tiempoInicio
print(f"Puntos más cercanos {puntosMasCercanos}")   
print(f"El tiempo de ejecución para {n} puntos son {tiempoEjecucion} segundos")