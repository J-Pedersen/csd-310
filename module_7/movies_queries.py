import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "user",
    "password": "password",
    "host": "127.0.0.1",

        "database": "movies",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """

    db = mysql.connector.connect(**config) # connect to the pysports database
   
    # output the connection status
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

print("\n-- DISPLAYING Studio RECORDS --")
cursor = db.cursor()
cursor.execute("SELECT studio_id,studio_name FROM studio;") # selecting all studio fields
studio = cursor.fetchall()
for studio in studio:
    print(" Studio ID: {}\n Studio Name: {}\n".format(studio[0],studio[1])) # both studio fields 

print("\n-- DISPLAYING Genre RECORDS --")
cursor = db.cursor()
cursor.execute("SELECT genre_id, genre_name FROM genre;") # selecting all genre fields
genre = cursor.fetchall()
for genre in genre:
    print(" Genre ID: {}\n Genre Name: {}\n".format(genre[0],genre[1])) # both genre fields 

print("\n-- DISPLAYING Short Film RECORDS --")
cursor = db.cursor()
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;") # selecting only movies shorter than two hours
film = cursor.fetchall()
for film in film:
    print(" Film Name: {}\n Runtime: {}\n".format(film[0],film[1])) # movie name and runtime fields 

print("\n-- DISPLAYING Director RECORDS in Order --")
cursor = db.cursor()
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director;") # selecting movies and directors and sorting by director
film = cursor.fetchall()
for film in film:
    print(" Film Name: {}\n  Director: {}\n".format(film[0],film[1])) # movie name and director fields
    
db.close()
