var n = 1;
var i = 0;

//ruta de fotos
function getImagePath() { 
    i = i + 1; 
    return "/static/imagenes/f"+i+".PNG"; 
}

//poner ruta dinamica de fotos
function img_src(val) {
    var a = document.body.getElementsByTagName('IMG');
    var img = a?a[a.length-1]:0;
    if (img) img.src = val;
}

//mostrar y ocultar tablas
$(document).ready(function(){
    var elem = document.getElementById("clase");
    elem.onchange = function(){        
        if(this.value == "cliente"){
            var cliente = document.getElementById("tableCliente");
            cliente.style.display = "block";

            var producto = document.getElementById("tableProducto");
            producto.style.display = "none";

            var factura = document.getElementById("tableFactura");
            factura.style.display = "none";
        }  
        else if(this.value == "producto"){
            var cliente = document.getElementById("tableCliente");
            cliente.style.display = "none";

            var producto = document.getElementById("tableProducto");
            producto.style.display = "block";

            var factura = document.getElementById("tableFactura");
            factura.style.display = "none";
        }    
        else if(this.value == "factura"){
            var cliente = document.getElementById("tableCliente");
            cliente.style.display = "none";

            var producto = document.getElementById("tableProducto");
            producto.style.display = "none";

            var factura = document.getElementById("tableFactura");
            factura.style.display = "block";
        }      
    };
});

// Crear nuevo input para productos
function newInput() {
var input = $("<div id='p"+ n +"' class='row form-group'><div class='col'><label>Producto:</label><select class='form-control' name='producto"+ n +"'id='idProducto"+ n +"' required='1'>{% for score in codigos %}<option value={{score.0}}> {{score.0}} </option>{% endfor %}</select></div><div class='col'><label>Cantidad:</label><input type='text' class='form-control' name='cantidad"+ n +"' id='idCantidad "+ n +"' required='1'></div></div>")
.prependTo("#idFrmFactura");
$("div#p".concat(n-1)).after(input);
n = n + 1;
$("#idNumProductos").val(n);
}

function deleteInput(){
    $("div#p".concat(n-1)).remove();
    n = n - 1;
    $("#idNumProductos").val(n);
}

//insertar
function insertar(){
    var elem = document.getElementById("clase");
    var clase = elem.value;

    if(clase == 'cliente'){
        $("#idCedula").val('');
        $("#idNombre1").val('');
        $("#idNombre2").val('');
        $("#idApellido1").val('');
        $("#idApellido2").val('');
        $("#idDireccion").val('');
        $("#idTelefono").val('');
        $("#idFoto").val('');

        //Datos de boton y titulo para el modal
        $("#idBtnOperacionCliente").html('Insertar');
        $("#idTituloDialogoCliente").html('Insertar cliente');

        //Habilitar los datos
        $("#idCedula").prop("disabled", false);
        $("#idNombre1").prop("disabled", false);
        $("#idNombre2").prop("disabled", false);
        $("#idApellido1").prop("disabled", false);
        $("#idApellido2").prop("disabled", false);
        $("#idDireccion").prop("disabled", false);
        $("#idTelefono").prop("disabled", false);
        $("#idFoto").prop("disabled", false);

        //Url de accion
        $("#idFrmCliente").attr('action', "{{url_for('insertCliente')}}");
        $('#idDlgCliente').modal('show');
    }

    else if(clase == 'producto'){
        $("#idCodigo").val('');
        $("#idCategoria").val('');
        $("#idNombre").val('');
        $("#idPrecio").val('');
        $("#idStock").val('');
        $("#idEstado").val('');

        //Datos de boton y titulo para el modal
        $("#idBtnOperacionProducto").html('Insertar');
        $("#idTituloDialogoProducto").html('Insertar producto');

        //Habilitar los datos
        $("#idCodigo").prop("disabled", false);
        $("#idCategoria").prop("disabled", false);
        $("#idNombre").prop("disabled", false);
        $("#idPrecio").prop("disabled", false);
        $("#idStock").prop("disabled", false);
        $("#idEstado").prop("disabled", false);

        //Url de accion
        $("#idFrmProducto").attr('action', "{{url_for('insertProducto')}}");
        $('#idDlgProducto').modal('show');
    }
    
    else if(clase == 'factura'){
        var btn = document.getElementById("btnNuevoProducto");
        btn.style.display = "block";

        $("#idFactura").val('');
        $("#idNumProductos").val(n);
        $("#idCodigoF").val('');
        $("#idCliente").val('');
        $("#idProducto0").val('');
        $("#idCantidad0").val('');
        $("#idFecha").val('');
        $("#idTotal").val('');
        $("#idMetodoPago").val('');

        //Datos de boton y titulo para el modal
        $("#idBtnOperacionFactura").html('Insertar');
        $("#idTituloDialogoFactura").html('Insertar factura');

        //Habilitar los datos
        $("#idFactura").prop("disabled", false);
        $("#idCodigoF").prop("disabled", false);
        $("#idCliente").prop("disabled", false);
        $("#idProducto0").prop("disabled", false);
        $("#idCantidad0").prop("disabled", false);
        $("#idFecha").prop("disabled", false);
        $("#idTotal").prop("disabled", true);
        $("#idMetodoPago").prop("disabled", false);

        //Url de accion
        $("#idFrmFactura").attr('action', "{{url_for('insertFactura')}}");
        $('#idDlgFactura').modal('show');
    }
}

//Editar
function editarCliente(cedula, nombre1, nombre2, apellido1, apellido2, direccion, telefono){
        $("#idCedula").val(cedula);
        $("#idNombre1").val(nombre1);
        $("#idNombre2").val(nombre2);
        $("#idApellido1").val(apellido1);
        $("#idApellido2").val(apellido2);
        $("#idDireccion").val(direccion);
        $("#idTelefono").val(telefono);
        $("#idFoto").val('');

        //Datos de boton y titulo para el modal
        $("#idBtnOperacionCliente").html('Editar');
        $("#idTituloDialogoCliente").html('Editar cliente');

        //Habilitar los datos
        $("#idCedula").prop("disabled", true);
        $("#idNombre1").prop("disabled", false);
        $("#idNombre2").prop("disabled", false);
        $("#idApellido1").prop("disabled", false);
        $("#idApellido2").prop("disabled", false);
        $("#idDireccion").prop("disabled", false);
        $("#idTelefono").prop("disabled", false);
        $("#idFoto").prop("disabled", false);

        //Url de accion
        $("#idFrmCliente").attr('action', '{{url_for("updateCliente")}}');
        $('#idDlgCliente').modal('show');        
}

//Editar Producto
function editarProducto(codigo, categoria, nombre, precio, stock, estado){
    $("#idCodigo").val(codigo);
    $("#idCategoria").val(categoria);
    $("#idNombre").val(nombre);
    $("#idPrecio").val(precio);
    $("#idStock").val(stock);
    $("#idEstado").val(estado);

    //Datos de boton y titulo para el modal
    $("#idBtnOperacionProducto").html('Editar');
    $("#idTituloDialogoProducto").html('Editar Cliente');

    //Habilitar los datos
    $("#idCodigo").prop("disabled", true);
    $("#idCategoria").prop("disabled", false);
    $("#idNombre").prop("disabled", false);
    $("#idPrecio").prop("disabled", false);
    $("#idStock").prop("disabled", false);
    $("#idEstado").prop("disabled", false);

    //Url de accion
    $("#idFrmProducto").attr('action', "{{url_for('updateProducto')}}");
    $('#idDlgProducto').modal('show');
}

//Editar Factura
function editarFactura(id, codigoF, cliente, producto, cantidad, fecha, total, metodoPago){
    
    var btn = document.getElementById("btnNuevoProducto");
    btn.style.display = "none";

    $("#idFactura").val(id);
    $("#idCodigoF").val(codigoF);
    $("#idCliente").val(cliente);
    $("#idProducto0").val(producto);
    $("#idCantidad0").val(cantidad);
    $("#idFecha").val(fecha);
    $("#idTotal").val(total);
    $("#idMetodoPago").val(metodoPago);

    //Datos de boton y titulo para el modal
    $("#idBtnOperacionFactura").html('Editar');
    $("#idTituloDialogoFactura").html('Editar Cliente');

    //Habilitar los datos
    $("#id").prop("disabled", true);
    $("#idCodigoF").prop("disabled", true);
    $("#idCliente").prop("disabled", false);
    $("#idProducto0").prop("disabled", true);
    $("#idCantidad0").prop("disabled", false);
    $("#idFecha").prop("disabled", false);
    $("#idTotal").prop("disabled", true);
    $("#idMetodoPago").prop("disabled", false);

    //Url de accion
    $("#idFrmFactura").attr('action', "{{url_for('updateFactura', filename='crud.py')}}");
    $('#idDlgFactura').modal('show');
}

//Eliminar
function eliminarCliente(cedula, nombre1, nombre2, apellido1, apellido2, direccion, telefono){
    $("#idCedula").val(cedula);
    $("#idNombre1").val(nombre1);
    $("#idNombre2").val(nombre2);
    $("#idApellido1").val(apellido1);
    $("#idApellido2").val(apellido2);
    $("#idDireccion").val(direccion);
    $("#idTelefono").val(telefono);
    $("#idFoto").val(foto);

    //Datos de boton y titulo para el modal
    $("#idBtnOperacionCliente").html('Eliminar');
    $("#idTituloDialogoCliente").html('Eliminar cliente');

    //Habilitar los datos
    $("#idCedula").prop("disabled", true);
    $("#idNombre1").prop("disabled", true);
    $("#idNombre2").prop("disabled", true);
    $("#idApellido1").prop("disabled", true);
    $("#idApellido2").prop("disabled", true);
    $("#idDireccion").prop("disabled", true);
    $("#idTelefono").prop("disabled", true);
    $("#idFoto").prop("disabled", true);

    //Url de accion
    $("#idFrmCliente").attr('action', '{{url_for("delete")}}');
    $('#idDlgCliente').modal('show');        
}