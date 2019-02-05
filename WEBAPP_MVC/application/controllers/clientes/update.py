import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        clientes = config.model_clientes.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update(clientes) # Envia el registro y renderiza update.html
    
    def POST(self,nombre):
        formulario = web.input() # almacena los datos del formulario
        nombre = formulario['nombre'] # almacena el nombre escrito en el input
        ape_pat = formulario['ape_pat'] # almacena el contenido escrito en el input
        ape_mat = formulario['ape_mat'] # alamcena la marca escrito en el input
        colonia = formulario['colonia'] # alamcena el precio escrito en el input
        config.model_clientes.update_clientes(nombre, ape_pat, ape_mat, colonia)
        raise web.seeother('/clientes') # redirecciona al index
