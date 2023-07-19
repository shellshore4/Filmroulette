import json
import os
import random
import requests

def lambda_handler(event, context):
    # Get the TMDb API key from the environment variables
    tmdb_api_key = os.environ['TMDB_API_KEY']
    num = random.randint(1,340)
    # Get the top rated movies from TMDb
    response = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?page={num}&api_key={tmdb_api_key}')

    # Check that the request was successful
    if response.status_code == 200:
        # Parse the response
        data = response.json()

        # Select a random movie from the top rated movies
        movie = random.choice(data['results'])

        # Return the recommended movie's data
        return {
            'statusCode': 200,
            'body': json.dumps({
                'title': movie['title'],
                'overview': movie['overview'],
                'poster_path': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            }),
            'headers': {
                'Content-Type': 'application/json',
            },
        }
    else:
        # If the request was not successful, return an error message
        return {
            'statusCode': response.status_code,
            'body': 'Could not get data from TMDb API',
        }
