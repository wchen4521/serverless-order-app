import json

def lambda_handler(event, context):
    for record in event['Records']:
        print(f"Notification Received: {record['Sns']['Message']}")
    return {'statusCode': 200}
