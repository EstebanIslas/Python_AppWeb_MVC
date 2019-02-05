import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config


#Metodo para seleccionar todos los registros de la tabla clientes

def select_productos():
    try:
        return db.select('productos') # Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_productos Error {}".format(e.args)
        print "Model select_productos Message {}".format(e.message)
        return None


#Metodo para seleccionar un registro que coincida con el nombre dado

def select_nombre(nombre):
    try:
        return db.select('productos',where='nombre=$nombre', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None


#Metodo para insertar un nuevo registro 

def insert_productos(nombre, marca, clase, precio):
    try:
        return db.insert('productos', 
        nombre=nombre,
        marca=marca,
        clase=clase,
        precio=precio) # inserta un registro en producto
    except Exception as e:
        print "Model insert_productos Error {}".format(e.args)
        print "Model insert_productos Message {}".format(e.message)
        return None


#Metodo para eliminar un registro que coincida con el nombre recibido

def delete_productos(nombre):
    try:
        return db.delete('productos', where='nombre=$nombre',vars=locals()) # borra un registro de clientes
    except Exception as e:
        print "Model delete_productos Error {}".format(e.args)
        print "Model delete_productos Message {}".format(e.message)
        return None


#Metodo para actualizar los datos, del nombre recibido

def update_productos(nombre, marca, clase, precio): # actualiza los datos de la tabla clientes que coincidan con el nombre
    try:
        return db.update('productos',
            marca=marca,
            clase=clase,
            precio=precio, 
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_productos Error {}".format(e.args)
        print "Model update_productos Message {}".format(e.message)
        return None
