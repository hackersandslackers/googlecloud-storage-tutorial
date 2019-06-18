"""Google Cloud Storage Configuration."""
from os import environ


# Google Cloud Storage
bucketURL = environ.get('GCP_BUCKET_URL')
bucketName = environ.get('GCP_BUCKET_NAME')
bucketFolder = environ.get('GCP_BUCKET_FOLDER_NAME')

# Data
localFolder = environ.get('LOCAL_FOLDER')
