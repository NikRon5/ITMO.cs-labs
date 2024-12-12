import unittest

from src.lab4.task1.recommender import Recommender
from src.lab4.task1.utils import User, get_users, get_movies

class RecommenderTestCase(unittest.TestCase):
    def test_recommneder(self):
        # Given
        watch_history_path = "watch_history.txt"
        movies_path = "movies.txt"
        users = get_users(watch_history_path)
        movies = get_movies(movies_path)

        user_watch_history = [2,4]
        user = User(user_watch_history)

        recommender = Recommender(movies, users)

        # When
        recommended_movie = recommender.get_recommendations(user)

        # Then
        self.assertEqual("Дюна", recommended_movie)

    def test_recommender_all_watched(self):
        # Given
        watch_history_path = "watch_history.txt"
        movies_path = "movies.txt"
        users = get_users(watch_history_path)
        movies = get_movies(movies_path)

        user_watch_history = [1,2,3,4]
        user = User(user_watch_history)

        recommender = Recommender(movies, users)

        # When
        recommended_movie = recommender.get_recommendations(user)

        # Then
        self.assertEqual([], recommended_movie)

    def test_recommender_no_wathed(self):
        # Given
        watch_history_path = "watch_history.txt"
        movies_path = "movies.txt"
        users = get_users(watch_history_path)
        movies = get_movies(movies_path)

        user_watch_history = []
        user = User(user_watch_history)

        recommender = Recommender(movies, users)

        # When
        recommended_movie = recommender.get_recommendations(user)

        # Then
        self.assertEqual([], recommended_movie)













