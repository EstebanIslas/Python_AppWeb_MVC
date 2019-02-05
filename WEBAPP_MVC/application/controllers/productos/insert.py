import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre = formulario['nombre'] # almacena el nombre escrito en el input
        marca = formulario['marca'] # almacena el contenido escrito en el input
        clase = formulario['clase'] # alamcena la marca escrito en el input
        precio = formulario['precio'] # alamcena el precio escrito en el input
        config.model_productos.insert_productos(nombre, marca, clase, precio) # llama al metodo insert_clientes y le paso los datos guardados
        raise web.seeother('/productos') # redirecciona al index.html
