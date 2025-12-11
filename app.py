import random
from flask import Flask, render_template, request, redirect,url_for, session
from flaskext.mysql import MySQL
from datetime import date, datetime

app = Flask(__name__)

app.secret_key = "12345ABCDE"

mysql=MySQL()
#config mysql with flask
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='car_rental_db'
app.config['MYSQL_DATABASE_HOST']='localhost'


mysql.init_app(app)


@app.route('/') #homepage 
def Index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) #Cutstomer Login page
def Login():
    error=None

    if request.method=="POST":
        email=request.form['email']
        password=request.form['password']
        
        con=mysql.connect()
        cur=con.cursor()
        
        cur.execute("SELECT * FROM customer WHERE Email = %s AND Password = %s", (email, password))   

        data=cur.fetchone()
        cur.close()
        con.close()

        if data:
            session['Clogged_in'] = True
            session['customerID']= data[0]
            session['firstName']= data[1]
            session['lastName']= data[2]
            session['dob']= data[3]
            session['phone']= data[4]
            session['email']= data[5]
            session['password']= data[6]
            session['address']= data[7]
            session['city']= data[8]
            session['state']= data[9]
            session['zipcode']= data[10]

            return redirect(url_for('Dashboard'))
        else:
            error = "Invalid Email or Password. Please try again or Register."
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@app.route('/payment', methods=['GET', 'POST']) #payment page
def Payment():
    method=None
    show=False
    if request.method == "POST":
        if 'action' in request.form:
            if request.form['action'] == 'back':
                method = None
            elif request.form['action'] == 'pay':
                con=mysql.connect()
                cur=con.cursor()
                method = request.form.get(method)
                Rental_ID = request.form.get('rentalID')
                Amount = request.form.get('amount')
                PDate = date.today()
            
                cur.execute("INSERT INTO payment(PDate, Amount, Method, Rental_ID) VALUES (%s, %s, %s, %s)", (PDate, Amount, method, Rental_ID))
                con.commit()

                cur.close()
                con.close()
                show=True
                return render_template('payment.html', show=show)
        elif 'method' in request.form:
            method = request.form['method']
    return render_template('payment.html', method=method)

@app.route('/adminLogin', methods=['GET', 'POST'])
def AdminLogin():
    error=None
    if request.method=="POST":
        employeeID=request.form['employeeID']
        password=request.form['password']

        con=mysql.connect()
        cur=con.cursor()

        cur.execute("SELECT * FROM staff_member WHERE EmployeeID = %s AND Password = %s", (employeeID, password))

        data=cur.fetchone()
        cur.close()
        con.close()

        if data:
            session['Alogged_in'] = True
            session['employeeID']= data[0]
            session['firstName']= data[1]
            session['lastName']= data[2]
            session['role']= data[3]             
            session['Salary']= data[4]
            session['BranchID']= data[5] 
            session['password']= data[6] 
              
            return redirect(url_for('AdminDashboard'))
        else:
            error = "Invalid Email or Password For Admin"
            return render_template('adminLogin.html', error=error)

    return render_template('adminLogin.html')

@app.route('/register', methods=['GET', 'POST'])
def Register():
    if request.method=='POST':
        customerID=request.form['customerID']
        firstName=request.form['firstName']
        lastName=request.form['lastName']
        phoneNum=request.form['phoneNum']
        dob=request.form['DOB']
        address=request.form['address']
        state=request.form['state']
        city=request.form['city']
        zipcode=request.form['zipcode']
        email=request.form['email']
        password=request.form['password']
        
        con=mysql.connect()
        cur=con.cursor()
    
        cur.execute("INSERT INTO customer(CustomerID, C_FName, C_LName, DateOfBirth, Phone, Email, Password, Street_Address, City, State, Zip_Code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (customerID, firstName, lastName, dob, phoneNum, email, password, address, city, state, zipcode))
        con.commit()

        cur.close()
        con.close()
        return redirect(url_for('Index'))
    
    else: 
        return render_template('register.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def Dashboard():

    show = False    
    if 'Clogged_in' in session:
        customer_id = session['customerID']
        
        con = mysql.connect()
        cur = con.cursor()

        cur.execute("SELECT * FROM CUSTOMER WHERE CustomerID = %s", (customer_id,))
        user_data = cur.fetchone()

        cur.execute("SELECT RENTAL_AGREEMENT.Rental_ID, RENTAL_AGREEMENT.Start_Date, RENTAL_AGREEMENT.End_Date, RENTAL_AGREEMENT.TotalCost, CAR.Brand, CAR.Model, CAR.LicensePlateNumber FROM RENTAL_AGREEMENT JOIN CAR ON RENTAL_AGREEMENT.CarID = CAR.CarID WHERE RENTAL_AGREEMENT.CustomerID = %s", (customer_id,))
        rental_data= cur.fetchall()

        cur.close()
        con.close()

        my_rentals = []
        for row in rental_data:
            rental = {
                'id': row[0],
                'start': row[1],
                'end': row[2],
                'cost': row[3],
                'car_name': f"{row[4]} {row[5]}", 
                'plate': row[6]
            }
            my_rentals.append(rental)
            
        user_profile = {
            'firstName': user_data[1],
            'lastName': user_data[2],
            'email': user_data[5],
            'phone': user_data[4],
            'address': f"{user_data[7]}, {user_data[8]}, {user_data[9]}"
        }

        return render_template('dashboard.html', profile=user_profile, rentals=my_rentals)

        return render_template('dashboard.html')
    else:
        return redirect(url_for('Login'))



@app.route('/adminDashboard', methods=['GET', 'POST'])
def AdminDashboard():
    if 'Alogged_in' in session:
        return render_template('adminDashboard.html')
    else:
        return redirect(url_for('AdminLogin'))

@app.route('/admin/users')
def AdminUsers():
    role = session.get('role')

    if 'Alogged_in' in session and role and role.lower() == 'admin':        
        con = mysql.connect()
        cur = con.cursor()
        
        cur.execute("SELECT * FROM `customer`")
        data = cur.fetchall() 
        
        cur.close()
        con.close()
        

        users_list = []
        for row in data:
            user_dict = {
                'customerID': row[0],
                'firstName': row[1],
                'lastName': row[2],
                'dob': row[3],
                'phoneNum': row[4],
                'email': row[5],
                'password': row[6],
                'address': row[7],
                'city': row[8],
                'state': row[9],
                'zipcode': row[10]
                }
            
            users_list.append(user_dict)

        return render_template('adminUsers.html', users=users_list)
    else:
        return redirect(url_for('AdminLogin'))

@app.route('/logout')
def Logout():
    session.clear()
    
    return redirect(url_for('Index'))

@app.route('/cars')
def AvailableCars():
    if 'Clogged_in' in session:
        
        con = mysql.connect()
        cur = con.cursor()
        
        cur.execute("SELECT * FROM car WHERE RentalStatus = 'available'")
        data = cur.fetchall()
        cur.close()
        con.close()
        
        cars_list = []
        for row in data:
            car_dict = {
                'carID': row[0],
                'plate': row[1],
                'model': row[2],
                'brand': row[3],
                'category': row[4],
                'year': row[5],
                'status': row[6],
            }

            cars_list.append(car_dict)
            
        return render_template('cars.html', cars=cars_list)
    else:
        return redirect(url_for('Login'))
    


@app.route('/rent/<int:car_id>', methods=['GET', 'POST'])
def RentCar(car_id):
    if 'Clogged_in' in session:
        con = mysql.connect()
        cur = con.cursor()

        cur.execute("SELECT * FROM CAR WHERE CarID = %s", (car_id,))
        car_data = cur.fetchone()
        
        car_obj = {
            'carID': car_data[0],
            'plate': car_data[1],
            'model': car_data[2],
            'brand': car_data[3],
            'category': car_data[4]
        }
        
        daily_rate = 60

        if request.method == 'POST':
            startDay_String = request.form['startDate']
            endDay_String = request.form['endDate']
            customer_id = session['customerID']

            
            d1 = datetime.strptime(startDay_String, "%Y-%m-%d")
            d2 = datetime.strptime(endDay_String, "%Y-%m-%d")
            delta = d2 - d1
            days = delta.days
            
            if days <= 0:
                error = "End date must be after start date!"
                return render_template('rentCar.html',car=car_obj, rate=daily_rate, error=error)           
             
            daily_rate=100
            total_cost = days * daily_rate

            cur.execute("INSERT INTO RENTAL_AGREEMENT(Start_Date, End_Date, DailyRate, TotalCost, CustomerID, CarID) VALUES (%s, %s, %s, %s, %s, %s)", (startDay_String, endDay_String, daily_rate, total_cost, customer_id, car_id))
            
            cur.execute("UPDATE CAR SET RentalStatus = 'rented' WHERE CarID = %s", (car_id,))
            con.commit()
                
            cur.close()
            con.close()
            
            return redirect(url_for('Dashboard'))
        
        cur.close()
        con.close()
        return render_template('rentCar.html', car=car_obj, rate=daily_rate)
    
    else:
        return redirect(url_for('Login'))
    
if __name__ == "__main__":
    app.run(debug=True) #runs server in debug mode

