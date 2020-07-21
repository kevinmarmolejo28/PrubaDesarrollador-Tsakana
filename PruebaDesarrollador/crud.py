#Importar flask
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Crear objeto flask
app = Flask(__name__)

#Llave secreta
app.secret_key = "tsakana"

# Configuracion bd
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'tsakana'

#Objeto Mysql
mysql = MySQL(app)

#Ruta del index
@app.route("/")
def index():

    cur = mysql.connection.cursor()
    #Consulta para clientes
    #Crea y ejecuta la consulta
    sQuery = "SELECT cedula, nombre1, nombre2, apellido1, apellido2, direccion, telefono, foto, (select count(codigoF) from factura where cedulaC = cedula) compras FROM cliente order by compras DESC"
    cur.execute(sQuery)
    #Obtiene los datos
    data1 = cur.fetchall()

    i = 1

    for registro in data1:
        image = registro[7]
        p = "static/imagenes/f"+str(i)+".PNG"
        write_file(image, p)
        i = i + 1 

    #Consulta para productos
    sQuery = "select * from producto"
    cur.execute(sQuery)
    data2 = cur.fetchall()

    #Consulta para facturas
    sQuery = "select id, codigoF, cedulaC, codigoP, cantidad, DATE(fecha), total, metodoPago from factura"
    cur.execute(sQuery)
    data3 = cur.fetchall()

    #Consulta para cedulas de clientes
    sQuery = "select cedula from cliente"
    cur.execute(sQuery)
    data4 = cur.fetchall()

    #Consulta para codigos de productos
    sQuery = "select codigo from producto where estado = 'Activo'"
    cur.execute(sQuery)
    data5 = cur.fetchall()

    cur.close()
    
    return render_template('index.html', clientes = data1, productos = data2, facturas = data3, cedulas = data4, codigos = data5)

@app.route("/insertCliente",methods=['POST'])
def insertCliente():
    #Verifica el metodo
    if(request.method == 'POST'):
        cedula = request.form['cedula']
        primerNombre = request.form['primerNombre']
        segundoNombre = request.form['segundoNombre']
        primerApellido = request.form['primerApellido']
        segundoApellido = request.form['segundoApellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        #foto = request.form['foto']
        f = request.files['inputfile']
        foto = f.read()

        cur = mysql.connection.cursor()

        sQuery = "INSERT INTO cliente (cedula, nombre1, nombre2, apellido1, apellido2, direccion, telefono, foto)"
        sQuery = sQuery + " VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

        try:
            cur.execute(sQuery,(cedula, primerNombre, segundoNombre, primerApellido, segundoApellido, direccion, telefono, foto))

            mysql.connection.commit()

            #Mensaje
            flash("Se ha insertado el dato correctamente", 'alert-success')
        
        except mysql.connection.Error as e:
            flash("Error al insertar el dato:" +str(e), 'alert-warning')

        #Redirige al index
        return redirect(url_for('index'))

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

@app.route("/updateCliente",methods=['POST'])
def updateCliente():
    #Verifica el metodo
    if(request.method == 'POST'):
        cedula = request.form['cedula']
        primerNombre = request.form['primerNombre']
        segundoNombre = request.form['segundoNombre']
        primerApellido = request.form['primerApellido']
        segundoApellido = request.form['segundoApellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        #foto = request.form['foto']
        t = request.files['inputfile']
        foto = t.read()

        cur = mysql.connection.cursor()

        sQuery = "update cliente set nombre1=%s, nombre2=%s, apellido1=%s, apellido2=%s, direccion=%s, telefono=%s, foto=%s"
        sQuery = sQuery + " where cedula=%s"

        sQuery1 = "update cliente set nombre1=%s, nombre2=%s, apellido1=%s, apellido2=%s, direccion=%s, telefono=%s"
        sQuery1 = sQuery1 + " where cedula=%s"
 
        try:
            print (len(str(foto)))
            if len(str(foto)) > 3:
                cur.execute(sQuery,(primerNombre, segundoNombre, primerApellido, segundoApellido, direccion, telefono, foto, cedula))
                mysql.connection.commit()

            else:
                cur.execute(sQuery1,(primerNombre, segundoNombre, primerApellido, segundoApellido, direccion, telefono, cedula))
                mysql.connection.commit()

            flash("Se ha actualizado el dato correctamente", 'alert-success')

        except mysql.connection.Error as e:
            flash("Error al actualizar el dato:" +str(e), 'alert-warning')    
       

        #Redirige al index
        return redirect(url_for('index'))


@app.route("/delete",methods=['POST'])
def delete():
    if(request.method == 'POST'):
        cedula = request.form['cedula']

        cur = mysql.connection.cursor()

        sQuery = "delete from cliente where cedula = %s"

        try:
            cur.execute(sQuery,[cedula])

            mysql.connection.commit()

            #Mensaje
            flash("Se ha eliminado el dato correctamente", 'alert-success')
        
        except mysql.connection.Error as e:
            flash("Error al eliminar el dato:" +str(e), 'alert-warning')

        #Redirige al index
        return redirect(url_for('index'))

##########################################Crud producto######################################
@app.route("/insertProducto",methods=['POST'])
def insertProducto():
    #Verifica el metodo
    if(request.method == 'POST'):
        codigo = request.form['codigo']
        categoria = request.form['categoria']
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        estado = request.form['estado']

        cur = mysql.connection.cursor()

        sQuery = "INSERT INTO producto (codigo, categoria, nombre, precio, cantidad, estado)"
        sQuery = sQuery + " VALUES(%s,%s,%s,%s,%s,%s)"

        try:
            cur.execute(sQuery,(codigo, categoria, nombre, precio, stock, estado))

            mysql.connection.commit()

            #Mensaje
            flash("Se ha insertado el dato correctamente", 'alert-success')
        
        except mysql.connection.Error as e:
            flash("Error al insertar el dato:" +str(e), 'alert-warning')

        #Redirige al index
        return redirect(url_for('index'))

@app.route("/updateProducto",methods=['POST'])
def updateProducto():
    #Verifica el metodo
    if(request.method == 'POST'):
        codigo = request.form['codigo']
        categoria = request.form['categoria']
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        estado = request.form['estado']

        cur = mysql.connection.cursor()

        sQuery = "update producto set categoria=%s, nombre=%s, precio=%s, cantidad=%s, estado=%s"
        sQuery = sQuery + " where codigo=%s"

        cur.execute(sQuery,(categoria, nombre, precio, stock, estado, codigo))

        mysql.connection.commit()

        flash("Se ha actualizado el dato correctamente", 'alert-success')

        #Redirige al index
        return redirect(url_for('index'))


##########################################Crud factura######################################
@app.route("/insertFactura",methods=['POST'])
def insertFactura():
    #Verifica el metodo
    if(request.method == 'POST'):
        numProductos = request.form['numProductos']
        idF = request.form['factura']
        codigoF = request.form['codigoF']
        cliente = request.form['cliente']        
        fecha = request.form['fecha']
        #total = request.form['total']
        metodoPago = request.form['metodoPago']

        cur = mysql.connection.cursor()

        sQuery = "INSERT INTO factura (codigoF, cedulaC, codigoP, cantidad, fecha, total, metodoPago)"
        sQuery = sQuery + " VALUES(%s,%s,%s,%s,%s,%s,%s)"

        try:
            for i in range(int(numProductos)):
                producto = request.form['producto'+str(i)]
                cantidad = request.form['cantidad'+str(i)]

                Query = "select precio, cantidad from producto where codigo = " + producto
                cur.execute(Query)
                precio = cur.fetchall()

                total = 0
                resultado = True

                for registro in precio:
                    costo = registro[0]
                    stock = registro[1]
                    newStock = int(stock)- int(cantidad)

                    if newStock < 0:
                        resultado = False
                        break
                    else:
                        nQuery = "update producto set cantidad=%s"
                        nQuery = nQuery + " where codigo=%s"
                        cur.execute(nQuery,(newStock, producto))
                        mysql.connection.commit()

                        total = int(costo) * int (cantidad)
                        cur.execute(sQuery,(codigoF, cliente, producto, cantidad, fecha, total, metodoPago))
                        mysql.connection.commit()                    
            

            #Mensaje
            if resultado == True:
                flash("Se ha insertado el dato correctamente", 'alert-success')
            else:
                flash("No se puede realizar la factura ya que no hay suficientes productos en stock", 'alert-warning')
        
        except mysql.connection.Error as e:
            flash("Error al insertar el dato:" +str(e), 'alert-warning')

        #Redirige al index
        return redirect(url_for('index'))

@app.route("/updateFactura",methods=['POST'])
def updateFactura():
    #Verifica el metodo
    if(request.method == 'POST'):
        idF = request.form['factura']
        codigoF = request.form['codigoF']
        cliente = request.form['cliente']
        producto = request.form['producto0']
        cantidad = request.form['cantidad0']
        fecha = request.form['fecha']
        total = request.form['total']
        metodoPago = request.form['metodoPago']

        cur = mysql.connection.cursor()

        Query = "select cantidad from producto where codigo = " + producto
        cur.execute(Query)
        numStock = cur.fetchall()

        Query1 = "select cantidad from factura where id = %s"
        cur.execute(Query1,[idF])
        lastCantidad = cur.fetchall()

        print(lastCantidad)
        for cant in lastCantidad:
            oldCantidad = cant[0]
            
        resultado = True

        for registro in numStock:
            stock = registro[0]
            if oldCantidad != cantidad:
                print(oldCantidad)
                print(cantidad)
                if int(oldCantidad) > int(cantidad):
                    val = int(oldCantidad) - int(cantidad)
                    newStock = int(stock) + val
                else:
                    val = int(cantidad) - int(oldCantidad)
                    newStock = int(stock) - val
            else:
                newStock = int(stock)

            if newStock < 0:
                resultado = False
                break
            else:
                nQuery = "update producto set cantidad=%s"
                nQuery = nQuery + " where codigo=%s"
                cur.execute(nQuery,(newStock, producto))
                mysql.connection.commit()

                sQuery = "update factura set codigoF=%s, cedulaC=%s, codigoP=%s, cantidad=%s, fecha=%s, total=%s, metodoPago=%s"
                sQuery = sQuery + " where id=%s"
                cur.execute(sQuery,(codigoF, cliente, producto, cantidad, fecha, total, metodoPago, idF))
                mysql.connection.commit()

            if resultado == True:
                flash("Se ha actualizado el dato correctamente", 'alert-success')
            else:
                flash("No se puede realizar la factura ya que no hay suficientes productos en stock", 'alert-warning')

        #Redirige al index
        return redirect(url_for('index'))

@app.route("/search",methods=['POST'])
def search():
    #Verifica el metodo
    print("entre")
    if(request.method == 'POST'):
        codigo = request.form['codigoFactura']
        total = 0

        cur = mysql.connection.cursor()

        Query = "select codigoF, sum(total) from factura where codigoF = " + codigo
        cur.execute(Query)
        data = cur.fetchall()

        for registro in data:
            codigo = registro[0]
            total = registro[1]
            print(total)

        #Redirige al index
        return render_template('consulta.html', total = total, codigo = codigo)

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
        
@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

#Main para correr el objeto flask
if(__name__ == "__main__"):
    app.run(debug=True)