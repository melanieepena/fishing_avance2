from flask import Flask, render_template, request, redirect, session
import mysql.connector
from mysql.connector import Error
from userLogic import UserLogic
from userObj import UserObj
from inversorLogic import inversorLogic
from inversorObj import inversorObj
from emprendedorLogic import emprendedorLogic
from categoriaLogic import CategoriaLogic
from productosObj import productosObj
from productosLogic import productosLogic

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


@app.route("/productos", methods=["POST", "GET"])
def productos():
    logic = productosLogic()
    datos = logic.getAllProductoLen()
    if request.method == "GET":
        return render_template("productos.html", datosx=datos, mostrar=False)

    elif request.method == "POST":
        if request.form.get("formId"):
            formId = int(request.form["formId"])
            if formId == 1:
                id_prod = request.form["idColumnaU"]
                nameOld = request.form["NameU"]
                fotoOld = request.form["fotoU"]
                descOld = request.form["descU"]
                costoOld = request.form["costoU"]
                precioOld = request.form["precioU"]
                patenteOld = request.form["patenteU"]
                id_empOld = request.form["idEmpU"]
                return render_template(
                    "productos.html",
                    mostrar=True,
                    idx=id_prod,
                    nameUpx=nameOld,
                    fotoUpx=fotoOld,
                    descUpx=descOld,
                    costoUpx=costoOld,
                    precioUpx=precioOld,
                    patenteUpx=patenteOld,
                    empex=id_empOld,
                    datosx=datos,
                )
            if formId == 2:
                id_prod = int(request.form["idxForm"])
                name = request.form["nameUp"]
                foto = request.form["fotoUp"]
                desc = request.form["descUp"]
                costo = float(request.form["costoUp"])
                precio = float(request.form["precioUp"])
                patente = int(request.form["patenteUp"])
                logic.updateProducto(id_prod, name, foto, desc, costo, precio, patente)
                datos = logic.getAllProductoLen()
                render_template("productos.html", datosx=datos, mostrar=False)
            if formId == 3:
                id_prod = request.form["idColumnaD"]
                logic.deleteProducto(id_prod)
                datos = logic.getAllProductoLen()
                render_template("productos.html", datosx=datos, mostrar=False)
            if formId == 4:
                nombre = request.form["newName"]
                foto = request.form["newFoto"]
                desc = request.form["newDesc"]
                costo = float(request.form["newCosto"])
                precio = float(request.form["newPrecio"])
                patente = int(request.form["newPatente"])
                idEmp = int(request.form["newId_emp"])

                if (
                    nombre != ""
                    and desc != ""
                    and costo != ""
                    and precio != ""
                    and patente != ""
                    and idEmp != ""
                ):
                    logic = productosLogic()
                    logic.insertNewProducto(
                        nombre, foto, desc, costo, precio, patente, idEmp
                    )
                datos = logic.getAllProductoLen()
                return render_template("productos.html", datosx=datos, mostrar=False)
        return render_template("productos.html", datosx=datos, mostrar=False)


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

            try:
                logic.deleteCategoria(id)
                massage = "Se ha eliminado un usuario"
                data = logic.getAllCategorias()

            except mysql.connector.Error as error:
                print("Failed inserting BLOB data into MySQL table {}".format(error))
                massage = "No se puede eliminar. Afecta la integridad de los datos"
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
            id = int(request.form["id"])
            categoria = request.form["categoria"]
            logic.updateCategoria(id, categoria)
            data = logic.getAllCategorias()
            massage = "Se ha modificado el usuario"
            return render_template("categoria.html", data=data, massage=massage)


if __name__ == "__main__":
    app.run(debug=True)
