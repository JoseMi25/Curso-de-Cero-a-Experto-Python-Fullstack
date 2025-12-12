import pymysql

# 1. Activamos PyMySQL
pymysql.install_as_MySQLdb()

# 2. "Parcheamos" la versión para satisfacer a Django 5
import MySQLdb

# Forzamos la versión a 2.2.1 (tuple: major, minor, patch, level, serial)
if hasattr(MySQLdb, 'version_info'):
    MySQLdb.version_info = (2, 2, 1, 'final', 0)
    MySQLdb.mysql_version = (2, 2, 1, 'final', 0)