"""Google Cloud Storage Configuration."""

from os import environ, getenv, path

from dotenv import load_dotenv

# Resolve local directory
BASE_DIR: str = path.abspath(path.dirname(__file__))

# Google Cloud Storage Secrets
environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcloud.json"
load_dotenv(path.join(BASE_DIR, ".env"))

BUCKET_URL = getenv("GCP_BUCKET_URL")
BUCKET_NAME = getenv("GCP_BUCKET_NAME")
BUCKET_DIR = getenv("GCP_BUCKET_FOLDER_NAME")

# Example local files
LOCAL_DIR = path.join(BASE_DIR, "files")
SAMPLE_CSV = path.join(BASE_DIR, "sample_csv.csv")
SAMPLE_IMG = path.join(BASE_DIR, "sample_image.jpg")
SAMPLE_TXT = path.join(BASE_DIR, "sample_text.txt")
