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


@app.route("/inversionista")
def inversionista():
    return render_template("inversionista.html")


@app.route("/emprendedor", methods=["GET", "POST"])
def emprendedor():
    logic = emprendedorLogic()
    message = ""
    verdadero = False
    if request.method == "GET":
        data = logic.getAllEmprendedores()
        return render_template("emprendedor.html", data=data, message=message)
    elif request.method == "POST":
        formId = int(request.form["formId"])
        # Inserta una categoría
        if formId == 1:
            nombre = request.form["nombre"]
            email = request.form["email"]
            telefono = request.form["telefono"]
            id_usuario = request.form["id_usuario"]
            pais = request.form["pais"]
            ciudad = request.form["ciudad"]
            biografia = request.form["biografia"]
            logic.insertNewEmprendedor(
                nombre, email, telefono, id_usuario, pais, ciudad, biografia
            )
            data = logic.getAllEmprendedores()
            message = "Se ha insertado un nuevo usuario"
            return render_template("emprendedor.html", data=data, message=message)
        # Elimina una categoria
        elif formId == 2:
            id = int(request.form["id"])
            logic.deleteEmprendedor(id)
            data = logic.getAllEmprendedores()
            message = "Se ha eliminado un usuario"
            return render_template("emprendedor.html", data=data, message=message)
        # Va al form para dar update
        elif formId == 3:
            id = int(request.form["id"])
            nombre = request.form["nombre"]
            email = request.form["email"]
            telefono = request.form["telefono"]
            id_usuario = request.form["id_usuario"]
            pais = request.form["pais"]
            ciudad = request.form["ciudad"]
            biografia = request.form["biografia"]
            verdadero = True
            data = logic.getAllEmprendedores()
            return render_template(
                "emprendedor.html",
                data=data,
                message=message,
                verdadero=verdadero,
                id=id,
                nombre=nombre,
                email=email,
                telefono=telefono,
                id_usuario=id_usuario,
                pais=pais,
                ciudad=ciudad,
                biografia=biografia,
            )
        # Modifica una categoria
        else:
            id = int(request.form["id"])
            nombre = request.form["nombre"]
            email = request.form["email"]
            telefono = request.form["telefono"]
            id_usuario = request.form["id_usuario"]
            pais = request.form["pais"]
            ciudad = request.form["ciudad"]
            biografia = request.form["biografia"]
            logic.updateEmprendedor(
                id, nombre, email, telefono, id_usuario, pais, ciudad, biografia
            )
            data = logic.getAllEmprendedores()
            message = "Se ha modificado con éxito"
            return render_template("emprendedor.html", data=data)


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
