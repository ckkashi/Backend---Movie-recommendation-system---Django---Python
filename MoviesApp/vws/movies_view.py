from rest_framework.decorators import api_view
from rest_framework.response import Response
from MoviesApp.serializers import FavMoviesSerializer
from MoviesApp.models import FavMovies

# importing file fetching libraries
import os
import json
from django.conf import settings

class data_class:
    json_data=''

    # get movies from file
    def fetch_movies():
        read_file_path = os.path.join(settings.BASE_DIR,'movies_data.json')
        file_data = open(read_file_path)
        data_class.json_data = json.load(file_data.buffer)
        file_data.close()


@api_view(['GET'])
def get_movies(Request):
    try:
        if(data_class.json_data == ''):
            data_class.fetch_movies()
        return Response({"status":"Success","message": "Movies found.","data":data_class.json_data},status=200)
    except:
        return Response({"status":"Error","message": "Movies not found."},status=404)

@api_view(['GET'])
def get_movie_by_id(Request):
    movie_id = Request.GET.get('movie_id')
    if not movie_id:
        return Response({"status": "Error", "message": "Movie ID is required."}, status=400)
    try:
        movie_id = int(movie_id)
        if(data_class.json_data == ''):
            data_class.fetch_movies()

        movie = next((item for item in data_class.json_data if item.get('id') == movie_id), None)
        if movie:
            return Response({"status": "Success", "message": "Movie found.", "data": movie}, status=200)
        else:
            return Response({"status": "Error", "message": "Movie not found."}, status=404)
    except:
        return Response({"status":"Error","message": "Something went wrong."},status=404)
    
# fav movies functions
@api_view(['POST'])
def add_movies_to_fav(Request):
    user_id = Request.data['user_id']
    movie_id = Request.data['movie_id']
    movie_title = Request.data['movie_title']
    if not movie_id and not user_id and not movie_title:
        return Response({"status": "Error", "message": "Movie ID, Movie title, User ID, is required."}, status=400)
    try:
        movie_id = int(movie_id)
        user_id = int(user_id)

        check_exist = FavMovies.objects.filter(user_id=user_id,movie_id=movie_id)
        if check_exist:
            return Response({"status": "Error", "message": "Movie already added to favourite."}, status=400)
        else:
            fav_movie = FavMoviesSerializer(data=Request.data)
            if fav_movie.is_valid():
                fav_movie.save()
                return Response({"status": "Success", "message": "Movie added to favourite successfully.", "data": fav_movie.data}, status=200)
            else:
                return Response({"status": "Error", "message": "Something went wrong."}, status=400)    
    except:
        return Response({"status":"Error","message": "Something went wrong."},status=400)

@api_view(['GET'])
def get_user_fav_movies(Requests):
    user_id = Requests.GET.get('user_id')
    detailed = Requests.GET.get('detailed') or 0
    if not user_id:
        return Response({"status": "Error", "message": "User ID is required."}, status=400)
    try:
        user_id = int(user_id)
        detailed = int(detailed)
        fav_movies = FavMovies.objects.filter(user_id=user_id)
        if fav_movies:
            if detailed == 0:
                serialized_data = FavMoviesSerializer(fav_movies, many=True)
                print(serialized_data.data)
                return Response({"status": "Success", "message": "Favourite movies fetched successfully.", "data": serialized_data.data}, status=200)
            elif detailed == 1:
                fav_movies_data = []
                if(data_class.json_data == ''): 
                    data_class.fetch_movies()
                for fav_movie in fav_movies:
                    movie = next((item for item in data_class.json_data if item.get('id') == fav_movie.movie_id), None)
                    if movie:
                        fav_movies_data.append(movie)
                return Response({"status": "Success", "message": "Favourite movies detailed fetched successfully.", "data": fav_movies_data}, status=200)
            else:
                return Response({"status": "Error", "message": "Only two modes are available, for only ids their is 0, for complete detail their is 1."}, status=404)
        else:
            return Response({"status": "Error", "message": "Favourite movies not found."}, status=404)
    except:
        return Response({"status":"Error","message": "Something went wrong."},status=400)
