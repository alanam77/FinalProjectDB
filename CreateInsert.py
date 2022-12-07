import sqlite3
con = sqlite3.connect('FinalProject.db')
cur = con.cursor()
statement = '''CREATE TABLE '''