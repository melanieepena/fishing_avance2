from flask import Flask, render_template, request, redirect, session
import mysql.connector
from mysql.connector import Error
<<<<<<< HEAD

=======
>>>>>>> emprendimiento
from userLogic import UserLogic
from userObj import UserObj
from inversorLogic import inversorLogic
from inversorObj import inversorObj
from emprendedorLogic import emprendedorLogic
from fundadorLogic import fundadorLogic
from emprendimientoLogic import emprendimientoLogic
<<<<<<< HEAD
from categoriaLogic import CategoriaLogic
from productosObj import productosObj
from productosLogic import productosLogic
=======
>>>>>>> emprendimiento

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

            # Recoger datos
            nombre = request.form["nombre"]
            biografia = request.form["biografia"]
            email = request.form["email"]
            id_usuario = request.form["id_usuario"]
            pais = request.form["pais"]
            ciudad = request.form["ciudad"]

            try:
                logic.insertNewInversor(
                    nombre, biografia, email, id_usuario, pais, ciudad
                )
                message = "Se ha insertado un nuevo inversionista"
                data = logic.getAllInversionista()

            except mysql.connector.Error as error:
                print("Failed inserting BLOB data into MySQL table {}".format(error))
                message = "No se puede insertar. No existe el id usuario"
                data = logic.getAllInversionista()

            return render_template("inversionista.html", data=data, message=message)

        # Eliminar
        elif formId == 2:
            id = int(request.form["id"])

            try:
                logic.deleteInversionista(id)
                data = logic.getAllInversionista()
                message = "Se ha eliminado un usuario de inversionista"

            except mysql.connector.Error as error:
                print("Failed inserting BLOB data into MySQL table {}".format(error))
                message = (
                    "No se puede eliminar. Afecta la integridad de la base de datos"
                )
                data = logic.getAllInversionista()

            return render_template("inversionista.html", data=data, message=message)

        # Update
        elif formId == 3:
            id = int(request.form["id"])
            nombre = request.form["nombre"]
            biografia = request.form["biografia"]
            email = request.form["email"]
            id_usuario = request.form["id_usuario"]
            pais = request.form["pais"]
            ciudad = request.form["ciudad"]

            verdadero = True
            data = logic.getAllInversionista()
            return render_template(
                "inversionista.html",
                data=data,
                message=message,
                verdadero=verdadero,
                id=id,
                nombre=nombre,
                biografia=biografia,
                email=email,
                id_usuario=id_usuario,
                pais=pais,
                ciudad=ciudad,
            )

        # Modificar inversionista
        else:
            id = int(request.form["id"])
            nombre = request.form["nombre"]
            biografia = request.form["biografia"]
            email = request.form["email"]
            id_usuario = request.form["id_usuario"]
            pais = request.form["pais"]
            ciudad = request.form["ciudad"]

            try:
                logic.updateInversionista(
                    id, nombre, biografia, email, id_usuario, pais, ciudad
                )
                data = logic.getAllInversionista()
                message = "Se ha modificado el inversionista"

            except mysql.connector.Error as error:
                print("Failed inserting BLOB data into MySQL table {}".format(error))
                message = "No se puede modificar. No existe el id usuario"
                data = logic.getAllInversionista()

            return render_template("inversionista.html", data=data, message=message)

    # -------------------------------------------------------------------------------------------------------------------


@app.route("/emprendedor")
def emprendedor():
    return render_template("emprendedor.html")


@app.route("/productos", methods=["POST", "GET"])
def productos():
    logic = productosLogic()
    datos = logic.getAllProductoLen()
    message = ""
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
                    try:
                        logic.insertNewProducto(
                            nombre, foto, desc, costo, precio, patente, idEmp
                        )
                    except mysql.connector.Error as error:
                        print(
                            "Failed inserting BLOB data into MySQL table {}".format(
                                error
                            )
                        )
                        message = (
                            "No se puede eliminar. Afecta la integridad de los datos"
                        )
                    datos = logic.getAllProductoLen()
                    return render_template(
                        "productos.html", datosx=datos, mostrar=False, message=message
                    )

        return render_template("productos.html", datosx=datos, mostrar=False)


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


@app.route("/categoria", methods=["GET", "POST"])
def categoria():
<<<<<<< HEAD
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
=======
    return render_template("emprendimiento.html")
>>>>>>> emprendimiento


if __name__ == "__main__":
    app.run(debug=True)
