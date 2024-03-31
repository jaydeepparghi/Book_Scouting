# importing required libraries
import mysql.connector

def addUser(fname,lname,contact,email,password):
    dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="2141",
    database='BookScouting'
    )
    # preparing a cursor object
    cursorObject = dataBase.cursor()
    cursorObject.execute('select * from users')
    uid=len(cursorObject.fetchall())+1
    query = f"Insert into users values('{uid}','{fname}','{lname}','{email}','{contact}','{password}','Buyer')"
    cursorObject.execute(query)
    dataBase.commit()
    myresult = cursorObject.fetchall()

    # print(myresult)
    return myresult

def loginUser(email,password):
    dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="2141",
    database='BookScouting'
    )
    # preparing a cursor object
    cursorObject = dataBase.cursor()

    query = f"select * from users where email='{email}' and password='{password}'"
    cursorObject.execute(query)
    
    myresult = cursorObject.fetchall()

    dataBase.close()
    return myresult

def getUserDetails(uid):
    dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="2141",
    database='BookScouting'
    )
    # preparing a cursor object
    cursorObject = dataBase.cursor()

    query = f"select * from users where uid='{uid}'"
    cursorObject.execute(query)
    
    myresult = cursorObject.fetchall()

    dataBase.close()
    return myresult


def getAvailableBooks():
    dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="2141",
    database='BookScouting'
    )
    # preparing a cursor object
    cursorObject = dataBase.cursor()

    query = f"select * from book"
    cursorObject.execute(query)
    
    myresult = cursorObject.fetchall()

    dataBase.close()
    return myresult
    

def addBookToCart(uid,book_id,status):
    dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="2141",
    database='BookScouting'
    )
    # preparing a cursor object
    print(uid,book_id,status)
    cursorObject = dataBase.cursor()

    query = f"Insert into cart values('{uid}','{book_id}','{status}')"
    cursorObject.execute(query)
    dataBase.commit()
    myresult = cursorObject.fetchall()

    # print(myresult)
    return myresult


def getCartDetails(uid):
    # preparing a cursor object
    cursorObject = dataBase.cursor()

    query = f"select * from cart where uid='{uid}'"
    cursorObject.execute(query)
    
    myresult = cursorObject.fetchall()
    return myresult


def deleteFromCart(uid,book_id):
    # preparing a cursor object
    cursorObject = dataBase.cursor()

    query = f"delete from cart where uid='{uid}' and book_id='{book_id}'"
    cursorObject.execute(query)
    dataBase.commit()
    myresult = cursorObject.fetchall()
    return myresult

# addToCart('2A','2','2','Cancelled')
# print(getCartDetails('1A'))
# deleteFromCart('2A','2')
# for i in getBooks():
#     print(i)
# print(getUserDetails('1A'))

# Disconnecting from the server
