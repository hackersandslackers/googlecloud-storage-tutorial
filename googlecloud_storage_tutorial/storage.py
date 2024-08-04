"""Programmatically interact with a Google Cloud Storage bucket."""
from os import listdir
from os.path import isfile, join
from random import randint
from typing import List, Optional

from google.cloud import storage

from config import bucket_dir, bucket_name, local_dir

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)


def upload_files(bucket_name: str, bucket_dir: str, local_dir: str) -> str:
    """
    Upload files to GCP bucket.

    :param str bucket_name: Human-readable GCP bucket name.
    :param str bucket_dir: Bucket directory in which object exists.
    :param str local_dir: Local file path to upload/download files.

    :returns: str
    """
    files = [f for f in listdir(local_dir) if isfile(join(local_dir, f))]
    for file in files:
        local_file = local_dir + file
        blob = bucket.blob(bucket_dir + file)
        blob.upload_from_filename(local_file)
    return f"Uploaded {files.join(', ')} to '{bucket_name}' bucket."


def list_files(bucket_dir: str) -> List[Optional[str]]:
    """
    List all objects with file extension in a GCP bucket.

    :param str bucket_name: Human-readable GCP bucket name.
    :param str bucket_dir: Bucket directory in which object exists.

    :returns: List[Optional[str]]
    """
    files = bucket.list_blobs(prefix=bucket_dir)
    file_list = [file.name for file in files if "." in file.name]
    return file_list


def download_random_file(bucket_name: str, local_dir: str) -> str:
    """
    Download random file from GCP bucket.

    :param str bucket_name: Human-readable GCP bucket name.
    :param str bucket_dir: Bucket directory in which object exists.
    :param str local_dir: Local file path to upload/download files.

    :returns: str
    """
    fileList = list_files(bucket_name)
    rand = randint(0, len(fileList) - 1)
    blob = bucket.blob(fileList[rand])
    file_name = blob.name.split("/")[-1]
    blob.download_to_filename(local_dir + file_name)
    return f"{file_name} downloaded from bucket."


def delete_file(bucket_name: str, bucket_dir: str) -> str:
    """
    Delete file from GCP bucket.

    :param str bucket_name: Human-readable GCP bucket name.
    :param str bucket_dir: Bucket directory in which object exists.

    :returns: str
    """
    blob = bucket.blob(bucket_dir + file_name)
    file_name = blob.name.split("/")[-1]
    bucket.delete_blob(bucket_name + file_name)
    return f"{file_name} deleted from bucket: {bucket_name}."


def rename_file(bucket_dir: str, new_filename: str) -> str:
    """
    Rename a file in GCP bucket.

    :param str bucket_name: Human-readable GCP bucket name.
    :param str bucket_dir: Bucket directory from which to extract object.
    :param str new_filename: New file name for Blob object.

    :returns: str
    """
    blob = bucket.blob(bucket_dir + file_name)
    file_name = blob.name.split("/")[-1]
    bucket.rename_blob(blob, new_name=new_filename)
    return f"{file_name} renamed to {new_filename}."
