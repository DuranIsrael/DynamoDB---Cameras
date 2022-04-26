#I called this step 1 because we first must give python or our IDE (VSCODE for me) accesss to our AWSaccount in order to spin up and manipulate a table
#Make sure you have python downloaded on your local machine. From python you must download boto3 before doing this step.

import boto3

# replace the keys below with the desired AWS account you want to use. Make sure this accout had the correct permissions to create and manipulate DynamoDB

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='**********',
    aws_secret_access_key='************',
    )
