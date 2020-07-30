from flask import Flask, render_template, request, redirect, session
from userLogic import UserLogic
from userObj import UserObj
from inversorLogic import inversorLogic
from inversorObj import inversorObj
from emprendedorLogic import emprendedorLogic
from fundadorLogic import fundadorLogic
from emprendimientoLogic import emprendimientoLogic

app = Flask(__name__)
app.secret_key = "ILoveFishing"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/inversionista")
def inversionista():
    return render_template("inversionista.html")


@app.route("/emprendedor")
def emprendedor():
    return render_template("emprendedor.html")


@app.route("/productos")
def productos():
    return render_template("productos.html")


@app.route("/fundadores", methods=["GET", "POST"])
def fundadores():
    logic = fundadorLogic()
    verdadero = False
    if request.method == "GET":
        data = logic.getAllFundadores()
        message = ""
        return render_template("fundadores.html", data=data, message=message)
    elif request.method == "POST":
        formId = int(request.form["formId"])
        # INSERTAR
        if formId == 1:
            user = request.form["user"]
            emprendimiento = request.form["name"]
            rol = 3
            logicUsuario = UserLogic()
            logicEmpre = emprendimientoLogic()
            # Comprobando si existe
            existeUsuario = logicUsuario.checkUserInUsuario(user, rol)
            existeEmprendimiento = logicEmpre.checkEmprendimiento(emprendimiento)

            if existeUsuario and existeEmprendimiento:
                logicInsert = fundadorLogic()
                rows = logicInsert.insertNewFundador(user, emprendimiento)
                data = logic.getAllFundadores()
                message = "Se ha agregado al fundador"
                return render_template("fundadores.html", data=data, message=message)
            else:
                data = logic.getAllFundadores()
                message = "El usuario o emprendimiento seleccionado no existe. Pruebe de nuevo"
                return render_template("fundadores.html", data=data, message=message)
        # ELIMINAR
        elif formId == 2:
            id = int(request.form["id"])
            logic.deleteFundador(id)
            message = "Se ha eliminado un fundador"
            data = logic.getAllFundadores()
            return render_template("fundadores.html", data=data, message=message)
        # Va al form para dar update
        elif formId == 3:
            verdadero = True
            id = int(request.form["id"])
            data = logic.getAllFundadores()
            return render_template(
                "fundadores.html", data=data, verdadero=verdadero, id=id,
            )
        # UPDATE
        else:
            id = int(request.form["id"])
            user = request.form["user"]
            emprendimiento = request.form["name"]
            rol = 3
            logicUsuario = UserLogic()
            logicEmpre = emprendimientoLogic()
            # Comprobando si existe
            existeUsuario = logicUsuario.checkUserInUsuario(user, rol)
            existeEmprendimiento = logicEmpre.checkEmprendimiento(emprendimiento)

            if existeUsuario and existeEmprendimiento:
                logic.updateFundador(id, user, emprendimiento)
                data = logic.getAllFundadores()
                massage = "Se ha modificado al fundador"
                return render_template("fundadores.html", data=data, massage=massage)
            else:
                data = logic.getAllFundadores()
                massage = "El usuario o emprendimiento seleccionado no existe. Preuebe de nuevo"
                return render_template("fundadores.html", data=data, message=massage)


@app.route("/emprendimiento")
def emprendimiento():
    return render_template("emprendimiento.html")


@app.route("/categoria")
def categoria():
    return render_template("categoria.html")


if __name__ == "__main__":
    app.run(debug=True)
