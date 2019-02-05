import web
        
urls = (
    '/', 'application.controllers.productos.index.Index',
    '/productos', 'application.controllers.productos.index.Index',
    '/insert', 'application.controllers.productos.insert.Insert',
    '/update/(.*)', 'application.controllers.productos.update.Update',
    '/delete/(.*)', 'application.controllers.productos.delete.Delete',
    '/view/(.*)', 'application.controllers.productos.view.View',
    '/clientes', 'application.controllers.clientes.index.Index',
    '/insertclientes', 'application.controllers.clientes.insert.Insert',
    '/updateclientes/(.*)', 'application.controllers.clientes.update.Update',
    '/deleteclientes/(.*)', 'application.controllers.clientes.delete.Delete',
    '/viewclientes/(.*)', 'application.controllers.clientes.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
