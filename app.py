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
    if request.method == "GET":
        return render_template("fundadores.html", message="")
    elif request.method == "POST":
        user = request.form["user"]
        emprendimiento = request.form["name"]
        rol = 3
        logicUsuario = UserLogic()
        # Comprobando si existe
        existeUsuario = logicUsuario.checkUserInUsuario(user, rol)
        if existeUsuario:
            logic = fundadorLogic()
            rows = logic.insertNewFundador(user, emprendimiento)
            return render_template("fundadores.html", message="Se agrego con exito")
        else:
            return render_template(
                "fundadores.html", message="El usuario seleccionado no existe"
            )
        return render_template("index.html", message="")


@app.route("/Emprendimiento", methods=["GET", "POST"])
def signUPEmprendimiento():
    if request.method == "GET":
        return render_template("emprendimiento.html", message="")

    elif request.method == "POST":  # "POST"
        # Recuperando datos
        name = request.form["nombre"]
        rol = 3
        estado = str(request.form["estado"])
        descripcion = str(request.form["descripcion"])
        historia = request.form["historia"]
        eslogan = request.form["eslogan"]
        inversion_inicial = request.form["inversion_inicial"]
        fecha_fundacion = request.form["fecha_fundacion"]
        venta_año_anterior = request.form["venta_año_anterior"]
        oferta_porcentaje = request.form["oferta_porcentaje"]
        id_emprendedor = request.form["id_emprendedor"]
        nombre = request.form["nombre"]
        ####
        # Creando nuevo usuario
        emprendimientoLog = emprendimientoLogic()

        emprendimientoLog.insertNewEmprendimiento(
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
        )
        # id_user = int(logicUsuario.getNewUser(user, password, rol).getId())
        # Creando nuevo emprendedor

        return render_template("index.html", message="")


@app.route("/categoria")
def categoria():
    return render_template("emprendimiento.html")


if __name__ == "__main__":
    app.run(debug=True)
