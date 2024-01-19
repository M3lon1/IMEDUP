import sqlite3

def add_values_to_database(Hash, File_path):
    c.execute("INSERT INTO Test VALUES (:Hash, :File_path)", {'Hash': Hash, 'File_path': File_path})
    conn.commit()

DB_file = "D:\CS4DM Bauhaus Weimar\Octobr 2023\IMDEDU Project\Test.db"
conn = sqlite3.connect(DB_file)
c = conn.cursor()
try:
    c.execute("""CREATE TABLE test (
              Hash text,
              Path text
    )""")
    print("Data base with name Test.db has been created.")
except:
    print("Data base with name Test.db already exists.")

add_values_to_database("000112", "blabla")
c.execute(" SELECT * FROM Test")
print(c.fetchall())