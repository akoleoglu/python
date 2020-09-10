from flask import Flask,redirect,url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'This is home page for "/" path. <html><h1>Welcome to Ahmet\'s website.</h1></html>'

@app.route('/about')
def about():
    return '<html><h1> This is my about page... </h1></html>'


@app.route('/error')
def error():
    return '<html><h1> ### Got lost? ### </h1></html>'

@app.route('/hello')
def hello():
    return '<html><h1> Hello from Ahmet </h1></html>'

@app.route('/admin' , methods = ['GET'])
def admin():
    authorized=False
    if authorized:
        return 'This is the admin page... You can see this page'
    else:
        return redirect(url_for('error'))

# @app.route('/<name>')
# def greet(name):
#     greet_format = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Greeting Page</title>
#     </head>
#     <body>
#         <h1>Hello, { name }!</h1>
#         <h1>Welcome to my Greeting Page</h1>
#     </body>
#     </html>
#     """
#     return greet_format

@app.route('/greet-admin')
def greet_admin():
    return redirect(url_for('greet', name='Master Admin !!!'))


@app.route('/<name>')
def greet(name):
    return render_template('greet.html', person = name)


@app.route('/list10')
def list10():
    return render_template('list10.html')


@app.route('/evens')
def evens():
    return render_template('evens.html')



if __name__ == '__main__':
    app.run(host='localhost',port=5000, debug=True)

    