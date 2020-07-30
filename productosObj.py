class productosObj:
    def __init__(self, id, name, picture, desc, costo, precio, patente, id_emp):
        self.id = id

        self.name = name
        self.picture = picture
        self.desc = desc
        self.costo = costo
        self.precio = precio
        self.patente = patente
        self.id_emp = id_emp

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getPicture(self):
        return self.picture

    def getDesc(self):
        return self.desc

    def getCosto(self):
        return self.costo

    def getPrecio(self):
        return self.precio

    def getPatente(self):
        return self.patente

    def getIdEmp(self):
        return self.id_emp
