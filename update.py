import argparse
import sqlite3
con = sqlite3.connect('FinalProject.db')
cur = con.cursor()

parser = argparse.ArgumentParser()
parser.add_argument('--add', action = 'store_true', default=False, help ='adding operation')
parser.add_argument('--delete', action = 'store_true', default=False,help='deleting operation')
parser.add_argument('--table',type=str,default='Albums',help='the target table in the database')
parser.add_argument('--record',type=str,default='',help='the target table in the database')

args = parser.parse_args()
str = args.record
arr = str.split(',')

if args.table == 'Musicians':
    if args.add:
        cur.execute('''INSERT INTO Musicians VALUES(?,?,?,?,?)''',(arr[0],arr[1],arr[2],arr[3],arr[4]))
    elif args.delete:
        cur.execute('''DELETE FROM Musicians WHERE(num = ? AND street = ? AND str_type = ? AND name = ? AND ssn = ?)''', (arr[0],arr[1],arr[2],arr[3],arr[4]))
if args.table == 'Performs':
    if args.add:
        cur.execute('''INSERT INTO Performs VALUES(?,?)''', (arr[0],arr[1]))
    elif args.delete:
        cur.execute('''DELETE FROM Performs WHERE (ssn = ? AND album_id = ?)''',(arr[0],arr[1]))
if args.table == 'Albums':
    if args.add:
        cur.execute('''INSERT INTO Albums VALUES(?,?,?,?)''', (arr[0],arr[1],arr[2],arr[3]))
    elif args.delete:
        cur.execute('''DELETE FROM Albums WHERE(name = ? AND album_id = ? AND date = ? AND type = ?)''',(arr[0],arr[1],arr[2],arr[3]))
if args.table == 'Used':
    if args.add:
        cur.execute('''INSERT INTO Used VALUES(?,?)''', (arr[0],arr[1]))
    elif args.delete:
        cur.execute('''DELETE FROM Used WHERE (album_id = ? AND instrument_id = ?)''',(arr[0],arr[1]))
if args.table == 'Instruments':
    if args.add:
        cur.execute('''INSERT INTO Instruments VALUES(?,?,?)''',(arr[0],arr[1],arr[2]))
    elif args.delete:
        cur.execute('''DELETE FROM Instruments WHERE(instrument_id = ? AND type = ? AND key = ?)''',(arr[0],arr[1],arr[2]))
con.commit()

