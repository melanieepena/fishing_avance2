from logic import Logic
from emprendimientoObj import emprendimientoObj


class emprendimientoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "estado",
            "descripcion",
            "historia",
            "eslogan",
            "inversion_inicial",
            "fecha_fundacion",
            "venta_año_anterior",
            "oferta_porcentaje",
            "id_emprendedor",
            "nombre",
        ]

    def insertNewEmprendimiento(
        self,
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
        database = self.get_databaseXObj()
        sql = (
            "insert into fishingdb.emprendimiento (id, estado, descripcion, historia, eslogan, inversion_inicial, fecha_fundacion, venta_año_anterior, "
            + f"oferta_porcentaje, id_emprendedor, nombre) "
            + f"values (0, '{estado}', '{descripcion}', '{historia}', '{eslogan}', '{inversion_inicial}','{fecha_fundacion}','{venta_año_anterior}','{oferta_porcentaje}','{id_emprendedor}','{nombre}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getEmprendimientoByName(self, nombre):
        dataBase = self.get_databaseXObj()
        sql = (
            "SELECT * FROM fishingdb.emprendimiento "
            + f"where emprendimiento.nombre = '{nombre}';"
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            emprendimientObj = emprendimientoObj(
                data_dic["id"],
                data_dic["estado"],
                data_dic["descripcion"],
                data_dic["historia"],
                data_dic["eslogan"],
                data_dic["inversion_inicial"],
                data_dic["fecha_fundacion"],
                data_dic["venta_año_anterior"],
                data_dic["oferta_porcentaje"],
                data_dic["id_emprendedor"],
                data_dic["nombre"],
            )
            return emprendimientObj
        else:
            return None

    def checkEmprendimiento(self, name):
        dataBase = self.get_databaseXObj()
        sql = (
            "SELECT emprendimiento.nombre FROM fishingdb.emprendimiento "
            + f"where emprendimiento.nombre = '{name}';"
        )
        print(sql)
        data = dataBase.executeQuery(sql)
        counter = 0
        for item in data:
            counter += 1

        if counter > 0:
            return True
        else:
            return False

    def deleteEmprendimiento(self, id):
        database = self.get_databaseXObj()
        sql = f"delete from fishingdb.emprendimiento where emprendimiento.id = '{id}';"
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllEmprendimientoLen(self):
        dataBase = self.get_databaseXObj()
        sql = "SELECT * FROM fishingdb.emprendimiento;"
        data = dataBase.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        return data

    def updateEmprendimiento(
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
        database = self.get_databaseXObj()
        sql = f"update fishingdb.emprendimiento set emprendimiento.estado= '{estado}',emprendimiento.descripcion= '{descripcion}',emprendimiento.historia= '{historia}', emprendimiento.eslogan= '{eslogan}',emprendimiento.inversion_inicial= '{inversion_inicial}',emprendimiento.fecha_fundacion= '{fecha_fundacion}',emprendimiento.venta_año_anterior= '{venta_año_anterior}',emprendimiento.oferta_porcentaje= '{oferta_porcentaje}',emprendimiento.id_emprendedor= '{id_emprendedor}',emprendimiento.nombre= '{nombre}'  where emprendimiento.id = '{id}';"
        rows = database.executeNonQueryRows(sql)
        return rows
