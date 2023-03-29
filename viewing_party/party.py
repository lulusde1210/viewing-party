# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
	if title and genre and rating:
		return {"title": title, "genre": genre, "rating": rating}
	return None

def add_to_watched(user_data, movie):
	user_data['watched'].append(movie)
	return user_data

def add_to_watchlist(user_data,movie):
	user_data["watchlist"].append(movie)
	return user_data

def watch_movie(user_data, title):
	for movie in user_data['watchlist']:
		if movie['title'] == title:
			user_data['watchlist'].remove(movie)
			user_data['watched'].append(movie)
	return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
	watched = user_data['watched']

	if watched:
		total_rating = sum([movie["rating"] for movie in watched])
		return total_rating / len(watched)
	
	return 0.0

def get_most_watched_genre(user_data):
	if user_data['watched']:
		genre_count = {}
		
		for movie in user_data['watched']:
			genre = movie["genre"]
			genre_count[genre] = genre_count.get(genre,0)+1
			
		most_watched = max(genre_count, key=genre_count.get)
		return most_watched
	
	return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched_movies(user_data, unique_wanted):
	watched = set([tuple(movie.items()) for movie in user_data['watched']])

	friends_watched = set([
		tuple(movie.items()) 
		for friend in user_data['friends'] 
		for movie in friend['watched']
	])

	if unique_wanted == 'user':
		unique_watched = watched - friends_watched
	elif unique_wanted == 'friends':
		unique_watched = friends_watched - watched
	else:
		raise ValueError("Invalid watched_type parameter. "
                        "Must be 'user' or 'friends'.")

	return [dict(movie) for movie in unique_watched]

def get_unique_watched(user_data):
	return get_unique_watched_movies(user_data, 'user')

def get_friends_unique_watched(user_data):
	return get_unique_watched_movies(user_data, 'friends')
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
	recommendation = []
	friends_unique_watched = get_friends_unique_watched(user_data)
	
	for movie in friends_unique_watched:
		if movie["host"] in user_data["subscriptions"]:
			recommendation.append(movie)
			
	return recommendation

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
	recommendation = []
	most_watched = get_most_watched_genre(user_data)
	friends_unique_movies = get_friends_unique_watched(user_data)
	
	for movie in friends_unique_movies:
		if movie["genre"] == most_watched:
			recommendation.append(movie)
			
	return recommendation

def get_rec_from_favorites(user_data):
	recommendation = []
	user_unique_watched = get_unique_watched(user_data)
	
	for movie in user_data["favorites"]:
		if movie in user_unique_watched:
			recommendation.append(movie)
			
	return recommendation