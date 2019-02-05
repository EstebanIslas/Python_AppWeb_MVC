import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        productos = config.model_productos.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update(productos) # Envia el registro y renderiza update.html
    
    def POST(self,nombre):
        formulario = web.input() # almacena los datos del formulario
        nombre = formulario['nombre'] # almacena el nombre escrito en el input
        marca = formulario['marca'] # almacena el contenido escrito en el input
        clase = formulario['clase'] # alamcena la marca escrito en el input
        precio = formulario['precio'] # alamcena el precio escrito en el input
        config.model_productos.update_productos(nombre, marca, clase, precio)
        raise web.seeother('/productos') # redirecciona al index
