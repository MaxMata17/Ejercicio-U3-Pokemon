class Pokemon:
    total_creados = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud, nivel=1):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

        Pokemon.total_creados += 1
        print(f"¡{self.nombre} ha sido creado")

    def __del__(self):
        print(f"{self.nombre} ha sido liberado")

    def entrenar(self, *args):
        if not args:
            args = ("ataque", "defensa", "salud")

        mejoras = {
            "ataque": ("ataque", 5),
            "defensa": ("defensa", 3),
            "salud": ("salud", 10)
        }

        for estadistica in args:
            estadistica = estadistica.lower()

            if estadistica in mejoras:
                atributo, aumento = mejoras[estadistica]
                setattr(self, atributo, getattr(self, atributo) + aumento)
            else:
                print(f"Estadistica no valida: {estadistica}")
                continue

            print(f"{atributo.capitalize()} +{aumento}")

        self.nivel += 1
        print(f"¡{self.nombre} subio al nivel {self.nivel} ")

    def mostrar_info(self):
        print(f"\n++++++++{self.nombre} ++++++++++")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}")

    def atacar(self, objetivo):
        if self.salud <= 0:
            print(f"{self.nombre} no puede atacar porque esta debilitado.")
            return

        if objetivo.salud <= 0:
            print(f"{objetivo.nombre} ya esta debilitado.")
            return

        daño = max(1, self.ataque - objetivo.defensa)
        objetivo.salud = max(0, objetivo.salud - daño)

        print(
            f"{self.nombre} ataca a {objetivo.nombre} "
            f"y causa {daño} puntos de daño."
        )
        print(f"Salud restante de {objetivo.nombre}: {objetivo.salud}")

    @classmethod
    def total_pokemons(cls):
        print(f"Pokemones creados en total: {cls.total_creados}")
