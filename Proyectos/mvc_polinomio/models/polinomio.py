class NodoPolinomio:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class Polinomio:
    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente, exponente):
        nuevo_nodo = NodoPolinomio(coeficiente, exponente)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            anterior = None
            while actual is not None and actual.exponente > exponente:
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza = nuevo_nodo
            else:
                anterior.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = actual

    def generar_html(self):
        """Genera el texto del polinomio usando HTML para los exponentes"""
        if self.cabeza is None:
            return "0"

        resultado = ""
        actual = self.cabeza
        while actual is not None:
            if actual.coeficiente != 0:  # Ignorar términos con coeficiente 0
                
                # Manejo de los signos (+ y -) con espacios para que se vea mejor
                if actual.coeficiente > 0 and len(resultado) > 0:
                    resultado += " + "
                elif actual.coeficiente < 0 and len(resultado) > 0:
                    resultado += " " # Añadimos un espacio antes de que se pegue el signo negativo
                
                # Lógica original para los coeficientes 1 y -1
                if actual.coeficiente == -1 and actual.exponente != 0:
                    resultado += "-"
                elif actual.coeficiente != 1 or actual.exponente == 0:
                    # En lugar de floats forzados, respetamos enteros si los hay
                    resultado += str(actual.coeficiente)
                
                # Manejo de las variables y el exponente con HTML
                if actual.exponente > 0:
                    resultado += "x"
                    if actual.exponente > 1:
                        resultado += f"<sup>{actual.exponente}</sup>"
                        
            actual = actual.siguiente
            
        return resultado if resultado else "0"