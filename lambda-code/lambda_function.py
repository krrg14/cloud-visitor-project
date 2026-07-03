import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitorcount')

def lambda_handler(event, context):

    response = table.update_item(
        Key={'id': 'resume'},
        UpdateExpression='ADD #c :inc',
        ExpressionAttributeNames={
            '#c': 'count'
        },
        ExpressionAttributeValues={
            ':inc': 1
        },
        ReturnValues='UPDATED_NEW'
    )

    count = int(response['Attributes']['count'])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'count': count
        })
    }
