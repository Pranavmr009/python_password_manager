import sqlite3


conn = sqlite3.connect("data.db")
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
    c.execute(f"INSERT INTO data VALUES (:service, :password)", {'service': service, 'password': password})
    print("Executed successfully")
    conn.commit()


def search(service):
    c.execute("SELECT * FROM data WHERE service=:service", {'service': service})
    conn.commit()
    return c.fetchone()[1]


