# Import necessary modules from the Flask framework
from flask import Flask , render_template



# Create a Flask application instance
app = Flask(__name__)

# Define a route for the "/" page 
@app.route("/")
@app.route("/home")
def Home():
    return render_template('home.html')

# Define a route for the "/python" page 
@app.route("/python")
def python():
    return render_template('python.html')

# Define a route for the "/javascript" page
@app.route("/javascript")
def java_script():
    return render_template('javascript.html')



# Run the Flask web application in debug mode
if __name__ == '__main__':
    app.run(debug=True)