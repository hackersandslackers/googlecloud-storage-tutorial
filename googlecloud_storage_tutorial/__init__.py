"""Initialize script."""

from faker import Faker

from config import BUCKET_DIR, BUCKET_NAME, LOCAL_DIR
from googlecloud_storage_tutorial.storage import (
    delete_file,
    download_random_file,
    list_files,
    rename_file,
    upload_files,
)

# Using the `faker` library to generate random strings
fake = Faker()


def init_script():
    """Initialize script demonstration."""
    upload_files(BUCKET_NAME, BUCKET_DIR, LOCAL_DIR)
    list_files()
    download_random_file(LOCAL_DIR)
    rename_file(fake.unique.first_name())
    delete_file(BUCKET_NAME)
    upload_files(BUCKET_NAME, BUCKET_DIR, LOCAL_DIR)
