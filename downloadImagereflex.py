from requests import get
from pexels_api import API

PEXELS_API_KEY = '563492ad6f9170000100000182b38119805b48fcb467bb8019e2bcbd'

api = API(PEXELS_API_KEY)
api.search('reflection', page=1, results_per_page=5)
photos = api.get_entries()

urls = [photo.url for photo in photos]
