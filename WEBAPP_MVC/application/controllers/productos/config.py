import web
import application.models.model_productos as model_productos # importa el modelo_clientes


render = web.template.render('application/views/productos/', base='master')
