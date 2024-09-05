class MotorDeInferencia:
    def __init__(self):
        # Inicializamos las reglas y los hechos
        self.reglas = []
        self.hechos = []

    def agregar_regla(self, condicion, conclusion):
        # Agregamos reglas al motor
        self.reglas.append((condicion, conclusion))

    def agregar_hecho(self, hecho):
        # Agregamos hechos iniciales
        if hecho not in self.hechos:
            self.hechos.append(hecho)

    def ejecutar(self):
        # Ejecutamos el motor de inferencia (encadenamiento hacia adelante)
        while True:
            nueva_inferencia = False
            for condicion, conclusion in self.reglas:
                if all(hecho in self.hechos for hecho in condicion) and conclusion not in self.hechos:
                    print(f"Se infiere: {conclusion}")
                    self.agregar_hecho(conclusion)
                    nueva_inferencia = True
            if not nueva_inferencia:
                break

# Ejemplo de uso

# Creamos un motor de inferencia
motor = MotorDeInferencia()

# Agregamos reglas (si-entonces)
# Regla 1: Si el perfil de riesgo es bajo, entonces recomendar ETFs de bajo riesgo
motor.agregar_regla(['perfil_bajo_riesgo'], 'recomendar_etf_bajo_riesgo')

# Regla 2: Si el perfil de riesgo es alto, entonces recomendar ETFs de alto riesgo
motor.agregar_regla(['perfil_alto_riesgo'], 'recomendar_etf_alto_riesgo')

# Agregamos hechos iniciales
motor.agregar_hecho('perfil_bajo_riesgo')  # El usuario tiene un perfil de riesgo bajo

# Ejecutamos el motor de inferencia
motor.ejecutar()

# Salida esperada:
# Se infiere: recomendar_etf_bajo_riesgo
