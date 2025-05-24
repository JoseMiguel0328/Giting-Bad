class ErrorBase(Exception):
    pass

class DatoInvalidoError(ErrorBase):
    def __init__(self, mensaje="El dato no puede estar vacio."):
        super().__init__(mensaje)
    pass

class EdadInvalidaError(ErrorBase):
    def __init__(self, mensaje="Debe ingresar una edad permitida."):
        super().__init__(mensaje)
    pass

class TelefonoInvalidoError(ErrorBase):
    def __init__(self, mensaje="Debe ingresar un teléfono permitido."):
        super().__init__(mensaje)
    pass

class DocumentoInvalidoError(ErrorBase):
    def __init__(self, mensaje="Debe ingresar un documento valido."):
        super().__init__(mensaje)
    pass

class FechaInvalidaError(ErrorBase):
    def __init__(self, mensaje="Debe ingresar una fecha permitida."):
        super().__init__(mensaje)
    pass


