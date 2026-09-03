from flask import render_template, request
from models.polinomio import Polinomio

def index():
    resultado = None
    
    if request.method == 'POST':
        datos_entrada = request.form.get('coeficientes')
        
        # 1. Instanciamos la clase 
        mi_polinomio = Polinomio()
        
        try:
            # 2. Convertimos el texto (ej: "3, -2, 5") en una lista de números
            lista_coeficientes = [float(x.strip()) for x in datos_entrada.split(',')]
            
            # El exponente máximo es la cantidad de elementos menos 1
            grado_maximo = len(lista_coeficientes) - 1
            
            # 3. Recorremos la lista y agregamos nodo por nodo
            for i, coeficiente in enumerate(lista_coeficientes):
                exponente_actual = grado_maximo - i
                
                # Limpiamos decimales innecesarios (ej: 2.0 pasa a ser 2)
                if coeficiente.is_integer():
                    coeficiente = int(coeficiente)
                    
                mi_polinomio.agregar_termino(coeficiente, exponente_actual)
                
            # 4. Llamamos al método adaptado para la web
            resultado = mi_polinomio.generar_html()
            
        except ValueError:
            resultado = "Por favor, ingresa solo números separados por comas."
            
    return render_template('index.html', resultado=resultado)