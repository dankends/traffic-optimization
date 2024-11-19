# AWS Lambda Function for Real-Time Data Processing
# This function processes data from AWS Kinesis, performs transformations, and stores the results in S3.

import json
import boto3
import time

# Define the S3 bucket where processed data will be stored
s3 = boto3.client('s3')
bucket_name = 'your-s3-bucket-name'

def lambda_handler(event, context):
    # Process each record in the batch received from Kinesis
    for record in event['Records']:
        # Decode the base64-encoded data from Kinesis
        payload = json.loads(record['kinesis']['data'])
        
        # Data Transformation: Flag high traffic levels
        payload['high_traffic'] = payload['vehicle_count'] > 60
        
        # Save the processed data to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=f"processed-data/{payload['traffic_light_id']}/{int(time.time())}.json",
            Body=json.dumps(payload)
        )
    
    # Return success status
    return {'statusCode': 200, 'body': 'Data processed and saved to S3'}

