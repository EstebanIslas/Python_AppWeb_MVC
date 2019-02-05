import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, nombre): 
        clientes = config.model_clientes.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.delete(clientes) # Envia el registro y renderiza delete.html
    
    def POST(self, nombre):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        nombre = formulario['nombre'] # Obtine el nombre almacenado en el formulario
        config.model_clientes.delete_clientes(nombre) # Borra el registro del nombre seleccionado
        raise web.seeother('/clientes')
