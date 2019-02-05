import web
import application.models.model_clientes as model_clientes # importa el modelo_clientes


render = web.template.render('application/views/clientes/', base='master')
