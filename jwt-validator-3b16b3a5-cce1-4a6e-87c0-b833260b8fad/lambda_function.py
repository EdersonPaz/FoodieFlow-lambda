import json
import boto3
from botocore.exceptions import ClientError

COGNITO_USER_POOL_ID = 'qs3pkap3mh9dq5conru8r1ncu'

def lambda_handler(event, context):
    print(json.dumps(event))
    token = event['identitySource'][0].split('Bearer ')[1]
    
    cognito_client = boto3.client('cognito-idp')
    try:
        response = cognito_client.get_user(
            AccessToken=token
        )
        
        return generate_policy('user', 'Allow', event['routeArn'])
            
    except ClientError as e:
        return generate_policy('user', 'Deny', event['routeArn'])

def generate_policy(principal_id, effect, resource):
    policy = {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [{
                'Action': 'execute-api:Invoke',
                'Effect': effect,
                'Resource': resource
            }]
        }
    }
    return policy