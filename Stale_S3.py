import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Create S3 client
    s3 = boto3.client('s3')

    # Get list of all S3 buckets
    response = s3.list_buckets()

    # Get current timestamp
    current_time = datetime.now()

    # Define a timedelta for cutoff time (e.g., 30 days)
    cutoff_time = current_time - timedelta(days=30)

    # Iterate through each bucket
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        
        # Check if the bucket is empty
        objects_response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects_response:
            last_modified = max(obj['LastModified'] for obj in objects_response['Contents'])
            # If the bucket has been inactive for more than 30 days, delete it
            if last_modified < cutoff_time:
                print(f"Deleting stale bucket: {bucket_name}")
                s3.delete_bucket(Bucket=bucket_name)
        else:
            # If the bucket is empty, delete it
            print(f"Deleting empty bucket: {bucket_name}")
            s3.delete_bucket(Bucket=bucket_name)
