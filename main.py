from pokemon import Pokemon

pokemons = []


def capturar_pokemon():

    nombre = input("Nombre del Pokemon: ")
    tipo = input("Tipo del Pokemon: ")

    try:
        ataque = int(input("Puntos de ataque: "))
        defensa = int(input("Puntos de defensa: "))
        salud = int(input("Puntos de salud: "))

        if min(ataque, defensa, salud) < 0:
            print("Las estadisticas no pueden ser negativas.")
            return

        pokemon = Pokemon(nombre, tipo, ataque, defensa, salud)

        pokemons.append(pokemon)

    except ValueError:
        print("Error: introduce numeros enteros en las estadisticas.")


def seleccionar_pokemon():
    if not pokemons:
        print("No hay Pokemones capturados.")
        return None

    for i, pokemon in enumerate(pokemons):
        print(f"{i + 1}. {pokemon.nombre} (Nivel {pokemon.nivel})")

    try:
        opcion = int(input("Selecciona un Pokemon: "))

        if 1 <= opcion <= len(pokemons):
            return pokemons[opcion - 1]

        print("Opcion fuera de rango.")

    except ValueError:
        print("Debes introducir un numero.")

    return None


def entrenar_pokemon():
    pokemon = seleccionar_pokemon()

    if pokemon is None:
        return

    print("\nEstats disponibles:")
    print("1. Ataque")
    print("2. Defensa")
    print("3. Salud")
    print("4. Todas las estadisticas")

    opcion = input("que quieres mejorar? ")

    opciones = {
        "1": ("ataque",),
        "2": ("defensa",),
        "3": ("salud",),
        "4": ()
    }

    if opcion in opciones:
        pokemon.entrenar(*opciones[opcion])
    else:
        print("Opcion invalida.")


def mostrar_pokemons():
    if not pokemons:
        print("No hay Pokemones para mostrar.")
        return

    for pokemon in pokemons:
        pokemon.mostrar_info()


def contar_pokemons():
    print(f"Pokemones actualmente capturados: {len(pokemons)}")
    Pokemon.total_pokemons()


def liberar_pokemon():
    pokemon = seleccionar_pokemon()

    if pokemon is None:
        return

    nombre = pokemon.nombre
    pokemons.remove(pokemon)

    del pokemon

    print(f"{nombre} ha sido liberado de tu equipo")


def combatir():
    if len(pokemons) < 2:
        print("Necesitas dos Pokemones para combatir")
        return

    print("\nSelecciona tu Pokemon:")
    atacante = seleccionar_pokemon()

    if atacante is None:
        return

    print("\nSelecciona el Pokemon objetivo:")
    objetivo = seleccionar_pokemon()

    if objetivo is None:
        return

    if atacante is objetivo:
        print("Un Pokemon no puede atacarse a sí mismo.")
        return

    atacante.atacar(objetivo)


def main():
    while True:
        print("\n===== SIMULADOR POKÉMON =====")
        print("1. Capturar Pokemon ")
        print("2. Entrenar Pokemon ")
        print("3. Ver informacion ")
        print("4. Contar Pokemones ")
        print("5. Liberar Pokemon ")
        print("6. Combatir ")
        print("7. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            entrenar_pokemon()
        elif opcion == "3":
            mostrar_pokemons()
        elif opcion == "4":
            contar_pokemons()
        elif opcion == "5":
            liberar_pokemon()
        elif opcion == "6":
            combatir()
        elif opcion == "7":
            print("Gracias por jugar")
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
