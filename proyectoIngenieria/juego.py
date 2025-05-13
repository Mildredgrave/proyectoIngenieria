import sys #para que me permita interactuar en la linea de comandos/ desde terminal
import random

def comparar(opcion1, opcion2):
    if opcion1 == opcion2:
        return "empate"
    elif (opcion1 == 'piedra' and opcion2 == 'tijera') or \
        (opcion1 == 'papel' and opcion2 == 'piedra') or \
        (opcion1 == 'tijera' and opcion2 == 'papel'):
        return "gano"
    else:
        return "perdio"

def main():
    if len(sys.argv) != 4:
        print("Debe ingresar 3 opciones válidas: piedra, papel o tijera.")
        sys.exit(1)

    opciones_validas = ['piedra', 'papel', 'tijera']
    humano_opciones = [opcion.lower() for opcion in sys.argv[1:]]

    for opcion in humano_opciones:
        if opcion not in opciones_validas:
            print(f"Opción inválida: {opcion}. Usa piedra, papel o tijera.")
            sys.exit(1)

    programa_opciones = [random.choice(opciones_validas) for _ in range(3)]
    print(f"El programa elije: {programa_opciones[0]} {programa_opciones[1]} {programa_opciones[2]}")

    humano_puntos = 0
    programa_puntos = 0

    for i in range(3):
        resultado = comparar(humano_opciones[i], programa_opciones[i])
        if resultado == "gano":
            humano_puntos = humano_puntos + 1
        elif resultado == "perdio":
            programa_puntos = programa_puntos + 1

    print(f"Punteo: {humano_puntos} - {programa_puntos}")

    if humano_puntos > programa_puntos:
        print("Ganador: Humano")
    elif programa_puntos > humano_puntos:
        print("Ganador: Programa")
    else:
        print("Resultado: Empate")


if __name__ == "__main__":
    main()


