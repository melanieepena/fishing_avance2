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
            "id_usuario",
            "pais",
            "ciudad",
        ]

    def insertNewEmprendedor(
        self, name, email, phone, id_user, country, city,
    ):
        database = self.get_databaseXObj()
        sql = (
            "insert into fishingdb.emprendedor (id, nombre, email, telefono, id_usuario, pais, ciudad) "
            + f"values (0, '{name}', '{email}', '{phone}', {id_user},'{country}','{city}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getNewEmprendedor(
        self, name, email, phone, id_user, country, city,
    ):
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
                data_dic["id_usuario"],
                data_dic["pais"],
                data_dic["ciudad"],
            )
            return empObj
        else:
            return None
