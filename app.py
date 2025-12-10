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

@app.route('/login') #Cutstomer Login page
def Login():
    return render_template('login.html')

@app.route('/adminLogin')
def AdminLogin():
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