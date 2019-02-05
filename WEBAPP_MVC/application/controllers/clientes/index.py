import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        clientes = config.model_clientes.select_clientes().list() # Selecciona todos los registros de producto
        return config.render.index(clientes) # Envia registros y renderiza index.html
