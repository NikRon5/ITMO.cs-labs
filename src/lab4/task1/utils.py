class User:
    def __init__(self, watch_history):
        self.watch_history = watch_history

def get_movies(path):
    f = open(path, encoding='utf-8')
    movies = {}
    for movie in f.read().split("\n"):
        t_movie = movie.split(",")
        movies[int(t_movie[0])] = t_movie[1]
    f.close()
    return movies

def get_users(path):
    f = open(path, encoding='utf-8')
    users = []
    for user in f.read().split("\n"):
        user_watch_history = [int(i) for i in user.split(',')]
        users.append(User(user_watch_history))
    f.close()
    return users

