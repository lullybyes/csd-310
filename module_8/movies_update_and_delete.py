import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="movies_user",
    password="popcorn",
    database="movies"
)

# Create a cursor object
cursor = connection.cursor()

# Use the database
database_name = "movies"
cursor.execute("USE {}".format(database_name))

def show_films(cursor, title):
    # method to execute an inner join on all tables,
    #  iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name'"
                   " from film" 
                   " INNER JOIN genre ON film.genre_id=genre.genre_id"
                   " INNER JOIN studio ON film.studio_id=studio.studio_id")
    
    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    #iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS");

insert_query = "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, genre_id, studio_id) VALUES (%s, %s, %s, %s, %s, %s)"
data = ("Insidious", "2011", "103", "James Wan", 1, 2)
cursor.execute(insert_query, data)

show_films(cursor, "DISPLAYING FILMS AFTER INSERT");

update_query = "UPDATE film SET genre_id = %s WHERE film_name = %s"
update_data = (1, "Alien")  
cursor.execute(update_query, update_data)
connection.commit()
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE");

delete_query = "DELETE FROM film WHERE film_name = %s"
delete_data = ("Gladiator",) 
cursor.execute(delete_query, delete_data)

show_films(cursor, "DISPLAYING FILMS AFTER DELETE");
