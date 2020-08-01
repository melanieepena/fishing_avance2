class emprendedorObj:
    def __init__(self, id, nombre, email, telefono, usuario, pais, ciudad, biografia):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.pais = pais
        self.ciudad = ciudad
        self.usuario = usuario
        self.biografia = biografia

    def getId(self):
        return self.id
