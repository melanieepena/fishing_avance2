from flask import Flask, render_template, request, redirect, session
import mysql.connector
from mysql.connector import Error
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
    logic = emprendimientoLogic()
    massage = ""
    verdadero = False
    if request.method == "GET":
        data = logic.getAllEmprendimientoLen()
        return render_template("emprendimiento.html", data=data, massage=massage)

    elif request.method == "POST":  # "POST"
        formId = int(request.form["formId"])
        # Inserta una emprendimiento
        if formId == 1:
            estado = str(request.form["estado"])
            descripcion = request.form["descripcion"]
            historia = str(request.form["historia"])
            eslogan = request.form["eslogan"]
            inversion_inicial = request.form["inversion_inicial"]
            fecha_fundacion = request.form["fecha_fundacion"]
            venta_año_anterior = request.form["venta_año_anterior"]
            oferta_porcentaje = request.form["oferta_porcentaje"]
            id_emprendedor = request.form["id_emprendedor"]
            nombre = request.form["nombre"]

            try:
                logic.insertNewEmprendimiento(
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
                massage = "Se ha insertado un nuevo emprendimiento"
                data = logic.getAllEmprendimientoLen()

            except mysql.connector.Error as error:
                print("Failed inserting BLOB data into MySQL table {}".format(error))
                massage = "No se puede insertar. No existe el id emprendedor"
                data = logic.getAllEmprendimientoLen()

            return render_template("emprendimiento.html", data=data, massage=massage)

            # Elimina una categoria
        elif formId == 2:
            id = int(request.form["id"])

            try:
                logic.deleteEmprendimiento(id)
                massage = "Se ha eliminado un usuario"
                data = logic.getAllEmprendimientoLen()

            except mysql.connector.Error as error:
                print("Failed inserting BLOB data into MySQL table {}".format(error))
                massage = "No se puede eliminar. Afecta la integridad de los datos"
                data = logic.getAllEmprendimientoLen()

            return render_template("emprendimiento.html", data=data, massage=massage)
        # Va al form para dar update
        elif formId == 3:
            id = int(request.form["id"])
            estado = str(request.form["estado"])
            descripcion = request.form["descripcion"]
            historia = str(request.form["historia"])
            eslogan = request.form["eslogan"]
            inversion_inicial = request.form["inversion_inicial"]
            fecha_fundacion = request.form["fecha_fundacion"]
            venta_año_anterior = request.form["venta_año_anterior"]
            oferta_porcentaje = request.form["oferta_porcentaje"]
            id_emprendedor = request.form["id_emprendedor"]
            nombre = request.form["nombre"]
            verdadero = True
            data = logic.getAllEmprendimientoLen()
            return render_template(
                "emprendimiento.html",
                data=data,
                verdadero=verdadero,
                id=id,
                estado=estado,
                descripcion=descripcion,
                historia=historia,
                eslogan=eslogan,
                inversion_inicial=inversion_inicial,
                fecha_fundacion=fecha_fundacion,
                venta_año_anterior=venta_año_anterior,
                oferta_porcentaje=oferta_porcentaje,
                id_emprendedor=id_emprendedor,
                nombre=nombre,
            )

        # Modifica una categoria
        else:
            id = int(request.form["id"])
            estado = str(request.form["estado"])
            descripcion = request.form["descripcion"]
            historia = str(request.form["historia"])
            eslogan = request.form["eslogan"]
            inversion_inicial = request.form["inversion_inicial"]
            fecha_fundacion = request.form["fecha_fundacion"]
            venta_año_anterior = request.form["venta_año_anterior"]
            oferta_porcentaje = request.form["oferta_porcentaje"]
            id_emprendedor = request.form["id_emprendedor"]
            nombre = request.form["nombre"]

            try:
                logic.updateEmprendimiento(
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
                )
                data = logic.getAllEmprendimientoLen()
                massage = "Se ha modificado el emprendimiento"

            except mysql.connector.Error as error:
                print("Failed inserting BLOB data into MySQL table {}".format(error))
                massage = "No se puede modificar. No existe el id emprendedor"
                data = logic.getAllEmprendimientoLen()

            return render_template("emprendimiento.html", data=data, massage=massage)


@app.route("/categoria")
def categoria():
    return render_template("emprendimiento.html")


if __name__ == "__main__":
    app.run(debug=True)
