

import csv
import sqlite3

# create a connection to the database
conn = sqlite3.connect('books.db')

# create a cursor object to execute SQL commands
cursor = conn.cursor()

# create the books table
cursor.execute('CREATE TABLE books (title TEXT, author TEXT, year INTEGER)')

# commit the changes and close the connection
conn.commit()
conn.close()

# create a connection to the database
conn = sqlite3.connect('books.db')

# create a cursor object to execute SQL commands
cursor = conn.cursor()

# read the CSV file and insert its data into the books table
with open('books2.csv') as f:
    reader = csv.reader(f)
    next(reader) # skip the header row
    for row in reader:
        cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', row)

# commit the changes and close the connection


# create a connection to the database
conn = sqlite3.connect('books.db')

# create a cursor object to execute SQL commands
cursor = conn.cursor()

# select the title column from the books table in alphabetical order
cursor.execute('SELECT title FROM books ORDER BY title ASC')
rows = cursor.fetchall()

# print the titles
for row in rows:
    print(row[0])

# close the connection
conn.close()

# create a connection to the database
conn = sqlite3.connect('books.db')

# create a cursor object to execute SQL commands
cursor = conn.cursor()

# select all columns from the books table in order of publication
cursor.execute('SELECT * FROM books ORDER BY year ASC')
rows = cursor.fetchall()

# print the rows
for row in rows:
    print(row)

# close the connection
conn.close()
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# create an engine to connect to the database
engine = create_engine('sqlite:///books.db', echo=True)

# define a metadata object
metadata = MetaData()

# define the books table
books = Table('books', metadata,
    Column('title', String),
    Column('author', String),
    Column('year', Integer)
)

# create the books table if it doesn't exist
metadata.create_all(engine)

# select the title column from the books table in alphabetical order
with engine.connect() as conn:
    result = conn.execute(books.select().order_by(books.c.title))
    for row in result:
        print(row.title)
