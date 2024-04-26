
listOfTablesNames = ["StaffCalendar","Salesperson","MechanicInfo","Vehicles","InvoiceHistory","CustomerInfo","Services_and_Inventory","ServiceSchedule"] # So here im making a list of all the names of the tables
def printList(list = []):
    x = int(0)
    print("List Of The Table Names: ")
    for data in list:
        print(f"{x+1}. {data}")
        x += 1
def printQueries(list = []):
    x = int(0)
    print("\nList of Example Queries For The Entered Table")
    for data in list:
        print(f"{x+1}. {data}")
        x += 1 



# making my liust 
sql_queries_CustomerInfo = [
    "SELECT * FROM CustomerInfo;",
    "SELECT * FROM CustomerInfo WHERE cust_id = customer_id;",
    "SELECT * FROM CustomerInfo WHERE cust_fname = 'first_name';",
    "SELECT * FROM CustomerInfo WHERE cust_lname = 'last_name';",
    "SELECT * FROM CustomerInfo WHERE cust_phonenumber = phone_number;",
    "SELECT * FROM CustomerInfo WHERE cust_address = 'address';",
    "SELECT * FROM CustomerInfo WHERE dob > 'date';",
    "SELECT * FROM CustomerInfo WHERE dob < 'date';",
    "SELECT DISTINCT cust_id FROM CustomerInfo;",
    "SELECT COUNT(*) FROM CustomerInfo;"]
sql_queries_Services_Inventory = [ 
    "SELECT * FROM Services_and_Inventory;",
    "SELECT * FROM Services_and_Inventory WHERE services = 'service_name';",
    "SELECT * FROM Services_and_Inventory WHERE parts_amount > value;",
    "SELECT * FROM Services_and_Inventory WHERE parts LIKE '%keyword%';",
    "SELECT DISTINCT services FROM Services_and_Inventory;",
    "SELECT COUNT(*) FROM Services_and_Inventory;",
    "SELECT SUM(parts_amount) FROM Services_and_Inventory;",
    "SELECT AVG(parts_amount) FROM Services_and_Inventory;",
    "SELECT MAX(parts_amount) FROM Services_and_Inventory;",
    "SELECT MIN(parts_amount) FROM Services_and_Inventory;"]
sql_queries_vehicles = [
    "SELECT * FROM Vehicles;",
    "SELECT * FROM Vehicles WHERE vin_number = 'vin_number';",
    "SELECT * FROM Vehicles WHERE car_price = price;",
    "SELECT * FROM Vehicles WHERE vehicle_make = 'make';",
    "SELECT * FROM Vehicles WHERE vehicle_model = 'model';",
    "SELECT * FROM Vehicles WHERE vehicle_year = year;",
    "SELECT * FROM Vehicles WHERE car_price < value;",
    "SELECT * FROM Vehicles WHERE car_price > value;",
    "SELECT DISTINCT vin_number FROM Vehicles;",
    "SELECT COUNT(*) FROM Vehicles;"]
sql_queries_invoiceHistory = [
    "SELECT * FROM InvoiceHistory;",
    "SELECT * FROM InvoiceHistory WHERE invoice_id = 'invoice_id';",
    "SELECT * FROM InvoiceHistory WHERE invoice_price = price;",
    "SELECT * FROM InvoiceHistory WHERE service_date = 'YYYYMMDD';",
    "SELECT * FROM InvoiceHistory WHERE service_date < 'YYYYMMDD';",
    "SELECT * FROM InvoiceHistory WHERE service_date > 'YYYYMMDD';",
    "SELECT * FROM InvoiceHistory WHERE invoice_price < value;",
    "SELECT * FROM InvoiceHistory WHERE invoice_price > value;",
    "SELECT DISTINCT invoice_id FROM InvoiceHistory;",
    "SELECT COUNT(*) FROM InvoiceHistory;"]
sql_queries_ServiceSchedule = [
    "SELECT * FROM ServiceSchedule;",
    "SELECT * FROM ServiceSchedule WHERE service_date = 'service_date';",
    "SELECT * FROM ServiceSchedule WHERE services = 'service_name';",
    "SELECT * FROM ServiceSchedule WHERE parts = 'part_name';",
    "SELECT * FROM ServiceSchedule WHERE service_date < 'YYYYMMDD';",
    "SELECT * FROM ServiceSchedule WHERE service_date > 'YYYYMMDD';",
    "SELECT DISTINCT service_date FROM ServiceSchedule;",
    "SELECT COUNT(*) FROM ServiceSchedule;"]
sql_queries_MechanicInfo = [
    "SELECT * FROM MechanicInfo;",
    "SELECT * FROM MechanicInfo WHERE mechanic_id = 'mechanic_id';",
    "SELECT * FROM MechanicInfo WHERE mech_fname = 'first_name';",
    "SELECT * FROM MechanicInfo WHERE mech_lname = 'last_name';",
    "SELECT * FROM MechanicInfo WHERE date_worked < 'YYYYMMDD';",
    "SELECT * FROM MechanicInfo WHERE date_worked > 'YYYYMMDD';",
    "SELECT DISTINCT mechanic_id FROM MechanicInfo;",
    "SELECT COUNT(*) FROM MechanicInfo;"]
sql_queries_StaffCalendar = [
    "SELECT * FROM StaffCalendar;",
    "SELECT * FROM StaffCalendar WHERE date_worked = 'YYYYMMDD';",
    "SELECT * FROM StaffCalendar WHERE signin_time > 'HHMM';",
    "SELECT * FROM StaffCalendar WHERE signin_time < 'HHMM';",
    "SELECT * FROM StaffCalendar WHERE signout_time > 'HHMM';",
    "SELECT * FROM StaffCalendar WHERE signout_time < 'HHMM';",
    "SELECT * FROM StaffCalendar WHERE mechanic_id = 'mechanic_id';",
    "SELECT * FROM StaffCalendar WHERE salesperson_id = 'salesperson_id';",
    "SELECT DISTINCT date_worked FROM StaffCalendar;",
    "SELECT COUNT(*) FROM StaffCalendar;"]


tableToShow = str(input("Enter in a name of a table from the list above: "))
if(tableToShow == 'Services_and_Inventory'):
    printQueries(sql_queries_Services_Inventory)

elif(tableToShow == "CustomerInfo"):
    printQueries(sql_queries_CustomerInfo)

elif(tableToShow == "InvoiceHistory"):
    printQueries(sql_queries_CustomerInfo)

elif(tableToShow == "Vehicles"):
    printQueries(sql_queries_vehicles)

elif(tableToShow == "StaffCalendar"):
    printQueries(sql_queries_StaffCalendar)

elif(tableToShow == "MechanicInfo"):
    printQueries(sql_queries_MechanicInfo)

elif(tableToShow == "ServiceSchedule"):
    printQueries(sql_queries_ServiceSchedule)

print()

from flask import Blueprint, render_template, request, redirect, url_for
import csv
import sqlite3
import pandas 
from tabulate import tabulate 
from flask import jsonify
views = Blueprint(__name__, "views")
# Define a function to fetch data from the database
'''
SO WHAT I NEED TO IS MAKE A FUNCTION FOR EACH TABLE THAT PRINTS it table BASED OF ITS QUERY: 
'''


def fetch_customer_info():
    connection = sqlite3.connect('/Users/machew/PycharmProjects/firstpythoncode/pythonProject/pandas-cookbook-master/sqlite (2).db')
    query = "SELECT * FROM CustomerInfo"
    data_frame = pandas.read_sql(query, connection)
    connection.close()
    return data_frame


@views.route("/fetch_customer_info", methods=["GET"])
def fetch_customer_info_route():
    customer_data = fetch_customer_info()
    if customer_data is not None:
        customer_list = customer_data.to_dict(orient="records")
        return jsonify(customer_list)
    
def fetch_vehicle_data():
    # Establish connection to the database
    connection = sqlite3.connect('/Users/machew/PycharmProjects/firstpythoncode/pythonProject/pandas-cookbook-master/sqlite (2).db')
    # Read data from the database into a pandas DataFrame

    dataframe_example = pandas.read_sql("SELECT * from Vehicles", connection)
    # Close the connection
    connection.close()
    # Return the DataFrame
    return dataframe_example

@views.route("/fetch_vehicle_data", methods=["GET"])
def fetch_vehicle_data_route():
    # Call the function to fetch vehicle data from the database
    vehicle_data = fetch_vehicle_data()
    # Convert the DataFrame to a list of dictionaries (JSON format)
    vehicle_list = vehicle_data.to_dict(orient="records")
    # Return the vehicle data as JSON response
    return jsonify(vehicle_list)



@views.route("/")
def home():
    return render_template("index_work.html")

@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Handle form submission
        email = request.form.get("email")
        password = request.form.get("password")
        # Perform login authentication here
        # Password validation
        if email == "mattkilp5@gmail.com" and password == "matt":
            return "Login successful"  # Indicate successful login
        else:
            return "Invalid email or password"  # You can customize this response

    else:
        # Render login page for GET request
        return render_template("login.html")

