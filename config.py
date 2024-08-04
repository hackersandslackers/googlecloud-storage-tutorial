"""Google Cloud Storage Configuration."""
from os import environ

# Google Cloud Storage
bucket_url = environ.get("GCP_BUCKET_URL")
bucket_name = environ.get("GCP_BUCKET_NAME")
bucket_dir = environ.get("GCP_BUCKET_FOLDER_NAME")

# Data
local_dir = environ.get("LOCAL_FOLDER")
