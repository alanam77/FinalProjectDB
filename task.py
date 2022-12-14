import sqlite3
import csv
con = sqlite3.connect('NotownRecords.db')
cur = con.cursor()
statement = '''
CREATE TABLE Musicians(num INTEGER NOT NULL, street CHAR(20) NOT NULL, str_type CHAR(10) NOT NULL, name CHAR(20) NOT NULL, ssn INTEGER NOT NULL, PRIMARY KEY (ssn));
'''
cur.execute(statement)
statement = '''CREATE TABLE Albums(name CHAR(20) NOT NULL, album_id INTEGER NOT NULL, date INTEGER NOT NULL, type CHAR(2) NOT NULL, PRIMARY KEY (album_id));'''
cur.execute(statement)
statement = '''CREATE TABLE Instruments(instrument_id INTEGER NOT NULL, type CHAR(20) NOT NULL, key CHAR(20) NOT NULL, PRIMARY KEY (instrument_id));'''
cur.execute(statement)
statement = '''
CREATE TABLE Performs(ssn INTEGER NOT NULL, album_id INTEGER NOT NULL, PRIMARY KEY(ssn,album_id), FOREIGN KEY (ssn) REFERENCES Musicians, FOREIGN KEY (album_id) REFERENCES Albums);'''
cur.execute(statement)
statement = '''CREATE TABLE Used(album_id INTEGER NOT NULL, instrument_id INTEGER NOT NULL, PRIMARY KEY(album_id, instrument_id), FOREIGN KEY(album_id) REFERENCES Albums, FOREIGN KEY(instrument_id) REFERENCES Instruments);'''
cur.execute(statement)

filecontent = csv.reader(open('album.csv'))
header = next(filecontent)
for row in filecontent:
    print(row)
    name = row[0]
    id = (int)(row[1])
    date = (int)(row[2])
    type = (row[3])
    cur.execute('''INSERT INTO Albums VALUES(?,?,?,?)''', (name, id, date, type))
con.commit()

filecontent = csv.reader(open('musician.csv'))
header = next(filecontent)
for row in filecontent:
    print(row)
    num = (int)(row[0])
    street = (row[1])
    type = (row[2])
    name = (row[3])
    ssn = (int)(row[4])
    cur.execute('''INSERT INTO Musicians VALUES(?,?,?,?,?)''', (num,street,type,name,ssn))
con.commit()

filecontent = csv.reader(open('instrument.csv'))
header = next(filecontent)
for row in filecontent:
    print(row)
    id = (int)(row[0])
    type = (row[1])
    key = (row[2])
    cur.execute('''INSERT INTO Instruments VALUES(?,?,?)''', (id,type,key))
con.commit()

filecontent = csv.reader(open('musician-album.csv'))
header = next(filecontent)
for row in filecontent:
    print(row)
    ssn = (int)(row[0])
    aid = (int)(row[1])
    cur.execute('''INSERT INTO Performs VALUES(?,?)''', (ssn,aid))
con.commit()

filecontent = csv.reader(open('album-instrument.csv'))
header = next(filecontent)
for row in filecontent:
    print(row)
    aid = (int)(row[0])
    iid = (int)(row[1])
    cur.execute('''INSERT INTO Used VALUES(?,?)''', (aid,iid))
con.commit()