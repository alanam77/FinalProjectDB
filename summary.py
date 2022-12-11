import sqlite3
con = sqlite3.connect('FinalProject.db')
cur = con.cursor()
print("\n")
print("1. Total Number of Musicians and List of Musicians\n")
statement = '''SELECT COUNT(*) AS Total_Musicians FROM Musicians'''
res = cur.execute(statement)

print('--------------------')
n = [x[0] for x in res.description]
print(n)
print('--------------------')
for row in res : print(row)

statement = '''
            SELECT * FROM Musicians
            '''

res = cur.execute(statement)

print('--------------------')
n = [x[0] for x in res.description]
print(n)
print('--------------------')
for row in res : print(row)
print("\n")
print("2. Total Number of Albums and List of Albums\n")
statement = '''SELECT COUNT(*) AS Total_Albums FROM Albums'''
res = cur.execute(statement)

print('--------------------')
n = [x[0] for x in res.description]
print(n)
print('--------------------')
for row in res : print(row)

statement = '''
            SELECT * FROM Albums
            '''

res = cur.execute(statement)

print('--------------------')
n = [x[0] for x in res.description]
print(n)
print('--------------------')
for row in res : print(row)
print("\n")
print("3. Total Number of Instruments and List of Instruments\n")
statement = '''SELECT COUNT(*) AS Total_Instruments FROM Instruments'''
res = cur.execute(statement)

print('--------------------')
n = [x[0] for x in res.description]
print(n)
print('--------------------')
for row in res : print(row)

statement = '''
            SELECT * FROM Instruments
            '''

res = cur.execute(statement)

print('--------------------')
n = [x[0] for x in res.description]
print(n)
print('--------------------')
for row in res : print(row)
print("\n")
print("4. Names of Musicians and Number of Albums written by them\n")
statement = '''SELECT Musicians.name, COUNT(Performs.album_id) FROM Musicians NATURAL JOIN Performs GROUP BY Musicians.name'''
res = cur.execute(statement)

print('--------------------')
n = [x[0] for x in res.description]
print(n)
print('--------------------')
for row in res : print(row)
