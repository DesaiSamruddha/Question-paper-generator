import sqlite3
def create_db():
    con= sqlite3.connect(database=r'ims.db')
    cur=con.cursor()



    cur.execute("CREATE TABLE IF NOT EXISTS Manas(sid INTEGER PRIMARY KEY,name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Samruddha(qid INTEGER PRIMARY KEY,name text,sub text,mark text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Login2(fname text,lname text,contact number,eid varchar(20),pass varchar(20))")
    con.commit()


create_db()