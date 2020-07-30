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
        status,
        desc,
        history,
        slogan,
        inv_inic,
        fundationDate,
        sales_prevYear,
        offer,
        id_emp,
        name,
    ):
        database = self.get_databaseXObj()
        sql = (
            "insert into fishingdb.emprendimiento (id, estado, descripcion, historia, eslogan, inversion_inicial, fecha_fundacion, venta_año_anterior, "
            + f"oferta_porcentaje, id_emprendedor, nombre) "
            + f"values (0, '{status}', '{desc}', '{history}', {slogan}, {inv_inic},{fundationDate},{sales_prevYear},'{offer}','{id_emp}','{name}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getEmprendimientoByName(self, name):
        dataBase = self.get_databaseXObj()
        sql = (
            "SELECT * FROM fishingdb.emprendimiento "
            + f"where emprendimiento.nombre = '{name}';"
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
