create database ria_iniciales;
use ria_iniciales;
create table clientes(
    id_clientes int(4) not null auto_increment primary key ,
    nombre varchar(20)not null,
    ape_pat varchar(30) not null,
    ape_mat varchar (30) not null,
    colonia varchar(30) not null);

create table productos(
    id_producto int(4) not null auto_increment primary key,
    nombre varchar(20) not null,
    marca varchar(10) not null,
    clase varchar(20) not null,
    precio int(7) not null);

insert into clientes(nombre,ape_pat,ape_mat,colonia)values
('Esteban','Islas','Santos','Santiago'),
('Andrea','Serrano','Guerrero','El paraiso'),
('Jessica','Tellez','Galindo','Acaxochi');

insert into productos (nombre,marca,clase,precio)values
('Papas','Sabritas','Frituras','10'),
('Cerveza','Tecate','Bebidas','32'),
('Refresco','CocaCola','Bebidas','28');

show tables;

select * from clientes;
describe clientes;

select * from productos;
describe productos;

create user 'steph'@'localhost' IDENTIFIED BY 'steph.2019';
Grant ALL PRIVILEGES ON ria_iniciales.* TO'steph'@'localhost';
FLUSH PRIVILEGES;
