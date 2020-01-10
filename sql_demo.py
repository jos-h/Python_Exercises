import sqlite3
from pprint import pprint

conn = sqlite3.connect("example.db")
c = conn.cursor()

drop_table = "DROP TABLE DUMMY"
c.execute(drop_table)

create_query = """CREATE TABLE DUMMY (id int, parent int, child int, value int)"""
c.execute(create_query)

insert_query = [('2', '0', '100', '3'), ('2', '100', '101', '10'), ('2', '100', '102', '11'),
                ('2', '100', '103', '12'), ('2', '0', '100', '3'), ('2', '102', '104', '21'),
                ('2', '103', '105', '22'), ('2', '0', '200', '22'), ('2', '200', '201', '23'),
                ('2', '201', '205', '31'), ('2', '201', '206', '32'), ('2', '0', '300', '30')]

c.executemany('INSERT INTO DUMMY VALUES (?,?,?,?)', insert_query)

data = c.execute("SELECT * FROM DUMMY where id=2")
ll = list(data)
pprint(ll)
conn.commit()
conn.close()

