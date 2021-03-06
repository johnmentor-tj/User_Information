from flask import Flask,render_template,request,redirect, url_for, session

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('register.html')

@app.route('/confirm',methods = ['GET','POST'])
def confirmation():

    if request.method == 'POST':
        n = request.form.get('name')
        a = request.form.get('age')
        s = request.form.get('salary')

    return render_template('confirm.html',name=n, age=a, salary=s)

#Step - 1 Main Program
if __name__ == '__main__':
    app.run(debug=True)
