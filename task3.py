import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Admin@1234",
  database = "task3"
)

mycursor = mydb.cursor()

def db_commit():
  mydb.commit()

def insert(data_student):
  add_student = ("INSERT INTO student "
               "(first_name, last_name, age, grade)"
               "VALUES (%s, %s, %s, %s)")
  mycursor.execute(add_student,data_student)
  db_commit()

data_student = ('Alice', 'Smith',18,95.5)
insert(data_student)


def update(dict_change,dict_condition):
  change_schema = list(dict_change.keys())[0]
  change_value = list(dict_change.values())[0]
  condition_schema = list(dict_condition.keys())[0]
  condition_value = list(dict_condition.values())[0]

  mycursor.execute(f"UPDATE student SET {change_schema} = {change_value} WHERE {condition_schema} = '{condition_value}'")
  db_commit()

dict_change = {'grade':97,'first_name':'Alice'}
dict_condition = {'first_name':'Alice'}
update(dict_change,dict_condition)


def delete(condition):

  key = list(condition.keys())[0]
  value = list(condition.values())[0]
  mycursor.execute(f"DELETE FROM student WHERE {key} = '{value}'")
  db_commit()

condition = {'last_name':'Smith'}
delete(condition)

def all_student():
  mycursor.execute("SELECT * FROM student")
  return mycursor.fetchall()

myresult = all_student()

mydb.close()

for x in myresult:
    print(x)







