import boto3

dynamodb = boto3.resource('dynamodb')

response = client.delete_table(
    TableName='Cameras'
)