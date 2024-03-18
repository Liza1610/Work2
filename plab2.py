#Kana_Hosoya NIU:1667774
#Lizbeth_Aquino NIU 1664021

#print("Este programa es parecido al juego WORDLE ")
#print("Empieza una partida")

llista=["perro","queso","fecha"]
import random
num=random.randrange(0, 2)



pal=llista[num]
palabra=input("ingresa una palabra con 5 letras: ")
len(palabra) != 5 

    print("Longitud incorrecta")
if palabra==pal:
    print("si")
else:
    print("chao")

