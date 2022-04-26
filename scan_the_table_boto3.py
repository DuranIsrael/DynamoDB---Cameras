import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Camera')

response = table.scan(FilterExpression=Attr('brand').eq('Canon'))

print("The query returned the following items:")
for item in response['Items']:
    print(item)
