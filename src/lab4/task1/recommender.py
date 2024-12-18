class Recommender:
    def __init__(self, movies, users):
        self.movies = movies
        self.users = users

    def get_recommendations(self, user):
        unwatched_movies = []
        for another_user in self.users:
            c = 0
            for users_movie in user.watch_history:
                if users_movie in another_user.watch_history:
                    c+=1
                    if c >= len(user.watch_history)/2:
                        unwatched_movies += another_user.watch_history
                        break
        unwatched_movies = self.__remove_watched_movies(unwatched_movies, user.watch_history)

        if len(unwatched_movies) == 0:
            return []
        else:
            recommended_id = max(unwatched_movies, key=unwatched_movies.count)
            recommended_name = self.movies[recommended_id]
            return recommended_name

    def __remove_watched_movies(self, movies, watched_movies):
        wathed_movies = []
        for movie in movies:
            if movie not in watched_movies:
                wathed_movies.append(movie)
        return wathed_movies