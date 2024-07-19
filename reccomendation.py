import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split

# Sample data: User IDs, Movie IDs, Ratings
data = {
    'user_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'movie_id': [101, 102, 103, 101, 102, 104, 101, 103, 104],
    'rating': [5, 3, 4, 4, 2, 5, 4, 5, 4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a User-Item Matrix
user_item_matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating')

# Fill NaN values with 0
user_item_matrix.fillna(0, inplace=True)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# Convert the similarity matrix to a DataFrame
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to get movie recommendations for a given user
def get_recommendations(user_id, num_recommendations=5):
    # Get the similarity scores for the given user
    similarity_scores = user_similarity_df[user_id]
    
    # Get the movies rated by the given user
    user_rated_movies = user_item_matrix.loc[user_id]
    
    # Find the users most similar to the given user
    similar_users = similarity_scores.nlargest(num_recommendations + 1).index[1:]
    
    # Get the movies rated by the similar users
    similar_users_ratings = user_item_matrix.loc[similar_users]
    
    # Compute the average rating for each movie
    avg_ratings = similar_users_ratings.mean(axis=0)
    
    # Exclude the movies already rated by the given user
    recommendations = avg_ratings[user_rated_movies == 0].nlargest(num_recommendations)
    
    return recommendations

# Example usage
user_id = 1
recommendations = get_recommendations(user_id)
print(f"Recommendations for User {user_id}:\n{recommendations}")
# This output suggests that movie 104 is reccomended for user 1 with an average rating of 4.5 from similar users