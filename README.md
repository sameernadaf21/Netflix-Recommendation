
# Netflix Recommendation System

This repository contains a movie recommendation system implemented in Python. The system is designed to recommend movies based on user input and utilizes cosine similarity to find similar movies in a given dataset.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Dataset](#dataset)
- [Algorithm](#algorithm)

## Overview

Movie Recommendation System is a Python script that reads a movie dataset, preprocesses it, and provides movie recommendations based on user input. It employs text vectorization and cosine similarity to determine movie similarities and generate recommendations.

## Requirements

To run the movie recommendation system, you'll need the following:

- Python 3.x
- Required Python packages (specified in `requirements.txt`)

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```
## Usage
To use the Movie Recommendation System, follow these steps:
1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/movie-recommendation.git
   ```
2. Navigate to the project directory:
    ```bash
    cd movie-recommendation
     ```
3. Make sure you have the dataset file ('dataset.csv') in the same directory as the script.
4. Run the recommendation script:
    ```bash
    python movie_recommendation.py
     ```
## Dataset
The movie recommendation system uses a dataset ('dataset.csv') containing information about movies. The dataset includes columns such as 'id,' 'title,' 'overview,' 'genre,' and 'vote_average.' You can replace this dataset with your own movie dataset, ensuring that it has similar columns.
## Algorithm

The recommendation system uses the following algorithm:

1. **Load and preprocess the movie dataset:**
   - Import the dataset and perform initial data exploration.
   - Clean and select relevant features.

2. **Text Vectorization and Cosine Similarity Calculation:**
   - Combine 'overview' and 'genre' information to create 'tags.'
   - Convert text data into numerical vectors using CountVectorizer.
   - Calculate cosine similarity between movie vectors.

3. **Movie Recommendation Function:**
   - Create a function to recommend movies based on user input.
   - Find close matches to the user's input movie title.
   - Sort movies by similarity and display the top 5 recommendations.


