import database
mycursor = database.mydb.cursor()
#--------------------------------------#
def selectdb(table):
    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)
    show = mycursor.fetchall()
    return show
#--------------------------------------#
def deletedb(table,id_name,id):
    sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
    mycursor.execute(sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print (deletedb("products","product_id",2))
#--------------------------------------#
def editdb(table,colum,id_name,id,val):
    sql = f"UPDATE {table} SET {colum} = %s WHERE {id_name} = %s"
    val_sql = (val,id)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print (editdb("products","stock","product_id",2,10))
#--------------------------------------#
def insert_product(name,description,price,stock):
    sql = "INSERT INTO products VALUES ( %s, %s, %s, %s ,%s)"
    val_sql = (None,name,description,price,stock)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0 :
        return True
    else:
        return False
#print (insert_product("bin","ถังขยะ",50,100))
#--------------------------------------#
def insert_categories(name):
    sql = "INSERT INTO categories VALUES (%s,%s)"
    val_sql = (None,name)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
#print(insert_categories("เสื้อผ้า"))
#--------------------------------------#
def insert_users(name,password,email,role):
    sql = "INSERT INTO users VALUES (%s,%s,%s,%s,%s)"
    val_sql = (None,name,password,email,role)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
#print(insert_users('Thanchanok',123456,'Thanchanok@gmail.com','admin'))
#--------------------------------------#
def insert_order(date,amount,status):
    sql = "INSERT INTO orders VALUES (%s,%s,%s,%s)"
    val_sql = (None,date,amount,status)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
#print(insert_order('11/11/2568',2888,'ยกเลิกรายการ'))