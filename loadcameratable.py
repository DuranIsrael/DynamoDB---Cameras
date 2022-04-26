
# this s the script to load the data into the table  
import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Cameras')
#here it is going to open the json file
with open("cameradata.json") as json_file:
    camera = json.load(json_file)
    for cameras in camera:
        brand = cameras['brand']
        model = cameras['model']

        print("Adding cameras:", brand, model)

        table.put_item(
           Item={
               'brand': brand,
               'model': model,
            }
        )
