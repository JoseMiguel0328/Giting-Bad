class Dueno():
    def __init__(self, nombre='', telefono=0, direccion='', documento=''):  # Se crea el constructor
        if not str(telefono).isdigit() or len(str(telefono)) < 7:
            raise ValueError("Número de teléfono inválido")
        if not documento:
            raise ValueError("El documento no puede estar vacío")

        self.nombre = nombre.lower()
        self.telefono = telefono
        self.direccion = direccion.lower()
        self.documento = documento

    