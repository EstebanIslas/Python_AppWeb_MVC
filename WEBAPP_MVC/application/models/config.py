import web

#Parametros de configuracion para conectarse a una base de datos
#MySQL o MariaDB

db = web.database(
    dbn='mysql', # motor de base de datos
    host='localhost', # ruta del servidor
    db='ria_iniciales', # nombre de la base de datos
    user='steph', # usuario privilegiado
    pw='steph.2019', # password del usuario
    port = 3306 # puerto de mariadb
    )