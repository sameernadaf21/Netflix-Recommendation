
# Netflix Recommendation System

This repository contains a movie recommendation system implemented in Python. The system is designed to recommend movies based on user input and utilizes cosine similarity to find similar movies in a given dataset.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Dataset](#dataset)
- [Algorithm](#algorithm)
- [License](#license)

## Overview

Movie Recommendation System is a Python script that reads a movie dataset, preprocesses it, and provides movie recommendations based on user input. It employs text vectorization and cosine similarity to determine movie similarities and generate recommendations.

## Requirements

To run the movie recommendation system, you'll need the following:

- Python 3.x
- Required Python packages (specified in `requirements.txt`)

You can install the required packages using the following command:

```bash
pip install -r requirements.txt

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


