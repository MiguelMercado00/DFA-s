class AutomataFinitoDeterminista:
    def __init__(self):
        self.estado_actual = 'q0'
        self.estados_finales = {'q0'}

    def transitar(self, simbolo):
        transiciones = {
            'q0': {'1': 'q1', '0': 'q0'},
            'q1': {'1': 'q0', '0': 'q2'},
            'q2': {'1': 'q2', '0': 'q1'}
        }
        if simbolo not in transiciones[self.estado_actual]:
            return False
        self.estado_actual = transiciones[self.estado_actual][simbolo]
        return True

    def acepta_cadena(self, cadena):
        self.estado_actual = 'q0'
        for simbolo in cadena:
            if not self.transitar(simbolo):
                return False
        return self.estado_actual in self.estados_finales


# Función para solicitar entrada y verificar el resultado del autómata
def procesar_cadena():
    cadena = input("Ingrese una cadena de 0s y 1s: ")

    # Si no se ingresó ninguna cadena, se acepta la cadena vacía
    if not cadena:
        print("El autómata acepta la cadena.")
        return
    afd = AutomataFinitoDeterminista()
    if afd.acepta_cadena(cadena):
        print("El autómata acepta la cadena.")
    else:
        print("El autómata rechaza la cadena.")


# Ejecutar la función para procesar la cadena ingresada
procesar_cadena()
