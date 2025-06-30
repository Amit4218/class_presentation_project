import requests

def get_riddle():

    try:

        response = requests.get("http://localhost:5000/get-random-riddle")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching riddle: {e}")
        return None
