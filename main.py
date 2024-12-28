class Film:
    def __init(self, name):
        self.name = name

    def watch(self):
        print('Bon visionnage')

class FilmCassette(Film):
    """Un film en cassette !"""

    def __init__(self, name):
        """Initialise le nom et la bande magnetique."""
        self.name = name
        self.magnetic_tape = True
    
    def rewind(self):
        """Rembobine le film."""
        print("C'est long à rembobiner !")
        self.magnetic_tape = True
class FilmDVD(Film):
    def __init__(self, name):
        self.name = name
    def display_menu(self):
        print('Lancer le dvd')

film_dvd = FilmDVD('Blade runner')
film_dvd.display_menu()