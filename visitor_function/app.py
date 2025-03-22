import json
import boto3
from decimal import Decimal
        
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-count')  # Replace with your table name
            
def lambda_handler(event, context):
    try:
        # Update the visitor count atomically
        response = table.update_item(
            Key={'id': '1'},  # Fixed ID
            UpdateExpression="SET #c = if_not_exists(#c, :start) + :inc",
            ExpressionAttributeNames={'#c': 'count'},
            ExpressionAttributeValues={':inc': 1, ':start': 0},
            ReturnValues="UPDATED_NEW"
        )
        # Get the updated count and convert from Decimal to int
        updated_count = response['Attributes']['count']

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # Required for frontend
            },  
            'body': json.dumps({'visitor-count': int(updated_count)})
        } 

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
        
