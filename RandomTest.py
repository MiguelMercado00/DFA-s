import random

class AutomataFinitoDeterminista:
    def __init__(self):
        self.estado_actual = 'q0'
        self.estados_finales = {'q0'}  # Estados finales incluyen q0 y q3

    def transitar(self, simbolo):
        transiciones = {
            'q0': {'1': 'q1', '0': 'q0'},
            'q1': {'1': 'q2', '0': 'q1'},
            'q2': {'1': 'q0', '0': 'q2'},
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


# Generar cadena aleatoria con número de 1 múltiplo de 3
def generar_cadena_multiplo_de_3(n):
    cantidad_unos = n // 3 * 3  # Asegura que la cantidad de unos sea un múltiplo de 3
    cadena = ['1'] * cantidad_unos + ['0'] * (n - cantidad_unos)
    random.shuffle(cadena)
    return ''.join(cadena)

# Generar cadena aleatoria con número de 1 no múltiplo de 3
def generar_cadena_no_multiplo_de_3(n):
    cantidad_unos = n // 3 * 3 + 1  # Asegura que la cantidad de unos no sea un múltiplo de 3
    cadena = ['1'] * cantidad_unos + ['0'] * (n - cantidad_unos)
    random.shuffle(cadena)
    return ''.join(cadena)

# Procesar la cadena con el DFA y mostrar el resultado
def procesar_cadena_y_mostrar_resultado(cadena):
    afd = AutomataFinitoDeterminista()
    if afd.acepta_cadena(cadena):
        print("El DFA acepta la cadena.")
    else:
        print("El DFA rechaza la cadena.")

# Generar y procesar la cadena aleatoria con número de 1 múltiplo de 3
cadena_a = generar_cadena_multiplo_de_3(1000000)
print("\nCadena A:")
procesar_cadena_y_mostrar_resultado(cadena_a)

# Generar y procesar la cadena aleatoria con número de 1 no múltiplo de 3
cadena_b = generar_cadena_no_multiplo_de_3(1000000)
print("\nCadena B:")
procesar_cadena_y_mostrar_resultado(cadena_b)
