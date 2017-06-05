# Defining movie class that will store information about movies
import webbrowser


class Movie():
    """ Constructor that will create movie objects with the following attributes
        title: A string stores the title of the movie
        storyline: String stores the description of the movie
        poster_image_url: String store the URL of movie's poster
        trailer_youtube_url: String to store the URL of movie's trailer
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Instance methods to play the movie trailer in a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
