"""Programatically create a BigQuery table from a CSV."""
from os import listdir
from os.path import isfile, join
from random import randint
from google.cloud import storage
from config import bucketURI, bucketName, localFolder, bucketFolder


def upload_files(bucketName):
    """Upload files to bucket."""
    files = [f for f in listdir(localFolder) if isfile(join(localFolder, f))]
    print(files)
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketName)
    for file in files:
        localFile = localFolder + file
        blob = bucket.blob(bucketFolder + file)
        blob.upload_from_filename(localFile)
    return f'Uploaded {files} to "{bucketName}" bucket.'


def list_files(bucketName):
    """List all files in bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketName)
    files = bucket.list_blobs(prefix=bucketFolder)
    fileList = [file.name for file in files if '.' in file.name]
    print('fileList:', fileList)
    return fileList


def download_random_file(bucketURI, bucketName, bucketFolder):
    """Get random file from bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketName)
    fileList = list_files(bucketName)
    rand = randint(0, len(fileList) - 1)
    blob = bucket.blob(fileList[rand])
    fileName = blob.name.split('/')[-1]
    blob.download_to_filename('./files/' + fileName)
    return fileName


def delete_file(bucketName, bucketFolder, fileName):
    """Delete file from bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketName)
    bucket.delete_blob(bucketFolder + fileName)
    return f'{fileName} deleted from bucket.'


def rename_file(bucketName, bucketFolder, fileName, newFileName):
    """Delete file from bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketName)
    bucket.rename_blob(bucketFolder + fileName,
                       new_name=newFileName)
    return f'{fileName} renamed to {newFileName}.'


print(upload_files(bucketName))
print(list_files(bucketName))
print(download_random_file(bucketURI,
                           bucketName,
                           bucketFolder))
print(rename_file(bucketName,
                  bucketFolder,
                  'test.csv',
                  'sample_test.csv'))
print(delete_file(bucketName,
                  bucketFolder,
                  'sample_text.txt'))
