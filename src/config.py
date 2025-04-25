import os
from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = os.getenv("GCP_BUCKET_NAME")
FILE_NAME = "earthquakes.json"
BASE_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"



