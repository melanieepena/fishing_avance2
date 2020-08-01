from logic import Logic
from emprendedorObj import emprendedorObj


class emprendedorLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "nombre",
            "email",
            "telefono",
            "foto",
            "id_usuario",
            "pais",
            "ciudad",
            "biografia",
        ]

    def insertNewEmprendedor(
        self, name, email, phone, id_user, country, city, biografia
    ):
        database = self.get_databaseXObj()
        sql = (
            "insert into fishingdb.emprendedor (id, nombre, email, telefono, id_usuario, pais, ciudad, biografia) "
            + f"values (0, '{name}', '{email}', '{phone}', {id_user},'{country}','{city}', '{biografia}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getNewEmprendedor(self, name, email, phone, id_user, country, city, biografia):
        dataBase = self.get_databaseXObj()
        sql = "select * from fishingdb.emprendedor " + f"where id_usuario = {id_user};"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            empObj = emprendedorObj(
                data_dic["id"],
                data_dic["nombre"],
                data_dic["email"],
                data_dic["telefono"],
                data_dic["foto"],
                data_dic["id_usuario"],
                data_dic["pais"],
                data_dic["ciudad"],
                data_dic["biografia"],
            )
            return empObj
        else:
            return None

    def getEmprendedorByUser(self, id_user):
        dataBase = self.get_databaseXObj()
        sql = "select * from fishingdb.emprendedor " + f"where id_usuario = {id_user};"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            empObj = emprendedorObj(
                data_dic["id"],
                data_dic["nombre"],
                data_dic["email"],
                data_dic["telefono"],
                data_dic["foto"],
                data_dic["id_usuario"],
                data_dic["pais"],
                data_dic["ciudad"],
                data_dic["biografia"],
            )
            return empObj
        else:
            return None

    def getAllEmprendedores(self):
        dataBase = self.get_databaseXObj()
        sql = "select * from fishingdb.emprendedor;"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        return data

    def deleteEmprendedor(self, id):
        database = self.get_databaseXObj()
        sql = f"delete from fishingdb.emprendedor where emprendedor.id = '{id}';"
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateEmprendedor(
        self, id, name, email, phone, id_user, country, city, biografia
    ):
        database = self.get_databaseXObj()
        sql = (
            "update fishingdb.emprendedor "
            + f"set emprendedor.nombre = '{name}', emprendedor.email = '{email}', emprendedor.telefono = '{phone}', emprendedor.id_usuario = '{id_user}', "
            + f"emprendedor.pais = '{country}', emprendedor.ciudad = '{city}', emprendedor.biografia = '{biografia}' "
            + f"where emprendedor.id = '{id}';"
        )
        rows = database.executeNonQueryRows(sql)
        return rows
