from MoviesApp.vws.auth_views import register_user,login_user,get_user_by_id
from MoviesApp.vws.movies_view import get_movies, get_movie_by_id, add_movies_to_fav, get_user_fav_movies
from django.urls import path

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('getUserById', get_user_by_id),
    path('getMovies', get_movies),
    path('getMovieById', get_movie_by_id),
    path('addFavMovie', add_movies_to_fav),
    path('getFavMovies', get_user_fav_movies)
]