import mysql.connector

# connect to the database server 

try:
    conn = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'indigo'
        )
    mycursor = conn.cursor()
    print('Connection Established')
except: 
    print('Connection Error')
    

#  create a database on db server 

# mycursor.execute('CREATE DATABASE IF NOT EXISTS indigo')
# conn.commit()

# to create a table 

# mycursor.execute(""" CREATE TABLE IF NOT EXISTS airport (
#     airport_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     name VARCHAR(255) NOT NULL
#     ) 
# """)
# conn.commit() 

#  insert data to a table 

# mycursor.execute(""" INSERT INTO airport VALUES 
#                  (1 , 'DEL' , 'New Delhi' , 'IGIA'),
#                  (2 , 'CCU' , 'Kolkata' , 'NSCA'),
#                  (3 , 'BOM' , 'Mumbai' , 'CSMA')
#                  """)

# conn.commit()


# search / retrieve 

# mycursor.execute(""" SELECT * FROM airport 
#                  WHERE airport_id > 1
#                  """)
# data = mycursor.fetchall()
# print(data)

# for i in data:
#     print(i[3]) 


# conn.commit()


# update

# mycursor.execute(""" UPDATE airport SET city = 'Bombay'
#                  WHERE airport_id = 3 """)
# conn.commit()

# delete 

mycursor.execute(""" DELETE FROM airport WHERE airport_id = 3 """)
conn.commit()

# when we are performing write operations then it is mandatory to write conn.commit() also  