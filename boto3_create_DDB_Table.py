import boto3 

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #we are calling the resource to let aws know we are creating a DDB table

table = dynamodb.create_table( #here is where we enter the table parameters.
    TableName='Cameras',
    KeySchema=[
        {
            'AttributeName': 'brand',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'model',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'brand',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'model',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status) #will print the status of the table. tell us the tabel is "creating"
