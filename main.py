"""Programatically create a BigQuery table from a CSV."""
from google.cloud import storage
from google.cloud import bigquery
from config import bucketURI, bucketName, bigqueryDataset, bigqueryTable, localDataFile, destinationBlobName
import pprint


def storage_upload_blob(bucketName, source_file_name, destinationBlobName):
    """Upload a CSV to Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketName)
    blob = bucket.blob(destinationBlobName)
    blob.upload_from_filename(source_file_name)
    return 'File {} uploaded to {}.'.format(source_file_name,
                                            destinationBlobName)


def bigquery_insert_data(bucketURI, destinationBlobName, dataset_id, table_id):
    """Insert CSV from Google Storage to BigQuery Table."""
    target = bucketURI + destinationBlobName
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.skip_leading_rows = 1
    job_config.source_format = bigquery.SourceFormat.CSV
    load_job = bigquery_client.load_table_from_uri(target,
                                                   dataset_ref.table(table_id),
                                                   job_config=job_config)
    print('Starting job {}'.format(load_job.job_id))
    load_job.result()  # Waits for table load to complete.
    return 'Job finished.'


def get_table_schema(dataset_id, table_id):
    """Get BigQuery Table Schema."""
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    bg_tableref = bigquery.table.TableReference(dataset_ref, table_id)
    bg_table = bigquery_client.get_table(bg_tableref)
    # Print Schema to Console
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(bg_table.schema)
    return bg_table.schema


storage_upload_blob(bucketName,
                    localDataFile,
                    destinationBlobName)
bigquery_insert_data(bucketURI,
                     destinationBlobName,
                     bigqueryDataset,
                     bigqueryTable)
bigqueryTableSchema = get_table_schema(bigqueryDataset,
                                       bigqueryTable)
