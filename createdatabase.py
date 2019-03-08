import sqlite3
con=sqlite3.connect('see.db')


c=con.cursor()

c.execute("""CREATE TABLE SEETABLE(
              PLACE TEXT,
              NAME TEXT,
              PRICE TEXT,
              HOURS TEXT,
              LONG TEXT,
              LAT TEXT,
              ADDRESS TEXT,
              ALT TEXT,
              DIRECTIONS TEXT,
              URL TEXT,
              EMAIL TEXT,
              PHONE TEXT,
              TOLLFREE TEXT,
              FAX TEXT)""")

c.execute("CREATE UNIQUE INDEX NODUP ON SEETABLE(PLACE, NAME)")

c.execute("""CREATE TABLE DOTABLE(
              PLACE TEXT,
              NAME TEXT,
              PRICE TEXT,
              HOURS TEXT,
              LONG TEXT,
              LAT TEXT,
              ADDRESS TEXT,
              ALT TEXT,
              DIRECTIONS TEXT,
              URL TEXT,
              EMAIL TEXT,
              PHONE TEXT,
              TOLLFREE TEXT,
              FAX TEXT)""")
c.execute("CREATE UNIQUE INDEX NODUP1 ON DOTABLE(PLACE, NAME)")

c.execute("""CREATE TABLE LISTTABLE(
              PLACE TEXT,
              NAME TEXT,
              PRICE TEXT,
              HOURS TEXT,
              LONG TEXT,
              LAT TEXT,
              ADDRESS TEXT,
              ALT TEXT,
              DIRECTIONS TEXT,
              URL TEXT,
              EMAIL TEXT,
              PHONE TEXT,
              TOLLFREE TEXT,
              FAX TEXT)""")

c.execute("CREATE UNIQUE INDEX NODUP2 ON LISTTABLE(PLACE, NAME)")

c.execute("""CREATE TABLE NOFORMATSEE(
              PLACE TEXT,
              NAME TEXT,
              DESCRIPTION TEXT)""")

c.execute("CREATE UNIQUE INDEX NODUP3 ON NOFORMATSEE(PLACE, NAME)")


c.execute("""CREATE TABLE NOFORMATDO(
              PLACE TEXT,
              NAME TEXT,
              DESCRIPTION TEXT)""")

c.execute("CREATE UNIQUE INDEX NODUP4 ON NOFORMATDO(PLACE, NAME)")
