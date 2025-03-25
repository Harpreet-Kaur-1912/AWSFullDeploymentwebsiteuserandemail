import json
import boto3

# Initialize AWS services
dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses')

def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event['body'])
        name = body.get('name')
        email = body.get('email')

        if not name or not email:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Name and email are required'})
            }

        # Store data in DynamoDB
        table = dynamodb.Table('Users')
        table.put_item(Item={'email': email, 'name': name})

        # Send confirmation email
        ses.send_email(
            Source='your-email@example.com',
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'Registration Successful'},
                'Body': {'Text': {'Data': f'Thank you, {name}, for signing up!'}}
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Success'})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
