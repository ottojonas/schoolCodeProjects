import csv 
import sqlite3

with sqlite3.connect("hotels.db") as db: 
    myCursor = db.cursor() 


#with open('hotels.csv') as csvFile: 
#    csvReader = csv.reader(csvFile , delimiter = ',')
#    for row in csvReader: 
#        insert = 'insert into hotel(hotelNo, name, address) values(?, ?, ?)'
#        myCursor.execute(insert, [(row[0]), (row[1]), (row[2])])
#        db.commit()

#with open("rooms.csv") as csvFile: 
#    csvReader = csv.reader(csvFile , delimiter = ',')
#    for row in csvReader: 
#        insert = 'insert into room(roomNo, hotelNo, type, price) values(? , ? , ? , ?)'
#        myCursor.execute(insert, [(row[0]), (row[1]), (row[2]), (row[3])])
#        db.commit()

#with open("customers.csv") as csvFile: 
#    csvReader = csv.reader(csvFile , delimiter = ',')
#    for row in csvReader: 
#        insert = 'insert into guest(guestNo, name, address) values(? , ? , ?)'
#       myCursor.execute(insert,  [(row[0]), (row[1]), (row[2])])
#        db.commit()

#myCursor.execute('''create table if not exists room (roomNo char(4), hotelNo char(4), type char(1), price decimal(5 , 2));''')
#myCursor.execute('''create table if not exists guest (guestNo char(4), name varchar(20), address varchar(50));''')
#myCursor.execute('''create table if not exists booking (hotelNo char(4), guestNo char(4), dateFrom datetime, dateTo datetime, roomNo char(4))''')
#myCursor.execute('''select date('now') as date;''')
#myCursor.execute('''create table if not exists bookingOld (hotelNo char(4), guestNo char(4), dateFrom datetime, dateTo datetime, roomNo char(4))''')

#update = 'update room set price = price*1.05;'

#update = 'update room set price = round(price, 2);'

#update = 'update booking set bookingID = "b001";'
#myCursor.execute(update)
#db.commit()

#myCursor.execute(update)
#db.commit()

#update = 'update bookingOld set bookingID = "b001";'
#myCursor.execute(update)
#db.commit()

#alterTable = 'alter table booking add bookingID integer(4);'
#myCursor.execute(alterTable)
#db.commit()

#alterTable = 'alter table bookingOld drop column bookingNo;'
#myCursor.execute(alterTable)
#db.commit()

#insert = 'insert into room values (1 , "h111" , "s" , 72.00);'
#myCursor.execute(insert)
#db.commit()

#insert = 'insert into booking values ("h111", "g111", date("1999-01-01"), date("1999-01-02"), 1);'
#myCursor.execute(insert) 
#db.commit()

#insert = 'insert into guest values ("g111", "John Smith", "London");'
#myCursor.execute(insert)
#db.commit()

#insert = 'insert into booking (bookingID) values (0001);'
#myCursor.execute(insert)
#db.commit()

#insert = 'insert into bookingOld (bookingID) values (0001);'
#myCursor.execute(insert)
#db.commit()

#insert = 'insert into bookingOld select * from booking where dateTo < date("2000-01-01");'
#myCursor.execute(insert)
#db.commit()

#delete = 'delete from booking where dateTo < date("2000-01-01");'
#myCursor.execute(delete)
#db.commit()

