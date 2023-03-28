# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {}
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
        
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
    if user_data["watched"] == []:
        return 0.0
    total = 0
    for movie in user_data["watched"]:
        total += movie["rating"]
    avg_rating = total/len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    if user_data['watched']:
        genre_dict = {}
        for movie in user_data['watched']:
            genre_dict[movie["genre"]] = genre_dict.get(movie["genre"],0)+1
        most_watched = max(genre_dict, key=genre_dict.get)
        return most_watched
    return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def aggregate_friends_watched(user_data):
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)
    return friends_watched

def get_unique_watched(user_data):
    friends_watched = aggregate_friends_watched(user_data)
    unique_watched = []
    for movie in user_data['watched']:
        if movie not in friends_watched:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    friends_watched = aggregate_friends_watched(user_data)
    unique_watched = []

    for movie in friends_watched:
        if movie not in user_data['watched'] and movie not in unique_watched:
                unique_watched.append(movie)
    return unique_watched
        
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