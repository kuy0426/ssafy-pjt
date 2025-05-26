import requests
from movies.models import Movie, Actor, MovieActor

API_KEY = "YOUR_TMDB_API_KEY"

def fetch_movies(request):
    response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1")
    data = response.json()

    for movie in data["results"]:
        movie_obj, created = Movie.objects.get_or_create(title=movie["title"], release_date=movie["release_date"])

        # 배우 정보 가져오기
        movie_id = movie["id"]
        cast_response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}")
        cast_data = cast_response.json()

        for actor in cast_data.get("cast", []):
            actor_obj, _ = Actor.objects.get_or_create(name=actor["name"])
            MovieActor.objects.get_or_create(movie=movie_obj, actor=actor_obj)

    return JsonResponse({"message": "Movies and actors fetched successfully!"})
