import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create an S3 client using the default session (which uses the credentials and region configured with aws configure)
s3_client = boto3.client('s3')

# Define the bucket name and the object key
bucket_name = 'danjie-personal'
object_key = 'lmao/loll.png'  # The path in the bucket where the file will be stored
file_path = 'ready.png'  # Local path of the file to be uploaded

try:
    # Upload the file
    s3_client.upload_file(file_path, bucket_name, object_key)
    print(f'Successfully uploaded {file_path} to s3://{bucket_name}/{object_key}')
except NoCredentialsError:
    print('Credentials not available.')
except PartialCredentialsError:
    print('Incomplete credentials provided.')
except Exception as e:
    print(f'Error uploading the object: {e}')
