import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    body = json.loads(event['body'])
    order_id = body['order_id']
    status = body['status']

    table.update_item(
        Key={'order_id': order_id},
        UpdateExpression='SET delivery_status = :val',
        ExpressionAttributeValues={':val': status}
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Status updated for {order_id}'})
    }
