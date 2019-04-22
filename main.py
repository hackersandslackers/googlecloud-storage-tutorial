from google.cloud import storage
from google.cloud import bigquery
import pprint

bucket_uri = 'gs://your-bucket/'
bucket_name = 'your-bucket'
bucket_target = 'datasets/data_upload.csv'
local_dataset = 'data/test.csv'
bucket_target_uri = bucket_uri + bucket_target
bigquery_dataset = 'uploadtest'
bigquery_table = 'my_table'


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Upload a CSV to Google Cloud Storage.

    1. Retrieve the target bucket.
    2. Set destination of data to be uploaded.
    3. Upload local CSV.
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    # Commence Upload
    blob.upload_from_filename(source_file_name)
    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


def insert_bigquery(target_uri, dataset_id, table_id):
    """Insert CSV from Google Storage to BigQuery Table.

    1. Specify target dataset within BigQuery.
    2. Create a Job configuration.
    3. Specify that we are autodetecting datatypes.
    4. Reserve row #1 for headers.
    5. Specify the source format of the file (defaults to CSV).
    6. Pass the URI of the data storage on Google Cloud Storage from.
    7. Load BigQuery Job.
    8. Execute BigQuery Job.
    """
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.skip_leading_rows = 1
    job_config.source_format = bigquery.SourceFormat.CSV
    uri = target_uri
    load_job = bigquery_client.load_table_from_uri(
        uri,
        dataset_ref.table(table_id),
        job_config=job_config)  # API request
    print('Starting job {}'.format(load_job.job_id))
    # Waits for table load to complete.
    load_job.result()
    print('Job finished.')


def get_schema(dataset_id, table_id):
    """Get BigQuery Table Schema.

    1. Specify target dataset within BigQuery.
    2. Specify target table within given dataset.
    3. Create Table class instance from existing BigQuery Table.
    4. Print results to console.
    5. Return the schema dict.
    """
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    bg_tableref = bigquery.table.TableReference(dataset_ref, table_id)
    bg_table = bigquery_client.get_table(bg_tableref)
    # Print Schema to Console
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(bg_table.schema)
    return bg_table.schema


upload_blob(bucket_name, local_dataset, bucket_target)
insert_bigquery(bucket_target_uri, bigquery_dataset, bigquery_table)
bigquery_table_schema = get_schema(bigquery_dataset, bigquery_table)
