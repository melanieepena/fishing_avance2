from logic import Logic
from productosObj import productosObj


class productosLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "nombre",
            "foto",
            "descripcion",
            "costo_unitario",
            "precio_venta",
            "patente",
            "id_emprendimiento",
        ]

    def insertNewProducto(self, name, picture, desc, costo, precio, patente, id_emp):
        database = self.get_databaseXObj()
        sql = (
            "insert into fishingdb.productos (id, nombre, foto, descripcion, costo_unitario, precio_venta, patente, id_emprendimiento) "
            + f"values (0, '{name}', '{picture}', '{desc}', {costo},{precio},{patente},{id_emp});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteProducto(self, id_prod):
        database = self.get_databaseXObj()
        sql = "delete from fishingdb.productos " + f"where id = {id_prod};"
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateProducto(self, id_prod, name, picture, desc, costo, precio, patente):
        database = self.get_databaseXObj()
        sql = (
            "update fishingdb.productos"
            + f" set nombre ='{name}',foto='{picture}', descripcion='{desc}', costo_unitario={costo}, precio_venta={precio}, patente={patente}"
            + f" where id = {id_prod};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getNewProducto(self, id_prod):
        dataBase = self.get_databaseXObj()
        sql = "select * from fishingdb.productos " + f"where id = {id_prod};"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            prodObj = productosObj(
                data_dic["id"],
                data_dic["nombre"],
                data_dic["foto"],
                data_dic["descripcion"],
                data_dic["costo_unitario"],
                data_dic["precio_venta"],
                data_dic["patente"],
                data_dic["id_emprendimiento"],
            )
            return prodObj
        else:
            return None

    def getAllProductoLen(self):
        dataBase = self.get_databaseXObj()
        sql = "select * from fishingdb.productos "
        data = dataBase.executeQuery(sql)
        return data


print(productosLogic().getAllProductoLen())
