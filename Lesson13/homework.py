import sqlite3

with sqlite3.connect('homework.db') as sq:
    cur = sq.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS students(
                id PRIMARY KEY,
                name VARCHAR(20) NOT NULL,
                age INTEGER NOT NULL);
                """)

    cur.execute("""INSERT INTO students(name, age)
    VALUES
    ('Ann', 25),
    ('Kate', 29);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS audience(
                id PRIMARY KEY,
                number INTEGER NOT NULL,
                exam REFERENCES students (name)
                ON DELETE CASCADE ON UPDATE NO ACTION);
                """)

    cur.execute("""INSERT INTO audience(number)
        VALUES
        (309),
        (111);""")