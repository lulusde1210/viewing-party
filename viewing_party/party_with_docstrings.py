# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
	"""
	Creates and returns a dictionary representing a movie with the given 
	title, genre, and rating.

    Parameters:
        title (str): The title of the movie.
        genre (str): The genre of the movie.
        rating (float): The rating of the movie.

    Returns:
        dict: A dictionary representing a movie with the given title, genre, 
		and rating.

        If any of the arguments are falsy, None is returned.
    """
	if title and genre and rating:
		return {"title": title, "genre": genre, "rating": rating}
	return None

def add_to_watched(user_data, movie):
	"""
	Adds the given movie to the user's "watched" list.

    Parameters:
        user_data (dict): A dictionary representing user data, including a
		"watched" list of movie dictionaries.

        movie (dict): A dictionary representing a movie. 

    Returns:
        dict: An updated user_data dictionary with the given movie added to 
		the "watched" list.
    """
	user_data['watched'].append(movie)
	return user_data

def add_to_watchlist(user_data,movie):
	"""
	Adds the given movie to the user's "watchlist".

    Parameters:
        user_data (dict): A dictionary representing user data, including a 
		"watchlist" list of movie dictionaries.

        movie (dict): A dictionary representing a movie.

    Returns:
        dict: An updated user_data dictionary with the given movie added to 
		the "watchlist".
    """
	user_data["watchlist"].append(movie)
	return user_data

def watch_movie(user_data, title):
	"""
	Moves the movie with the given title from the user's "watchlist" to their 
	"watched" list and returns the updated user_data dictionary.

    Parameters:
        user_data (dict): A dictionary representing user data, including a
		"watchlist" list of movie dictionaries and a "watched" list of
		movie dictionaries.

        title (str): The title of the movie to watch.

    Returns:
        dict: An updated user_data dictionary with the movie with the given 
		title moved from the "watchlist" to the "watched" list.
    """
	for movie in user_data['watchlist']:
		if movie['title'] == title:
			user_data['watchlist'].remove(movie)
			user_data['watched'].append(movie)
	return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
	"""
    Calculate the average rating of all movies in the user's watched list.

    Parameters:
        user_data (dict): A dictionary representing user data, including a
		"watched" list of movie dictionaries.

    Returns:
		float: The average rating of all movies in the watched list. 
		If the list is empty, the function returns 0.0.
    """
	watched = user_data['watched']

	avg = sum([movie["rating"] for movie in watched]) / len(watched) \
		if watched else 0.0
	
	return avg

def get_most_watched_genre(user_data):
	"""
    Determine the genre with highest occurances in the user's watched list.

    Parameters:
        user_data (dict): A dictionary representing user data, including a
		"watched" list of movie dictionaries.

    Returns:
		str or None: The genre that is most frequently watched. If "watched" 
		list is empty, the function returns None.
    """
	genre_count = {}
	
	for movie in user_data['watched']:
		genre_count[movie["genre"]] = genre_count.get(movie["genre"], 0) + 1
		
	most_watched =  max(genre_count, key=genre_count.get) \
		if user_data['watched'] else None

	return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched_movies(user_data, unique_wanted):
	"""
    Return a list of movies that the user has watched and none of their 
	friends have watched (or vice versa).
    
    Parameters:
        user_data (dict): A dictionary representing user data, including a
		"watched" list of movie dictionaries and a "friends" list of
		dictionaries representing friends. The friends dictionaries include a
		"watched" lists of movie dictionaries.

        unique_wanted (str): A string representing whose list of unique movies
		you want (either 'user' or 'friends').
    
    Returns:
        list: A list of dictionaries, where each dictionary represents a 
		unique movie that only the unique_wanted has watched.
    """
	watched = set([tuple(movie.items()) for movie in user_data['watched']])

	friends_watched = set([ tuple(movie.items()) \
		for friend in user_data['friends'] for movie in friend['watched']])

	unique_watched = watched - friends_watched if unique_wanted == 'user' \
		else friends_watched - watched

	return [dict(movie) for movie in unique_watched]

def get_unique_watched(user_data):
	"""
    Find movies that the user has watched and none of their friends have.
    
    Parameters:
        user_data (dict): A dictionary representing user data, including a
		"watched" list of movie dictionaries and a "friends" list of
		dictionaries representing friends. The friends dictionaries include a
		"watched" lists of movie dictionaries.
    
    Returns:
        list: A list of dictionaries, where each dictionary represents a 
		unique movie that only the user has watched.
    """
	return get_unique_watched_movies(user_data, 'user')

def get_friends_unique_watched(user_data):
	"""
    Find movies that the user's friends have watched and the user has not.
    
    Parameters:
        user_data (dict): A dictionary representing user data, including a
		"watched" list of movie dictionaries and a "friends" list of
		dictionaries representing friends. The friends dictionaries include a
		"watched" lists of movie dictionaries.

    Returns:
        list: A list of dictionaries where each dictionary represents a unique
		movie that only the user's friends have watched.
    """
	return get_unique_watched_movies(user_data, 'friends')
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
	"""
    Create a list of movie recommendations available to the user based on 
	their subscriptions.

    Parameters:
		user_data (dict): A dictionary containing user data, including a list 
		of their subscriptions and their friends' watched movies.

    Returns:
		list: A list of movie recommendations available to the user based on 
		their subscriptions.
    """
	friends_unique_watched = get_friends_unique_watched(user_data)

	recommendation = [movie for movie in friends_unique_watched \
		if movie["host"] in user_data["subscriptions"]]

	return recommendation

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
	"""
	Create a lit of movie recommendations based on the user's most watched
	genre and the movies their friends have watched and they have not.
    
    Parameters:
        user_data (dict): A dictionary that contains a user's data including
        their watched list and their friends' data.
    
    Returns:
        list: A list of unique movie recommendations that belong to the user's
        most watched genre based on their friends' watched list.
    """
	most_watched_genre = get_most_watched_genre(user_data)
	friends_unique_movies = get_friends_unique_watched(user_data)
	
	recommendation =  [movie for movie in friends_unique_movies \
		if movie["genre"] == most_watched_genre]
	
	return recommendation

def get_rec_from_favorites(user_data):
	"""
	Create a list of movie recommendations based on the user's favorite movies
	that the user's friends have not watched.
	
	Parameters:
		user_data (dict): A dictionary that contains a user's data including
		their watched list, their friends' data.
	
	Returns:
		list: A list of unique movie recommendations that belong to the user's
		favorite movies that the user's friends have not watched.
	"""
	user_unique_watched = get_unique_watched(user_data)

	recommendation = [movie for movie in user_data["favorites"] \
		if movie in user_unique_watched]
	
	return recommendation