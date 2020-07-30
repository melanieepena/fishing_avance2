from logic import Logic
from userLogic import UserLogic
from emprendedorLogic import emprendedorLogic
from emprendedorObj import emprendedorObj
from emprendimientoLogic import emprendimientoLogic
from emprendimientoObj import emprendimientoObj


class fundadorLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = ["id", "usuario", "password", "rol"]

    def insertNewFundador(self, user, name):

        usuarioEmprendedor = UserLogic()
        id_emprendedor = usuarioEmprendedor.getUserByUser(user)

        infoEmprendimiento = emprendimientoLogic()
        id_emprendimiento = infoEmprendimiento.getEmprendimientoByName(name)

        database = self.get_databaseXObj()
        sql = (
            "insert into fishingdb.fundador (id, id_emprendedor, id_emprendimiento) "
            + f"values (0, {id_emprendedor.getId()}, {id_emprendimiento.getId()});"
        )
        print(sql)
        rows = database.executeNonQueryRows(sql)
        return rows
