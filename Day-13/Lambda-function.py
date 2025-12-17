import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='s3-bauket-demo-123',
)