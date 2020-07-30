from flask import Flask, render_template, request, redirect, session
from userLogic import UserLogic
from userObj import UserObj
from inversorLogic import inversorLogic
from inversorObj import inversorObj
from emprendedorLogic import emprendedorLogic
from fundadorLogic import fundadorLogic

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


@app.route("/emprendimiento")
def emprendimiento():
    return render_template("emprendimiento.html")


@app.route("/categoria")
def categoria():
    return render_template("categoria.html")


if __name__ == "__main__":
    app.run(debug=True)
