import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Cameras')

response = table.delete_item(Key = {'brand': 'Canon', 'model': 'EOS-R6'}) #here we are deleting a particular item from the table

print(response)
