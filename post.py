import psycopg2
  
conn = None
try:
    # connect to the PostgreSQL server
    conn = psycopg2.connect(
        host='localhost',
        dbname='mydb',
        user='postgres',
        password='user',
        port=5432
    )
  
    # Creating a cursor with name cur.
    cur = conn.cursor()
    #cur.execute(
     #   "CREATE TABLE blob_datastore (s_no serial, file_name VARCHAR ( 50 ), blob_data bytea)")
    # SQL query to insert data into the database.
    insert_script = '''
        INSERT INTO blob_datastore(s_no,file_name,blob_data) VALUES (%s,%s,%s);
    '''
  
    # open('File,'rb').read() is used to read the file.
    # where open(File,'rb').read() will return the binary data of the file.
    # psycopg2.Binary(File_in_Bytes) is used to convert the binary data to a BLOB data type.
    BLOB_1 = psycopg2.Binary(
        open(f"files\\toast_flip.mp4", 'rb').read())       # Video
    BLOB_2 = psycopg2.Binary(
        open(f'files\\ex.jpg', 'rb').read())        # Image
    BLOB_3 = psycopg2.Binary(open(f'files\\a-gif.gif', 'rb').read())        # GIF
    BLOB_4 = psycopg2.Binary(open(f'files\\UNIT IV.pdf', 'rb').read())   # PDF
  
    # And Finally we pass the above mentioned values to the insert_script variable.
    insert_values = [(1, 'toast_flip.mp4', BLOB_1), (2, 'ex.jpg', BLOB_2),
                     (3, 'a-gif.gif', BLOB_3), (4, 'UNIT IV.pdf', BLOB_4)]
  
    # The execute() method with the insert_script & insert_value as argument.
    for insert_value in insert_values:
        cur.execute(insert_script, insert_value)
        print(insert_value[0], insert_value[1],
              "[Binary Data]", "row Inserted Successfully")
  
    # SQL query to fetch data from the database.
    cur.execute('SELECT * FROM BLOB_DataStore')
  
    # open(file,'wb').write() is used to write the binary data to the file.
    for row in cur.fetchall():
        BLOB = row[2]
        open("new"+row[1], 'wb').write(BLOB)
        print(row[0], row[1], "BLOB Data is saved in Current Directory")
  
    # Close the connection
    cur.close()
  
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        
        # Commit the changes to the database
        conn.commit()