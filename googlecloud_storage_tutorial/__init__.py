"""Initialize script demonstration"""
from config import bucket_dir, bucket_name, local_dir
from googlecloud_storage_tutorial.storage import (
    delete_file,
    download_random_file,
    list_files,
    rename_file,
    upload_files,
)


def init_script():
    print(upload_files(bucket_name))
    print(list_files(bucket_name))
    print(download_random_file(bucket_name, bucket_dir, local_dir))
    print(rename_file(bucket_name, bucket_dir, "test.csv", "sample_test.csv"))
    print(delete_file(bucket_name, bucket_dir, "sample_text.txt"))
