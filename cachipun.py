#Patricio Carrasco
iimport random
import sys

usuario = sys.argv[1].lower() #funcion para minusculas
opciones = ['piedra', 'papel', 'tijera'] #Definimos los posibles valores a elegir
entra_al_juego = usuario in opciones 
computador =  random.choice(opciones) 

print('-'*60)

if entra_al_juego == False:
   print('Argumento inválido: Debe ser piedra, papel o tijera.')
#En caso contrario, la opcion ingresada es correcta
#Usuario Empata:
elif usuario == computador:
   print(f'Tu jugaste {usuario} \nComputador jugó {computador} \nEmpate!!')
#Usuario gana:
elif (usuario == 'piedra' and computador == 'tijera') or (usuario == 'papel' and computador == 'piedra') or (usuario == 'tijera' and computador == 'papel'):
   print(f'Tu jugaste {usuario} \nComputador jugó {computador} \nGanaste!!')
#Usuario Pierde:
else: print(f'Tu jugaste {usuario} \nComputador jugó {computador} \nPerdiste!!')
print('-'*60)
