class Consulta():
    def __init__(self, fecha='', motivo='', diagnostico='', mascota=''): # Se crea el constructor
        self.motivo = motivo.lower()
        self.fecha = fecha
        self.diagnostico = diagnostico.lower()
        self.mascota = mascota
        
    def __str__(self): #Se utiliza el metodo magico str 
        return f"Fecha: {self.fecha}, Motivo: {self.motivo}, Diagnóstico: {self.diagnostico}"
