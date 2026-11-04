# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 11/04/2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

# TO DO 1: Create function add_movie(). 
# TO DO 2: Call the function 4 times.
# TO DO 3: Print the database as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.
def add_movie(database, movie, director, year, runtime):
    '''
    Add a movie to the database.
    @param database (list): The list to store movie information.
    @param title (str): The title of the movie.
    @param director (str): The director of the movie.
    @param year (int): The release year of the movie.
    @param runtime (int): The runtime of the movie.
    @return: The updated database with the new movie added.
    '''
    database.append({'Title': movie, 'Director': director, 'Year': year, 'Runtime': runtime})
    return database

def find_movie(database, title):
    '''
    Find a movie in the database by its title (case-insensitive and partial match by word accepted).
    @param database (list): The list containing movie information.
    @param title (str): The title of the movie to find.
    @return: The movie information if found. Otherwise, returns 'Movie not found.'
    '''
    for movie in database:
        if title.lower() in movie['Title'].lower().split():
            return movie

    return 'Movie not found.'

def main():
    movie_database = []
    add_movie(movie_database, "Inception", "Christopher Nolan", 2010, 148)
    add_movie(movie_database, "The Matrix", "Lana Wachowski, Lilly Wachowski", 1999, 136)
    add_movie(movie_database, "Interstellar", "Christopher Nolan", 2014, 169)
    add_movie(movie_database, "The Godfather", "Francis Ford Coppola", 1972, 175)

    # for movie in movie_database:
    #     print(movie)

    print(find_movie(movie_database, "godfather"))
main()