from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
# Home Page
@app.route("/")
def index():  
    return render_template("index.html"); 

# Coustomer Adding Page
@app.route("/add")  
def add():  
    return render_template("add.html")  

# Backend working of storing customer information
@app.route("/savecustomerdetails",methods = ["GET","POST"])
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:

            customer_id = request.form["customer_id"]
            customer_name = request.form["customer_name"]
            customer_email = request.form["customer_email"]
            customer_phone = request.form["customer_phone"]
            booking_date = request.form["booking_date"]


            con = sqlite3.connect('droame.db')
            cur = con.cursor()  
            cur.execute("INSERT into customer (customer_id, customer_name, customer_email, customer_phone, booking_date) VALUES (?,?,?,?,?)",(customer_id, customer_name, customer_email, customer_phone, booking_date))
            con.commit()  
            msg = "Customer Added Successfully."
            
        except:  
            con.rollback()  
            msg = "We can't add the Customer."
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()  

 
# View Customers Page
@app.route("/view")  
def view():  
    con = sqlite3.connect("droame.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from customer")
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  

# Updating Customer Records Page
@app.route("/updaterecord",methods = ["POST","GET"])  
def updaterecord():
     
    if request.method == "POST": 
        customer_id = request.form["customer_id"]
        customer_name = request.form["customer_name"]
        customer_email = request.form["customer_email"]
        customer_phone = request.form["customer_phone"]
        booking_date = request.form["booking_date"]



        con = sqlite3.connect("droame.db")
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("update customer set customer_name = ? where customer_id = ? ",(customer_name,customer_id))
            cur.execute("update customer set customer_email = ? where customer_id = ? ", (customer_email, customer_id))
            cur.execute("update customer set customer_phone = ? where customer_id = ? ", (customer_phone, customer_id))
            cur.execute("update customer set booking_date = ? where customer_id = ? ", (booking_date, customer_id))


            con.commit()   
            rows = cur.fetchall() 
            msg="Updated Successfully."

        except:  
            msg = "Can't update."
        finally:  
                return render_template("updateview.html",msg=msg)  

# Updating Booking Records Page backend working
@app.route("/updaterecord2",methods = ["POST","GET"])  
def updaterecord2():
     
    if request.method == "POST":
       booking_id = request.form["booking_id"]
       location_id = request.form["location_id"]
       drone_shot_id = request.form["drone_shot_id"]
       created_time = request.form["created_time"]
       customer_id = request.form["customer_id"]

    con = sqlite3.connect("droame.db")
    con.row_factory = sqlite3.Row
    try:  
            cur = con.cursor()  
            cur.execute("update bookings set location_id = ? where booking_id = ? ",(location_id,booking_id))
            cur.execute("update bookings set drone_shot_id = ? where booking_id = ? ", (drone_shot_id, booking_id))
            cur.execute("update bookings set created_time = ? where booking_id = ? ", (created_time, booking_id))
            cur.execute("update bookings set customer_id = ? where booking_id = ? ", (customer_id, booking_id))
            con.commit()   
            rows = cur.fetchall() 
            msg="Updated Successfully."

    except:  
            msg = "Can't update."
    finally:  
                return render_template("updateview2.html",msg=msg)
    

# Customer records delete page
@app.route("/delete")  
def delete():  
    return render_template("delete.html")  

# Backend working of deleting a customer from record
@app.route("/deleterecord",methods = ["POST","GET"])  
def deleterecord(): 
    if request.method == "POST": 
        customer_id = request.form["customer_id"]
        
        con = sqlite3.connect("droame.db")
        con.row_factory = sqlite3.Row
        try:  
            cur = con.cursor()  
            cur.execute("delete from customer where customer_id = ? ",(customer_id))
            rows = cur.fetchall()  

            con.commit() 
            msg = "Record successfully deleted."
        except:  
            msg = "Record can't be deleted."
        finally:  
            return render_template("delete_record.html",msg = msg)

# Update customer details page
@app.route("/update")  
def update():  
    return render_template("update.html") 

# Update booking details page
@app.route("/update2")  
def update2():  
    return render_template("update2.html") 



# Booking adding page
@app.route("/add2")  
def add2():  
    return render_template("add2.html")
  
# Backend working to store bookings
@app.route("/savebookingdetails",methods = ["GET","POST"])
def saveDeptDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:

            booking_id = request.form["booking_id"]
            location_id = request.form["location_id"]
            drone_shot_id = request.form["drone_shot_id"]
            created_time = request.form["created_time"]
            customer_id = request.form["customer_id"]

            con = sqlite3.connect('droame.db')
            cur = con.cursor()  
            cur.execute("INSERT into bookings (booking_id, location_id, drone_shot_id, created_time, customer_id) VALUES (?,?,?,?,?)",(booking_id, location_id, drone_shot_id, created_time, customer_id ))
            con.commit()  
            msg = "Booking Added Successfully."
            
        except:  
            con.rollback()  
            msg = "We can't add the booking."
        finally:  
            return render_template("success2.html",msg = msg)  
            con.close()  

# View Bookings Page
@app.route("/view2")  
def viewDept():  
    con = sqlite3.connect("droame.db")
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from bookings")
    rows = cur.fetchall()  
    return render_template("view2.html",rows = rows)  

# Booking records delete page
@app.route("/delete2")  
def deleteDept():  
    return render_template("delete2.html")  

# Backend working of deleting a booking from record
@app.route("/deletebookingsrecord",methods = ["POST","GET"])
def deletedeptrecord():

    if request.method == "POST":
        booking_id = request.form["booking_id"]

        con = sqlite3.connect("droame.db")
        con.row_factory = sqlite3.Row
        try:
            cur = con.cursor()
            cur.execute("delete from bookings where booking_id = ? ",(booking_id,))
            con.commit()
            msg = "Booking successfully deleted."
        except:
            msg = "Booking can't be deleted."
        finally:
            return render_template("delete_record2.html",msg = msg)

if __name__ == "__main__":  
    app.run(debug=True)  