# This code snippet helps user to upload the dump files produced by MySQL Shell utility to Amazon S3 in multi-parts.

# Make to sure install boto3 package: pip3 install boto3
# Replace values for URI to connect appropiate source
# Set up AWS credentials (either through environment variables or AWS configuration files)
# Make sure your AWS credentials have the necessary permissions to write to the S3 bucket

import os
import boto3
import threading
from boto3.s3.transfer import TransferConfig
import subprocess

# The ProgressPercentage class
class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            print(f"Upload progress: {percentage:.2f}%")

def upload_to_s3_multipart(local_file_path, bucket_name, s3_file_path):
    
    # Create an S3 client
    s3 = boto3.client('s3')

    # Set up transfer configuration for multipart upload
    config = TransferConfig(
        multipart_threshold=8 * 1024 * 1024,  # 8 MB
        max_concurrency=10,
        multipart_chunksize=8 * 1024 * 1024,  # 8 MB
        use_threads=True
    )

    try:
        # Upload each file with multipart upload
        for file_name in os.listdir(local_file_path):
            local_file = os.path.join(local_file_path, file_name)
            s3_key = os.path.join(s3_file_path, file_name)
            
            # Upload the file with multipart upload
            s3.upload_file(local_file, bucket_name, s3_key, Config=config,
                           Callback=ProgressPercentage(local_file))
            print(f"File '{file_name}' uploaded successfully to {bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Defining S3 path and local directory path
local_dump_file_path = '/path/to/your/local/dump.sql'
s3_bucket_name = 'your-s3-bucket-name'
s3_file_path = 'path/in/s3/'

# Dump MySQL instance using MySQL Shell
mysqlsh_command = (
    f"mysqlsh --uri=mysql://username:password@hostname:3306/db_name "
    f"-e 'util.dumpInstance(\"{local_dump_file_path}\", "
    f"{{ "
    f"threads: 4, "
    f"showProgress: true, "
    f"consistent: false, "
    f'includeSchemas: ["db_schema"] '
    f"}});'"
)

# Uncomment the line below to execute MySQL Shell command
#subprocess.run(mysqlsh_command, shell=True, check=True)

# Upload to S3 using multipart upload
upload_to_s3_multipart(local_dump_file_path, s3_bucket_name, s3_file_path)



