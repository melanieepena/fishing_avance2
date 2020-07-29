class inversorObj:
    def __init__(self, id, nombre, biografia, email, usuario, pais, ciudad):
        self.id = id

        self.nombre = nombre
        self.biografia = biografia
        self.email = email
        self.pais = pais
        self.ciudad = ciudad
        self.usuario = usuario

    def getId(self):
        return self.id
