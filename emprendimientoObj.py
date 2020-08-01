class emprendimientoObj:
    def __init__(
        self,
        id,
        estado,
        descripcion,
        historia,
        eslogan,
        inversion_inicial,
        fecha_fundacion,
        venta_año_anterior,
        oferta_porcentaje,
        id_emprendedor,
        nombre,
    ):
        self.id = id
        self.estado = estado
        self.descripcion = descripcion
        self.historia = historia
        self.eslogan = eslogan
        self.inversion_inicial = inversion_inicial
        self.fecha_fundacion = fecha_fundacion
        self.venta_año_anterior = venta_año_anterior
        self.oferta_porcentaje = oferta_porcentaje
        self.id_emprendedor = id_emprendedor
        self.nombre = nombre

    def getId(self):
        return self.id
