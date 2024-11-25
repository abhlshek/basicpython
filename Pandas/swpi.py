import requests

# Define the API endpoint
url = "https://swapi.dev/api/films/"

try:
    # Send GET request
    response = requests.get(url)

    # Raise an exception if the request was unsuccessful
    response.raise_for_status()

    # Parse JSON response
    data = response.json()

    # Process and print film titles
    print("Star Wars Films:")
    for film in data['results']:
        print(f"Title: {film['title']}, Release Date: {film['release_date']}")
except requests.exceptions.RequestException as e:
    print("Error while calling SWAPI:", e)
