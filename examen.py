
def calcular_objetivo_ml(peso, actividad):
    objetivo = peso * 35

    if actividad == "bajo":
        objetivo = objetivo * 0.9
    elif actividad == "medio":
        objetivo = objetivo
    elif actividad == "alto":
        objetivo = objetivo * 1.1
    else:
        print("actividad no valida")
    
    return objetivo

def estado_hidratacion(consumo, objetivo):
    if consumo < objetivo:
        falta = ((objetivo - consumo) / objetivo) * 100
        return "te falta " + str(int(falta)) + "% para llegar"
    elif consumo == objetivo:
        return "alcanzaste tu objetivo"
    else:
        exceso = ((consumo - objetivo) / objetivo) * 100
        return "te pasaste en " + str(float(exceso)) + "%."


personas = []

while True:
    try:
        print("\nNueva persona")

        peso = float(input("Peso en kg: "))
        actividad = input("Actividad (bajo, medio, alto): ")
        consumo = float(input("Agua consumida en ml: "))

        objetivo = calcular_objetivo_ml(peso, actividad)
        mensaje = estado_hidratacion(consumo, objetivo)

        persona = {
            "peso": peso,
            "actividad": actividad,
            "consumo": consumo,
            "objetivo": objetivo,
            "mensaje": mensaje
        }

        personas.append(persona)

        print("Objetivo:", objetivo, "ml")
        print(mensaje)

        seguir = input("¿Cargar otra persona? (s/n): ")
        if seguir != "s":
            break

    except:
        print("Error: ingresaste mal un dato")


print("\nResumen final:")

for persona in personas:
    print("Persona:")
    print("Peso:", persona["peso"], "kg")
    print("Actividad:", persona["actividad"])
    print("Consumo:", persona["consumo"], "ml")
    print("Objetivo:", persona["objetivo"], "ml")
    print("Estado:", persona["mensaje"])