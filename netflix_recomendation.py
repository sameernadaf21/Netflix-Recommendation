# Importing necessary libraries
import pandas as pd
import difflib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie dataset from a CSV file
movies = pd.read_csv('dataset.csv')

# Explore the dataset
# Display the first 10 rows
movies.head(10)

# Get summary statistics of the dataset
movies.describe()

# Display dataset information, including column data types and missing values
movies.info()

# Check for missing values in the dataset
movies.isnull().sum()

# Feature Selection: Select specific columns for analysis
selected_features = ['id', 'title', 'overview', 'genre', 'vote_average']
movies = movies[selected_features]

# Create a new column 'tags' by combining 'overview' and 'genre' columns
movies['tags'] = movies['overview'] + movies['genre']

# Text Vectorization: Convert 'tags' column into numerical vectors
cv = CountVectorizer(max_features=10000, stop_words='english')
vector = cv.fit_transform(movies['tags'].values.astype('U')).toarray()

# Calculate the shape of the vectorized data
vector.shape

# Calculate cosine similarity between movie vectors
similarity = cosine_similarity(vector)

# Define a function to recommend movies
def recommend(movie_title):
    # Lists to store recommended movie details
    recommended_titles = []
    recommended_ratings = []
    recommended_genres = []

    # Find close matches to the input movie title
    matches = difflib.get_close_matches(movie_title, movies['title'])
    
    if matches:
        # Find the index of the closest match
        index = movies[movies['title'] == matches[0]].index[0]
        
        # Sort movies by similarity and get the top 5 recommendations
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        for i in distance[0:5]:
            recommended_titles.append(movies.iloc[i[0]]['title'])
            recommended_ratings.append(movies.iloc[i[0]]['vote_average'])
            recommended_genres.append(movies.iloc[i[0]]['genre'])
        
        # Create a DataFrame to display recommendations
        recommended_movies_df = pd.DataFrame({
            'Movie Title': recommended_titles,
            'Rating': recommended_ratings,
            'Genre': recommended_genres
        }, index=range(1, 6))  # Index 1 to 5 for top 5 recommendations
        
        print(recommended_movies_df)
    else:
        print("No close matches found for the given movie title.")

# Example of recommending movies based on a movie title
recommend("Dilwale Dulhania Le Jayenge")

# Example of recommending movies based on a partial movie title
recommend("batm")
