import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-count')

def lambda_handler(event, context):
    response = table.get_item(Key={'id': '1'})  # Query using id "1"
    
    count = response.get('Item', {}).get('count', 0)  # Default to 0 if missing

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"visitor_count": count})
    }
