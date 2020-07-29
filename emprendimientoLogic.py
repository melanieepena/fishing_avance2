from logic import Logic


class emprendimientoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "nombre",
            "eslogan",
            "historia",
            "inversion_inicial",
            "venta_año_anterior",
            "oferta_porcentaje",
            "id_emprendedor",
            "fecha_fundacion",
            "descripcion",
            "estado",
        ]

    def insertNewEmprendimiento(
        self,
        name,
        slogan,
        history,
        inv_inic,
        sales_prevYear,
        offer,
        id_emp,
        fundationDate,
        desc,
        status,
    ):
        database = self.get_databaseXObj()
        sql = (
            "insert into fishingdb.emprendimiento (id, nombre, eslogan, historia, inversion_inicial, venta_año_anterior, oferta_porcentaje, id_emprendedor, fecha_fundacion,"
            + "descripcion, estado) "
            + f"values (0, '{name}', '{slogan}', '{history}', {inv_inic}, {sales_prevYear},{offer},{id_emp},'{fundationDate}','{desc}','{status}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows
