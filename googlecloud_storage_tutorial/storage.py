"""Programmatically interact with a Google Cloud Storage bucket."""

from os import listdir
from os.path import isfile, join
from random import randint
from typing import List, Optional, Tuple

from google.cloud import storage
from google.cloud.storage.blob import Blob

from config import BUCKET_DIR, BUCKET_NAME

# Initialize Google Cloud Storage client
storage_client = storage.Client()
bucket = storage_client.get_bucket(BUCKET_NAME)


def list_files() -> List[Optional[str]]:
    """
    List all objects with file extension in a GCP bucket.

    :param str bucket_name: Human-readable GCP bucket name.
    :param str bucket_dir: Bucket directory in which object exists.

    :returns: List[Optional[str]]
    """
    blobs = bucket.list_blobs(prefix=BUCKET_DIR)
    blob_file_list = [blob.name for blob in blobs if "." in blob.name]
    return blob_file_list


def pick_random_file() -> str:
    """
    Pick a `random` file from GCP bucket.

    :param str bucket_name: Human-readable GCP bucket name.

    :returns: str
    """
    blobs = list_files()
    rand = randint(0, len(blobs) - 1)
    blob = bucket.blob(blobs[rand])
    return blob, blob.name


def download_random_file(local_dir: str) -> Tuple[Blob, str]:
    """
    Download random file from GCP bucket.

    :param str bucket_name: Human-readable GCP bucket name.
    :param str bucket_dir: Bucket directory in which object exists.
    :param str local_dir: Local file path to upload/download files.

    :returns: str
    """
    blob, blob_filename = pick_random_file()
    blob.download_to_filename(f"{local_dir}/{blob.name.split('/')[-1]}")
    return blob, blob_filename


def delete_file(bucket_name: str) -> str:
    """
    Delete file from GCP bucket.

    :param str bucket_name: Human-readable GCP bucket name.
    :param str bucket_dir: Bucket directory in which object exists.

    :returns: str
    """
    blob, blob_filename = pick_random_file()
    bucket.delete_blob(blob_filename)
    return f"{blob_filename} deleted from bucket: {bucket_name}."


def rename_file(new_filename: str) -> str:
    """
    Rename a file in GCP bucket.

    :param str bucket_name: Human-readable GCP bucket name.
    :param str bucket_dir: Bucket directory from which to extract object.
    :param str new_filename: New file name for Blob object.

    :returns: str
    """
    blob, blob_filename = pick_random_file()
    bucket.rename_blob(blob, new_name=new_filename)
    return f"{blob_filename} renamed to {new_filename}."


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
        local_file = f"{local_dir}/{file}"
        print(f"local file = {local_file}\n")
        blob = bucket.blob(f"{bucket_dir}/{file}")
        blob.upload_from_filename(local_file)
    return f"Uploaded {files} to '{bucket_name}' bucket."
