from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from database import Database
from database import MOVIE_LIST
import pytube

class Media_management_app:
    def __init__(self):
        ...

    @staticmethod
    def show_menu():
        print("1.Add")
        print("2.Edit")
        print("3.Remove")
        print("4.Search")
        print("5.Search by time")
        print("6.Show movie info")
        print("7.Download")
        print("8.Exit")

    @staticmethod
    def add():
        choice = int(input("1.film 2.series 3.Documentary 4.clip \nwhat do you want add:"))
        name = str(input("Please enter your movie name: "))
        director = str(input("Please enter your director name: "))
        IMDB_score = float(input("Please enter IMDB score movie: "))
        url = str(input("Please enter your movie url: "))
        duration = int(input("Please enter your movie duration(enter minute): "))
        name_actor = str(input("Please separate the names with (,)\nPlease enter your movie actors: "))
        name_actor = list(name_actor.split(","))
        genre = str(input("Please separate the names with (,)\nPlease enter your movie genre: "))
        genre = list(genre.split(","))
        release_year = int(input("Please enter your movie release year: "))

        if choice == 1:
            new_movie = Film(name,director,IMDB_score,url,duration,name_actor,genre,release_year)

        elif choice == 2:
            episode = int(input("Please enter number of episode: "))
            new_movie = Series(name,director,IMDB_score,url,duration,name_actor,genre,release_year,episode)

        elif choice == 3:
            new_movie = Documentary(name,director,IMDB_score,url,duration,name_actor,genre,release_year)

        elif choice == 4:
            new_movie = Clip(name,director,IMDB_score,url,duration,name_actor,genre,release_year)

        else:
            print("We dont have another type of movie")
            return

        MOVIE_LIST.append(new_movie)
        print("movie add successful.")

    @staticmethod
    def edit():
        name = str(input("Please enter your movie want edit:"))
        for movie in (MOVIE_LIST):
            if movie.name == name:
                if isinstance(movie, Series):
                    print(f"{movie.name}  {movie.director}  {movie.IMDB_score}  {movie.url}  {movie.duration}  {movie.actor}  {movie.genre}  {movie.release_year}  {movie.episode}")
                    edit_attribute = int(input("1.name  2.director  3.IMDB_score  4.url  5.duration  6.actors  7.genre  8.release_year  9.episode\nwhich you want:"))
                else:
                    print(f"{movie.name}  {movie.director}  {movie.IMDB_score}  {movie.url}  {movie.duration}  {movie.actor}  {movie.genre}  {movie.release_year}")
                    edit_attribute = int(input("1.name  2.director  3.IMDB_score  4.url  5.duration  6.actors  7.genre  8.release_year\nwhich you want:"))

                new_attribute = input("Please enter new value: ")
                if edit_attribute == 1:
                    movie.name = new_attribute
                elif edit_attribute == 2:
                    movie.director = new_attribute
                elif edit_attribute == 3:
                    movie.IMDB_score = float(new_attribute)
                elif edit_attribute == 4:
                    movie.url = new_attribute
                elif edit_attribute == 5:
                    movie.duration = int(new_attribute)
                elif edit_attribute == 6:
                    movie.actor = list(new_attribute.split(","))
                elif edit_attribute == 7:
                    movie.genre = list(new_attribute.split(","))
                elif edit_attribute == 8:
                    movie.release_year = int(new_attribute)
                elif edit_attribute == 9 and isinstance(movie, Series):
                    movie.episode = int(new_attribute)
                print("operation successful")
                return 
        print("We dont have this movie!")

    @staticmethod
    def remove():
        global MOVIE_LIST
        name = str(input("Please enter your movie want remove:"))
        for movie in MOVIE_LIST:
            if movie.name == name:
                new_movie = [movie for movie in MOVIE_LIST if movie.name != name]
                MOVIE_LIST = new_movie
                print("operation successful")
                return
        else:
            print("We dont have this movie!")
            return

    @staticmethod
    def search():
        name = input("Please enter your movie name: ")
        for row in MOVIE_LIST:
            if row.name == name:
                if isinstance(row,Series):
                    print(f"{row.name}  {row.director}  {row.IMDB_score}  {row.url}  {row.duration}  {row.actor}  {row.genre}  {row.release_year}  {row.episode}")
                    break
                else:
                    print(f"{row.name}  {row.director}  {row.IMDB_score}  {row.url}  {row.duration}  {row.actor}  {row.genre}  {row.release_year}")
                    break
        else:
            print("We dont have this movie!")

    @staticmethod
    def search_by_time():
        small_time = int(input("Please enter your movie time zone(smaller time): ")) - 1
        big_time = int(input("Please enter your movie time zone(bigger time): ") ) + 1
        for row in MOVIE_LIST:
            if int(row.duration) >= small_time and int(row.duration) <= big_time:
                if isinstance(row,Series):
                    print(f"{row.name}  {row.director}  {row.IMDB_score}  {row.url}  {row.duration}  {row.actor}  {row.genre}  {row.release_year}  {row.episode}")
                else:
                    print(f"{row.name}  {row.director}  {row.IMDB_score}  {row.url}  {row.duration}  {row.actor}  {row.genre}  {row.release_year}")

    @staticmethod
    def show_info():
        for movie in MOVIE_LIST:

            if isinstance(movie,Series):
                print(f"{movie.name}  {movie.director}  {movie.IMDB_score}  {movie.url}  {movie.duration}  {movie.actor}  {movie.genre}  {movie.release_year}  {movie.episode}")
            else:
                print(f"{movie.name}  {movie.director}  {movie.IMDB_score}  {movie.url}  {movie.duration}  {movie.actor}  {movie.genre}  {movie.release_year}")

    @staticmethod
    def download():
        user_want = input("Please enter your movie name: ")
        for movie in MOVIE_LIST:
            if movie.name == user_want:
                pytube.YouTube(movie.url).streams.first().download()
                print("download completed.")
                break
        else:
            print("We dont have this movie!")
        

print("Loading")
Database.read()
print("Loading complete")

while True:
    Media_management_app.show_menu()
    choice = int(input("what do yo want? "))

    if choice == 1:
        Media_management_app.add() 

    elif choice == 2:
        Media_management_app.edit()
        
    elif choice == 3:
        Media_management_app.remove()
    
    elif choice == 4:
        Media_management_app.search()

    elif choice == 5:
        Media_management_app.search_by_time()

    elif choice == 6:
        Media_management_app.show_info()

    elif choice == 7:
        Media_management_app.download()

    elif choice == 8:
        print("Thank you for choosing us")
        Database.write()
        exit(0)

    else:
        print("Enter number between 1 and 8")
