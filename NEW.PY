import pymysql
# Creation of PyMySQL Connection Object
try:
    conn = pymysql.connect(host='127.0.0.1', user='root', password='mysql123', db='Face_reco_fill')
except pymysql.MySQLError as e:
    print(e)
    sys.exit()
finally:
    print("Connection established sucessfully")
    conn.close() # You always have to close the connection
