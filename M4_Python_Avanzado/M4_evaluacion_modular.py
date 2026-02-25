
class RangoInvalido(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
    def __str__(self):
        return self.mensaje

# Definir la clase principal Jugador
class Jugador:
    def __init__(self, nombre, edad, posicion, goles):
        self.nombre = nombre
        self.edad = int(edad)
        self.posicion = posicion
        self.goles = int(goles)
    
        if not (0 <= self.edad <= 120):
            raise RangoInvalido("Error: La edad debe estar entre 0 y 120 años.")
        if self.goles < 0:
            raise RangoInvalido("Error: El número de goles no puede ser negativo.")
            # o si? también podríamos considerar los autogoles, pero pasamos de eso por ahora.

    def mostrar_info(self,titulo=True):
        plantilla = f"{self.nombre:25}\t{self.edad:4}\t{self.posicion:15}\t{self.goles:4}"
        if titulo:
            plantilla_titulo = f"{'Nombre':25}\t{'Edad':4}\t{'Posición':15}\t{'Goles':4}"
            print(plantilla_titulo)
        print(plantilla)
    
# Subclase Capitan
class Capitan(Jugador):
    def __init__(self, jugador, liderazgo):
        super().__init__(jugador.nombre, jugador.edad, jugador.posicion, jugador.goles)
        self.liderazgo = float(liderazgo)

    def mostrar_info(self,titulo=True):
        plantilla = plantilla = f"{self.nombre + '   (C)':25}\t{self.edad:4}\t{self.posicion:15}\t{self.goles:4}\t{self.liderazgo:4.1f}"
        if titulo:
            plantilla_titulo = plantilla_titulo = f"{'Nombre':25}\t{'Edad':4}\t{'Posición':15}\t{'Goles':4}\t{'Liderazgo':<10}\n{'-'*80}"
            print(plantilla_titulo)
        print(plantilla)

# Crear clase Jugadores

class Jugadores:
    def __init__(self):
        self.jugadores = []

    def _cargar_linea(self, linea):
        datos = linea.strip().split(',')
        if len(datos) == 4:
            return Jugador(*datos)
        elif len(datos) == 5:
            jugador = Jugador(*datos[:4])
            return Capitan(jugador, datos[4])
        else:
            raise ValueError(f"Línea mal formateada: {linea}")

    def _formatear_jugador(self, jugador):
        if isinstance(jugador, Capitan):
            return f"{jugador.nombre},{jugador.edad},{jugador.posicion},{jugador.goles},{jugador.liderazgo}"
        else:
            return f"{jugador.nombre},{jugador.edad},{jugador.posicion},{jugador.goles}"

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                for linea in f:
                    jugador = self._cargar_linea(linea)
                    self.agregar_jugador(jugador)
        except FileNotFoundError:
            print(f"Error: El archivo {archivo} no se encontró.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}") 
    
    def guardar_en_archivo(self, archivo):
        try:
            with open(archivo, 'w') as f:
                for jugador in self.jugadores:
                    f.write(self._formatear_jugador(jugador) + '\n')
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
    
    def mostrar_jugadores(self):
        for i,jugador in enumerate(self.jugadores):
            if i == 0 and isinstance(jugador, Capitan):
                jugador.mostrar_info(titulo=True)
            else:
                jugador.mostrar_info(titulo=False)


###############################################
# Teniendo al gran equipo de la Copa America 2015
seleccion_chilena_2015 = {
    1: ("Claudio Bravo", 32, "Arquero", 0),
    2: ("Eugenio Mena", 26, "Defensa", 3),
    3: ("Miiko Albornoz", 24, "Defensa", 2),
    4: ("Mauricio Isla", 27, "Defensa", 3),
    5: ("Francisco Silva", 29, "Mediocampo", 0),
    6: ("Jose Pedro Fuenzalida", 30, "Mediocampo", 2),
    7: ("Alexis Sanchez", 26, "Delantero", 25),
    8: ("Arturo Vidal", 28, "Mediocampo", 10),
    9: ("Mauricio Pinilla", 31, "Delantero", 8),
    10: ("Jorge Valdivia", 31, "Mediocampo", 7),
    11: ("Eduardo Vargas", 25, "Delantero", 15),
    12: ("Paulo Garces", 30, "Arquero", 0),
    13: ("Jose Rojas", 32, "Defensa", 1),
    14: ("Matias Fernandez", 29, "Mediocampo", 14),
    15: ("Jean Beausejour", 31, "Mediocampo", 6),
    16: ("David Pizarro", 35, "Mediocampo", 4),
    17: ("Gary Medel", 27, "Defensa", 5),
    18: ("Gonzalo Jara", 29, "Defensa", 3),
    19: ("Felipe Gutierrez", 24, "Mediocampo", 3),
    20: ("Charles Aranguiz", 26, "Mediocampo", 5),
    21: ("Marcelo Diaz", 28, "Mediocampo", 1),
    22: ("Angelo Henriquez", 21, "Delantero", 2),
    23: ("Johnny Herrera", 34, "Arquero", 0)
}

# Funciones para luego correr casos modularmente

# Se crea el archivo de Chile vs Argentina en la copa America 2015
def crear_archivo_chile_argentina():
    texto = """Claudio Bravo,32,Arquero,0,9.5
Francisco Silva,29,Mediocampo,0
Marcelo Diaz,28,Mediocampo,1
Gary Medel,27,Defensa,5
Mauricio Isla,27,Defensa,3
Charles Aranguiz,26,Mediocampo,5
Arturo Vidal,28,Mediocampo,10
Jean Beausejour,31,Mediocampo,6
Jorge Valdivia,31,Mediocampo,7
Alexis Sanchez,26,Delantero,25
Eduardo Vargas,25,Delantero,15"""
    with open("chile_argentina_2015.txt", 'w') as f:
        f.write(texto)

def main_cargar_chile_argentina():
    equipo = Jugadores()
    equipo.cargar_desde_archivo("chile_argentina_2015.txt")
    equipo.mostrar_jugadores()

def main_archivo_no_encontrado():
    equipo = Jugadores()
    equipo.cargar_desde_archivo("chile_colombia_2015.txt")

def main_edad_invalida():
    """Edad invalida"""
    jugador = Jugador("Jugador Ejemplo", -5, "Delantero", 10)

# Se crea archivo de Chile vs Uruguay en la Copa America 2015
def main_guardar_chile_uruguay():
    equipo = Jugadores()
    lista_titulares = [1,17,18,4,2,20,21,8,10,11,7]
    for numero in lista_titulares:
        datos = seleccion_chilena_2015[numero]
        jugador = Jugador(*datos)
        if numero == 1:  # Claudio Bravo es el capitán
            jugador_capitan = Capitan(jugador, liderazgo=9.5)
            equipo.agregar_jugador(jugador_capitan)
        else:
            equipo.agregar_jugador(jugador)
    equipo.guardar_en_archivo("chile_uruguay_2015.txt")
    equipo.mostrar_jugadores()
    return None

# Se crea el archivo de Chile vs Argentina
crear_archivo_chile_argentina()

if __name__ == "__main__":
    # Descomentar la función que se quiera probar
    
    #main_archivo_no_encontrado() 
    #main_edad_invalida()
    #main_cargar_chile_argentina()
    #main_guardar_chile_uruguay()
    pass
