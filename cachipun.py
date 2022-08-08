#Patricio Carrasco
import random , sys

opciones = ["piedra", "papel", "tijera"]
opcion_comp = random.choice[opciones]
opcion_usr = sys.argv[1]

if opcion_comp == opcion_usr:
    print(f" tu opcion fue: {opcion_usr} y el compu: {opcion_comp}, EMPATARON ")
elif (opcion_comp == "piedra" and opcion_usr =="tijera") or (opcion_comp == "papel" and opcion_usr == "piedra") or (opcion_comp=="tijera" and opcion_usr"papel"):
    print(f"gano el computador con {opcion_comp} y tu con {opcion_usr}")
else: 
    print("gano el usuario con {opcion_usr} y computador con {opcion_comp}")
