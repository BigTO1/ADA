word = "aaaaaaaaaaaaaabb"
comp = ""
palabra = word
while( len(word) > 0):
    caracter = word[0]
    contador = 0
    for char in word:
        if( char == caracter):
            contador+=1
        else:
            break
    word = word[contador:]
    if(contador > 9):
        comp = comp + "9" + caracter
        contador-=9
    comp = comp + str(contador) + caracter 

print(f"La composición para {palabra} es: {comp} ")


