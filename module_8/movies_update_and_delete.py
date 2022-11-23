import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "root",
    "password": "Vamp!re77",
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
        
cursor = db.cursor()

def show_films(cursor, title):
    # method to execute an inner join on all tables,
    #   iterate over the dataset and output the results to the terminal window.

    #inner join query
    cursor.execute("""SELECT film_name AS Name, film_director As Director, genre_name AS Genre, studio_name AS 'Studio Name'
                    FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id""")
    
    # get the results from the cursor object
    films = cursor.fetchall()
    
    print("\n -- {} --".format(title))
    
    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

db.close()