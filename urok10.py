import sqlite3

conn = sqlite3.connect("v2222.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    teacher_id INTEGER
);
''')

#cursor.execute("delete from students;")
#cursor.execute("delete from courses;")
#cursor.execute("insert into students (name, age) VALUES ('George', 14);")
#cursor.execute("insert into students (name, age) VALUES ('Maria', 11);")
#cursor.execute("insert into students (name, age) VALUES ('Sofia', 15);")

#cursor.execute("insert into courses (course_name, teacher_id) VALUES ('Math', 1);")
#cursor.execute("insert into courses (course_name, teacher_id) VALUES ('Python', 2);")

cursor.execute("select name from students where age > 12")
students = cursor.fetchall()
for s in students:
    print(s[0])

cursor.execute("select name from students;")
students = cursor.fetchall()
cursor.execute("select course_name from courses;")
courses = cursor.fetchall()

print(students)
print(courses)
conn.commit()
conn.close()