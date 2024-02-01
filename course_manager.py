# course_manager.py

def get_courses():
    coursesdb = open("courses.txt")
    content = coursesdb.read()
    coursesdb.close()
    courses = content.split("\n")
    return courses

def render_courses_template():
    html_file = open("templates/courses.html")
    content = html_file.read()
    html_file.close()
    courses = get_courses()
    actual_values = ""
    for course in courses:
        actual_values += "<p>" + course + "</p>"
    return content.replace("$$COURSES$$", actual_values)

def search_courses(query):
    html_file = open("templates/courses.html")
    content = html_file.read()
    html_file.close()
    courses = get_courses()
    result = ""
    for course in courses:
        if course.lower().find(query.lower()) != -1:
            result += "<p>" + course + "</p>"
    if result == "":
        result = "<p> No result found </p>"
    return content.replace("$$COURSES$$", result)
