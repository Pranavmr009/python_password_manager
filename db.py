import sqlite3

conn = sqlite3.connect("/media/pranav/HDD-1/python projects/password_manager/data.db")
c = conn.cursor()

try:
    c.execute("""CREATE TABLE data(
                 service text,
                 password text
    )
    """)

except sqlite3.OperationalError:
    pass


def add_item(service, password):

    try:

        c.execute(f"INSERT INTO data VALUES (:service, :password)", {'service': service, 'password': password})
        print("Executed successfully")
        conn.commit()

    except:
        print("Failed to retrieve data")

def search(service):

    try:
        c.execute("SELECT * FROM data WHERE service=:service", {'service': service})
        conn.commit()
        return c.fetchone()[1]

    except:
        print("Failed to retrieve data")



def retrieve_all():

    try:
        c.execute("SELECT * FROM data")

    except:
        print("Failed to retrieve data")
    rows = c.fetchall()
    for row in rows:
        print(row[0])

