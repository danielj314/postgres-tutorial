import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object on the database
cursor = connection.cursor()

# Queery 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Queery 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Queery 3 - select only the "Queen" column from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Queery 4 - select only the "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Queery 5 - select only the albums with "ArtistId" #51 from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Queery 6 - select all tracks where composer is "Queen" from "Track"
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)

