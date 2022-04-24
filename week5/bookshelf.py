
import requests

def getData(subject):
    URL = "http://openlibrary.org/subject/"+subject+".json"
    try:
        response = requsets.get(URL, timeout=5)
        response.reise_for_status()
        response_JSON = response.json()
        return response_JSON
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)