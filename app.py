from flask import Flask, render_template, request, redirect, session
from userLogic import UserLogic
from userObj import UserObj
from inversorLogic import inversorLogic
from inversorObj import inversorObj
from emprendedorLogic import emprendedorLogic
from categoriaLogic import CategoriaLogic

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


@app.route("/fundadores")
def fundadores():
    return render_template("fundadores.html")


@app.route("/emprendimiento")
def emprendimiento():
    return render_template("emprendimiento.html")


@app.route("/categoria", methods=["GET", "POST"])
def categoria():
    logic = CategoriaLogic()
    massage = ""
    verdadero = False
    if request.method == "GET":
        data = logic.getAllCategorias()
        return render_template("categoria.html", data=data, massage=massage)
    elif request.method == "POST":
        formId = int(request.form["formId"])
        # Inserta una categoría
        if formId == 1:
            categoria = request.form["categoria"]
            logic.insertCategoria(categoria)
            massage = "Se ha insertado un nuevo usuario"
            data = logic.getAllCategorias()
            return render_template("categoria.html", data=data, massage=massage)
        # Elimina una categoria
        elif formId == 2:
            id = int(request.form["id"])
            logic.deleteCategoria(id)
            massage = "Se ha eliminado un usuario"
            data = logic.getAllCategorias()
            return render_template("categoria.html", data=data, massage=massage)
        # Va al form para dar update
        elif formId == 3:
            id = int(request.form["id"])
            categoria = request.form["categoria"]
            verdadero = True
            data = logic.getAllCategorias()
            return render_template(
                "categoria.html",
                data=data,
                verdadero=verdadero,
                categoria=categoria,
                id=id,
            )
        # Modifica una categoria
        else:
            massage = "Se ha insertado un nuevo usuario"
            return render_template("categoria.html", data=data, massage=massage)


if __name__ == "__main__":
    app.run(debug=True)
