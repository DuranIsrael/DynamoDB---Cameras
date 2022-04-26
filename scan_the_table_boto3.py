import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')#the resource or service we are calling is Dynamodb
table = dynamodb.Table('Camera')# here we are choosing our table

response = table.scan(FilterExpression=Attr('brand').eq('Canon'))

print("The query returned the following items:") 
for item in response['Items']:
    print(item) # this will print the scanned items
    
#in the terminal remeber to run these files using python. IE: python 'filename'
