class Mascota():
    def __init__(self, nombre='', especie='', raza='', edad=0, dueno=''): # Se crea el constructor
        self.nombre = nombre.lower()
        self.especie = especie.lower()
        self.raza = raza.lower()
        self.edad = edad
        self.dueno = dueno
    
    def __str__(self):
         # Se utiliza el metodo magico str 
        return f"{self.nombre} ({self.especie}, {self.raza}, {self.edad} años) \n  Dueño: {self.dueno.nombre} Tel: {self.dueno.telefono}, Dir: {self.dueno.direccion}, CC:{self.dueno.documento}"
