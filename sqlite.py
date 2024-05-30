import sqlite3

#connect to sql 
connection = sqlite3.connect("student.db")

#create a cursor object to insert record, create table
cursor = connection.cursor()

#create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION Varchar(25)
);
"""


cursor.execute(table_info)

cursor.execute(""" Insert into STUDENT values('Pavan', 'Data Science', 'A') """)
cursor.execute(""" Insert into STUDENT values('Raj', 'Data Science', 'B') """)
cursor.execute(""" Insert into STUDENT values('Kumar', 'Data Science', 'A') """)
cursor.execute(""" Insert into STUDENT values('Vikas', 'DEVOPS', 'A') """)
cursor.execute(""" Insert into STUDENT values('Bhart', 'DEVOPS', 'B') """)


print('The inserted records are')
data=cursor.execute(''' Select * from STUDENT ''')

for row in data:
    print(row)

connection.commit()

connection.close()