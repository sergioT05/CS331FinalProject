from flask import Flask, render_template, request, redirect,url_for
from flaskext.mysql import MySQL

app = Flask(__name__)

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
        
        cur.execute("SELECT * FROM `customer` WHERE `Email` = %s AND `Password` = %s", (email, password))   

        data=cur.fetchone()
        cur.close()
        con.close()

        if data:
            user_info = {
                'customerID': data[0],
                'firstName': data[1],
                'lastName': data[2],
                'dob': data[3],
                'phone': data[4],
                'email': data[5],
                'password': data[6],
                'address': data[7],
                'city': data[8],
                'state': data[9],
                'zipcode': data[10],
                }
            return render_template('dashboard.html', user=user_info)
        else:
            error = "Invalid Email or Password. Please try again or Register."
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/adminLogin', methods=['GET', 'POST'])
def AdminLogin():
    error=None
    if request.method=="POST":
        employeeID=request.form['employeeID']
        password=request.form['password']

        con=mysql.connect()
        cur=con.cursor()

        cur.execute("SELECT * FROM `staff_member` WHERE `EmployeeID` = %s AND `Password` = %s", (employeeID, password))

        data=cur.fetchone()
        cur.close()
        con.close()

        if data:
            staff_info = {
                'employeeID': data[0],
                'firstName': data[1],
                'lastName': data[2],
                'role': data[3],
                'Salary': data[4],
                'BranchID': data[5], 
                'password': data[6] 
                }            
            return render_template('adminDashboard.html', staff=staff_info)
        else:
            error = "Invalid Email or Password. Please try again or Register."
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
    
        cur.execute("INSERT INTO `customer`(`CustomerID`, `C_FName`, `C_LName`, `DateOfBirth`, `Phone`, `Email`, `Password`, `Street_Address`, `City`, `State`, `Zip_Code`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (customerID, firstName, lastName, dob, phoneNum, email, password, address, city, state, zipcode))
        con.commit()

        cur.close()
        con.close()
        return redirect(url_for('Index'))
    
    else: 
        return render_template('register.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def Dashboard():
    return render_template('dashboard.html')

@app.route('/adminDashboard', methods=['GET', 'POST'])
def AdminDashboard():
    return render_template('adminDashboard.html')

if __name__ == "__main__":
    app.run(debug=True) #runs server in debug mods