num_mark_movies = int(input())

max_rating = 0.0
name_of_movie_with_max = ""
min_rating = 0.0
name_of_movie_with_min = ""
all_rating_sum = 0.0

for i in range(0, num_mark_movies):
    name_of_movie = input()
    rating_of_movie = float(input())

    all_rating_sum += rating_of_movie

    if i == 0:
        max_rating = rating_of_movie
        min_rating = rating_of_movie
        name_of_movie_with_max = name_of_movie
        name_of_movie_with_min = name_of_movie

    if max_rating < rating_of_movie:
        max_rating = rating_of_movie
        name_of_movie_with_max = name_of_movie

    if rating_of_movie < min_rating:
        min_rating = rating_of_movie
        name_of_movie_with_min = name_of_movie

print(f"{name_of_movie_with_max} is with highest rating: {max_rating:.1f}")
print(f"{name_of_movie_with_min} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {(all_rating_sum / num_mark_movies):.1f}")
