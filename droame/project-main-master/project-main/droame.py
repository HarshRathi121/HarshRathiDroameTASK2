import sqlite3

# This .py file create two tables customer and bookings
# When you will run this file droame.db database will be created

con = sqlite3.connect("droame.db")
print("Database opened successfully")  

con.execute("create table customer (customer_id INTEGER PRIMARY KEY , customer_name VARCHAR NOT NULL, customer_email VARCHAR UNIQUE NOT NULL, customer_phone INTEGER UNIQUE NOT NULL, booking_date INTEGER NOT NULL)" )
con.execute("create table bookings (booking_id INTEGER PRIMARY KEY , location_id VARCHAR NOT NULL, drone_shot_id VARCHAR NOT NULL, created_time INTEGER NOT NULL,customer_id INTEGER NOT NULL,  FOREIGN KEY (customer_id) REFERENCES customer(customer_id))")



                                                                                                                   
print("Table created successfully")  
  
con.close()
  
