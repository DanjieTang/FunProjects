import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create an S3 client using the default session (which uses the credentials and region configured with aws configure)
s3_client = boto3.client('s3')

# Define the bucket name and the object key
bucket_name = 'enter-your-bucket-name'
object_key = 'enter-your-object-name' # Example 'myfolder/example.txt'
download_path = 'enter-your-file-name' # Example 'lmao.txt' This is downloaded to the current directory that is running the script(python download_from_s3.py).

try:
    # Download the object
    s3_client.download_file(bucket_name, object_key, download_path)
    print(f'Successfully downloaded {object_key} from {bucket_name} to {download_path}')
except NoCredentialsError:
    print('Credentials not available.')
except PartialCredentialsError:
    print('Incomplete credentials provided.')
except Exception as e:
    print(f'Error downloading the object: {e}')
