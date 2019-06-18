"""BigQuery Upload Configuration."""
from os import environ


# Google Cloud Storage
bucketURI = environ.get('GCP_BUCKET_URI')
bucketName = environ.get('GCP_BUCKET_NAME')
bucketFolder = environ.get('GCP_BUCKET_FOLDER_NAME')

# Data
localFolder = environ.get('LOCAL_FOLDER')
