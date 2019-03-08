import sqlite3
con=sqlite3.connect('see.db')


c=con.cursor()

c.execute("DROP TABLE SEETABLE")
c.execute("DROP TABLE DOTABLE")
c.execute("DROP TABLE LISTTABLE")
c.execute("DROP TABLE NOFORMATSEE")
c.execute("DROP TABLE NOFORMATDO")
