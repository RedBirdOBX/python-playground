current_movies = {
    "Dune" : "12:00 PM",
    "Dune 2" : "2:00 PM",
    "Blade Runner" : "4:00 PM",
    "Blade Runner 2049" : "6:00 PM"
}

print("Current movies and their times:")
for movie in current_movies:
    print(movie)

requested_movie = input("Enter the movie you want to watch:\n")
movie_time = current_movies.get(requested_movie, "Movie not found")
print("movie time:", movie_time)




