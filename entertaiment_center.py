""" This file contains all information about each movies.
    media.py will take these information and display
    them on the website
"""
import media
import fresh_tomatoes

""" Initializing movie objects with information such as: title,
    storyline, poster image url, and trailer youtube url
"""

# Create instances for movie: Pirate of the Carribean
pirate = media.Movie("Pirate of the Carribean", "Story about Pirate Life",
                     "https://upload.wikimedia.org/wikipedia/en/c/c6/On_Stranger_Tides_Poster.jpg",  # nopep8
                     "https://www.youtube.com/watch?v=IPf4rGw3XHw")

# Create instances for movie: Transformer
transformer = media.Movie("Transformer",
                          "Story about robots fighting each other",
                          "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg",  # nopep8
                          "https://www.youtube.com/watch?v=uD5IJvKcbEQ")

# Create instances for movie: Sherlock Holmes
sherlock = media.Movie("Sherlock Holmes", "Film about Sherlock Holmes",
                       "http://vignette3.wikia.nocookie.net/bakerstreet/images/d/db/Sherlock_holmes_ritchie.jpg/revision/latest?cb=20130202212947",  # nopep8
                       "https://www.youtube.com/watch?v=Egcx63-FfTE")


# Add all of the movie in an array to display them on the website
movies = [pirate, transformer, sherlock]

# Open all of the movies in browser by using fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
