"""Initialize script demonstration"""

from faker import Faker

from config import BUCKET_DIR, BUCKET_NAME, LOCAL_DIR
from googlecloud_storage_tutorial.storage import (
    delete_file,
    download_random_file,
    list_files,
    rename_file,
    upload_files,
)

fake = Faker()


def init_script():
    """Initialize script demonstration."""
    print(upload_files(BUCKET_NAME, BUCKET_DIR, LOCAL_DIR))
    print(list_files())
    print(download_random_file(LOCAL_DIR))
    print(rename_file(fake.unique.first_name()))
    print(delete_file(BUCKET_NAME))
    upload_files(BUCKET_NAME, BUCKET_DIR, LOCAL_DIR)
