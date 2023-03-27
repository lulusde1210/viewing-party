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
            genre_dict.setdefault(movie['genre'], 0)
            genre_dict[movie['genre']] += 1
        most_watched = max(genre_dict, key=genre_dict.get)
        return most_watched
    return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

