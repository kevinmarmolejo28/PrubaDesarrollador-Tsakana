#Borrar el esque existente 
drop schema if exists tsakana;

#Crear el esquema 
create schema tsakana;

#seleccionar esquema para trabajar
use tsakana;

#Borrar tablas si existen
drop table if exists cliente;
drop table if exists producto;
drop table if exists factura;

CREATE TABLE cliente(
cedula int (12) NOT NULL,
nombre1 varchar (10) NOT NULL,
nombre2 varchar (10),
apellido1 varchar (20) NOT NULL,
apellido2 varchar (20) NOT NULL,
direccion varchar (20) NOT NULL,
telefono bigint NOT NULL,
foto varchar (10) NOT NULL,
PRIMARY KEY (cedula));

CREATE TABLE producto(
codigo varchar (10) NOT NULL,
categoria varchar (20) NOT NULL,
nombre varchar (20) NOT NULL,
precio double NOT NULL,
cantidad int (5) NOT NULL,
estado varchar (10) NOT NULL,
PRIMARY KEY (codigo));

CREATE TABLE factura(
id int (5) auto_increment NOT NULL,
codigoF int(5) NOT NULL,
cedulaC int (12) NOT NULL,
codigoP varchar (10) NOT NULL,
cantidad int (5) NOT NULL,
fecha datetime NOT NULL,
total double NOT NULL,
metodoPago varchar (10) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (cedulaC) REFERENCES cliente(cedula),
FOREIGN KEY (codigoP) REFERENCES producto(codigo));