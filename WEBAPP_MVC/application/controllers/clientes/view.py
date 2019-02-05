import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, nombre):  
        clientes = config.model_clientes.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.view(clientes) # Envia el registro y renderiza view.html
