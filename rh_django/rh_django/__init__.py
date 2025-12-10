import pymysql

# Instalar PyMySQL como si fuera MySQLdb
pymysql.install_as_MySQLdb()

import MySQLdb

setattr(MySQLdb, 'version_info', (2, 2, 2, 'final', 0))
setattr(MySQLdb, '__version__', '2.2.2')