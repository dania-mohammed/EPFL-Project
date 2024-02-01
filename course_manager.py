# Function to retrieve courses from a file
def get_courses():
    coursesdb = open("courses.txt") 
    content = coursesdb.read()  
    coursesdb.close()  
    courses = content.split("\n")  # Split the content into a list of courses
    return courses

# Function to render the courses template
def render_courses_template():
    html_file = open("templates/courses.html") 
    content = html_file.read()  
    html_file.close()
    courses = get_courses()  
    actual_values = ""
    for course in courses:
        actual_values += "<p>" + course + "</p>"  # Generate HTML paragraphs for each course
    return content.replace("$$COURSES$$", actual_values)  # Replace the placeholder in the template with the actual course values

# Function to search for courses based on a query
def search_courses(query):
    html_file = open("templates/courses.html")  
    content = html_file.read()  
    html_file.close()  
    courses = get_courses() 
    result = ""
    for course in courses:
        if course.lower().find(query.lower()) != -1:  # Check if the query is found in the course name (case-insensitive)
            result += "<p>" + course + "</p>"  # Generate HTML paragraphs for the matching courses
    if result == "":
        result = "<p> No result found </p>"  # Display a message if no matching courses are found
    return content.replace("$$COURSES$$", result)  # Replace the placeholder in the template with the search result

