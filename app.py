from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# List Data structure to store student names
student_name_list = ["Spongebob", "Jimmy Neutron", "Alice"]

# Route for student list page
@app.route('/student')
def student_list():
    students_with_index = list(enumerate(student_name_list))
    return render_template('student-list.html', students=students_with_index)

# Route to add new student
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    if name:
        student_name_list.append(name)
    return redirect(url_for('student_list'))

# Route to delete student
@app.route('/delete/<int:index>')
def delete_student(index):
    if 0 <= index < len(student_name_list):
        student_name_list.pop(index)
    return redirect(url_for('student_list'))

# Route to edit student's name
@app.route('/edit/<int:index>', methods=['POST'])
def edit_student(index):
    new_name = request.form.get('new_name')
    if new_name and 0 <= index < len(student_name_list):
        student_name_list[index] = new_name
    return redirect(url_for('student_list'))

if __name__ == '__main__':
    app.run(debug=True)
