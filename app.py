from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #homepage 
def Index():
    return render_template('index.html')

@app.route('/login') #Login page
def Login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True) #runs server in debug mods