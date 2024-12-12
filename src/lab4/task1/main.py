from utils import User, get_users, get_movies
from recommender import Recommender

movies_path = "movies.txt"
watch_history_path = "watch_history.txt"


def main():
    # Getting all movies
    movies = get_movies(movies_path)

    # Getting all users
    users = get_users(watch_history_path)

    # Initializing recommender
    recommender = Recommender(movies, users)

    # Setting user
    watched_history_input = input()
    user_watch_history = []
    if watched_history_input != "":
        user_watch_history = [int(i) for i in input().split(',')]
    user = User(user_watch_history)

    # Get recommendations
    recommended = recommender.get_recommendations(user)

    print(recommended)


if __name__ == "__main__":
    main()

