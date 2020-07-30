from flask import Flask, render_template, request, redirect, session
from userLogic import UserLogic
from userObj import UserObj
from inversorLogic import inversorLogic
from inversorObj import inversorObj
from emprendedorLogic import emprendedorLogic

app = Flask(__name__)
app.secret_key = "ILoveFishing"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/inversionista", methods=["GET", "POST"])
def inversionista():
    logic = inversorLogic()
    message = ""
    verdadero = False
    if request.method == "GET":
        data = logic.getAllInversionista()
        return render_template("inversionista.html", data=data, message=message)

    elif request.method == "POST":  # "POST"
        formId = int(request.form["formId"])
        # Insertar
        if formId == 1:
            nombre = request.form["nombre"]
            biografia = request.form["biografia"]
            email = request.form["email"]
            id_usuario = request.form["idUsuario"]
            pais = request.form["pais"]
            ciudad = request.form["ciudad"]

            logic.insertNewInversor(nombre, biografia, email, id_usuario, pais, ciudad)
            message = "Se ha insertado un nuevo inversionista"
            data = logic.getAllInversionista()
            return render_template("inversionista.html", data=data, message=message)

        # Eliminar
        elif formId == 2:
            id = int(request.form["id"])
            logic.deleteInversionista(id)
            massage = "Se ha eliminado un usuario de inversionista"
            data = logic.getAllInversionista()
            return render_template("inversionista.html", data=data, message=message)
        # Update
        elif formId == 3:
            id = int(request.form["id"])
            nombre = request.form["nombre"]
            biografia = request.form["biografia"]
            email = request.form["email"]
            id_usuario = request.form["idUsuario"]
            pais = request.form["pais"]
            ciudad = request.form["ciudad"]

            verdadero = True
            data = logic.getAllInversionista()
            return render_template(
                "inversionista.html",
                data=data,
                verdadero=verdadero,
                id=id,
                nombre=nombre,
                biografia=biografia,
                email=email,
                id_usuario=id_usuario,
                pais=pais,
                ciudad=ciudad,
            )

        # Modifica una categoria
        else:
            id = int(request.form["id"])
            nombre = request.form["nombre"]
            biografia = request.form["biografia"]
            email = request.form["email"]
            id_usuario = request.form["idUsuario"]
            pais = request.form["pais"]
            ciudad = request.form["ciudad"]

            logic.updateInversionista(
                id, nombre, biografia, email, id_usuario, pais, ciudad,
            )
            data = logic.getAllInversionista()
            massage = "Se ha modificado el inversionista"
            return render_template("inversionista.html", data=data, message=message)

    # -------------------------------------------------------------------------------------------------------------------


@app.route("/emprendedor")
def emprendedor():
    return render_template("emprendedor.html")


@app.route("/productos")
def productos():
    return render_template("productos.html")


@app.route("/fundadores")
def fundadores():
    return render_template("fundadores.html")


@app.route("/emprendimiento")
def emprendimiento():
    return render_template("emprendimiento.html")


@app.route("/categoria")
def categoria():
    return render_template("categoria.html")


if __name__ == "__main__":
    app.run(debug=True)
