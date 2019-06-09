"""BigQuery Upload Configuration."""
from os import environ


# Google Cloud Storage
bucketURI = environ.get('GCP_BUCKET_URI')
bucketName = environ.get('GCP_BUCKET_NAME')

# Google BigQuery
bigqueryDataset = environ.get('GCP_BIGQUERY_DATASET')
bigqueryTable = environ.get('GCP_BIGQUERY_TABLE')

# Data
localDataFile = environ.get('LOCAL_DATA_TARGET')
destinationBlobName = environ.get('DESTINATION_BLOB_NAME')
