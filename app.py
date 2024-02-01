# Import necessary modules from the Flask framework
import flask
from flask import Flask , render_template
from json_demo import ProgrammingLanguageManager
from course_manager import get_courses, render_courses_template, search_courses



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
  
   # Pass data to the template and render it
   return render_template('python.html')

# Define a route for the "/javascript" page
@app.route("/javascript")
def java_script():
    return render_template('javascript.html')

# Define a route for the "/result" page
@app.route("/result")
def result():
      # Create an instance of ProgrammingLanguageManager
   manager = ProgrammingLanguageManager('data/programming_language.json')

# Load the data from the JSON file
   programming_languages =manager.load_data()

# Remove the 'paradigms' key from each language
#    manager.remove_paradigms()

# Save the modified data to a new JSON file
   manager.save_data('data/new_programming_language.json')
   return render_template('result.html',programming_languages=programming_languages)


@app.route("/remove")
def remove():
      # Create an instance of ProgrammingLanguageManager
   manager = ProgrammingLanguageManager('data/programming_language.json')

# Load the data from the JSON file
   programming_languages =manager.load_data()

# Remove the 'paradigms' key from each language
   manager.remove_paradigms()

# Save the modified data to a new JSON file
   manager.save_data('data/new_programming_language.json')
   return render_template('remove.html',programming_languages=programming_languages)



# Home page get the courses name 
# get courses name function from courses.txt
@app.route("/courses")
def course():
    return render_courses_template()

# create a search for courses page
@app.route("/search")
def search():
    query = flask.request.args.get("q")
    result = search_courses(query)
    return result

@app.route("/todo")
def todo():
    return render_template('todo.html')




# Run the Flask web application in debug mode
if __name__ == '__main__':
    app.run(debug=True)