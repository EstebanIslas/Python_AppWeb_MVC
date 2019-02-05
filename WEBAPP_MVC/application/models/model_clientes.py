import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config


#Metodo para seleccionar todos los registros de la tabla clientes

def select_clientes():
    try:
        return db.select('clientes') # Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_clientes Error {}".format(e.args)
        print "Model select_clientes Message {}".format(e.message)
        return None


#Metodo para seleccionar un registro que coincida con el nombre dado

def select_nombre(nombre):
    try:
        return db.select('clientes',where='nombre=$nombre', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None


#Metodo para insertar un nuevo registro 

def insert_clientes(nombre,ape_pat,ape_mat,colonia):
    try:
        return db.insert('clientes', 
        nombre=nombre,
        ape_pat=ape_pat,
        ape_mat=ape_mat,
        colonia=colonia) # inserta un registro en producto
    except Exception as e:
        print "Model insert_clientes Error {}".format(e.args)
        print "Model insert_clientes Message {}".format(e.message)
        return None


#Metodo para eliminar un registro que coincida con el nombre recibido

def delete_clientes(nombre):
    try:
        return db.delete('clientes', where='nombre=$nombre',vars=locals()) # borra un registro de clientes
    except Exception as e:
        print "Model delete_clientes Error {}".format(e.args)
        print "Model delete_clientes Message {}".format(e.message)
        return None


#Metodo para actualizar los datos, del nombre recibido

def update_clientes(nombre,ape_pat,ape_mat,colonia): # actualiza los datos de la tabla clientes que coincidan con el nombre
    try:
        return db.update('clientes',
            ape_pat=ape_pat,
            ape_mat=ape_mat,
            colonia=colonia, 
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_clientes Error {}".format(e.args)
        print "Model update_clientes Message {}".format(e.message)
        return None
