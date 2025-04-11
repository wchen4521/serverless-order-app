import json
import boto3
import os
import uuid

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    order_id = str(uuid.uuid4())
    body = json.loads(event['body'])
    body['order_id'] = order_id

    table.put_item(Item=body)
    sns.publish(
        TopicArn=os.environ['TOPIC_ARN'],
        Message=json.dumps({'default': f"Order {order_id} has been placed."}),
        MessageStructure='json'
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Order placed', 'order_id': order_id})
    }
