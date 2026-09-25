

class Config:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self, debug=True, archivo_datos="tareas.json"):
        
        if self._inicializado:
            return
        self.debug = debug
        self.archivo_datos = archivo_datos
        self._inicializado = True

    def __repr__(self):
        return f"Config(debug={self.debug}, archivo_datos='{self.archivo_datos}')"
