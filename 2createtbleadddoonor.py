import mysql.connector

m=mysql.connector.connect(host="localhost",
                          user="root",
                          password="sagar",
                          database="bload_donation")
mc=m.cursor()
s="create table register12(Sr_No int primary key AUTO_INCREMENT , name varchar (50), age int(4),bloadgroup varchar(4),contactno int(20))"
mc.execute(s)
